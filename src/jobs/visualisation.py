import plotly.express as px
import pycountry
from pyspark.sql.functions import udf
import pycountry_convert as pcc
from fuzzywuzzy import process
from pyspark.sql import SparkSession
from pyspark.sql.types import StringType


spark = SparkSession.builder.appName('Processing').master('spark://172.28.0.2:7077').getOrCreate()
print("SparkSession created successfully.")


#df = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("inputs/visa_number_in_japan.csv")
df = spark.read.csv('/opt/bitnami/spark/input/visa_number_in_japan.csv', header=True, inferSchema=True)
#data = [("Alice", 1), ("Bob", 2), ("Cathy", 3)]
#df = spark.createDataFrame(data, ["Name", "Id"])

# standardize or clean the columns
new_column_names = [col_name.replace(' ', '_')
                    .replace('/', '')
                    .replace('.', '')
                    .replace(',', '')
                    for col_name in df.columns]
df = df.toDF(*new_column_names)

df= df.dropna(how='all')

df = df.select('year', 'country', 'number_of_issued_numerical')

def correct_country_name(name, threshold=85):
    countries = [country.name for country in pycountry.countries]

    corrected_name, score = process.extractOne(name, countries)

    if score >= threshold:
        return corrected_name

    # no changes
    return name

def get_continent_name(country_name):
    try:
        country_code = pcc.country_name_to_country_alpha2(country_name, cn_name_format='default')
        continent_code = pcc.country_alpha2_to_continent_code(country_code)
        return pcc.convert_continent_code_to_continent_name(continent_code)
    except:
        return None

correct_country_name_udf = udf(correct_country_name, StringType())
df = df.withColumn('country', correct_country_name_udf(df['country']))


country_corrections = {
    'Andra': 'Russia',
    'Antigua Berbuda': 'Antigua and Barbuda',
    'Barrane': 'Bahrain',
    'Brush': 'Bhutan',
    'Komoro': 'Comoros',
    'Benan': 'Benin',
    'Kiribass': 'Kiribati',
    'Gaiana': 'Guyana',
    'Court Jiboire': "Côte d'Ivoire",
    'Lesot': 'Lesotho',
    'Macau travel certificate': 'Macao',
    'Moldoba': 'Moldova',
    'Naure': 'Nauru',
    'Nigail': 'Niger',
    'Palao': 'Palau',
    'St. Christopher Navis': 'Saint Kitts and Nevis',
    'Santa Principa': 'Sao Tome and Principe',
    'Saechel': 'Seychelles',
    'Slinum': 'Saint Helena',
    'Swaji Land': 'Eswatini',
    'Torque menistan': 'Turkmenistan',
    'Tsubaru': 'Zimbabwe',
    'Kosovo': 'Kosovo'
}

df = df.replace(country_corrections, subset='country')

continent_udf = udf(get_continent_name, StringType())
df = df.withColumn('continent', continent_udf(df['country']))

df.createGlobalTempView('japan_visa')

# VISUALISATION
df_cont = spark.sql("""
    SELECT year, continent, sum(number_of_issued_numerical) visa_issued
    FROM global_temp.japan_visa
    WHERE continent IS NOT NULL
    GROUP BY year, continent
""")

df_cont = df_cont.toPandas()

fig = px.bar(df_cont, x='year', y='visa_issued', color='continent', barmode='group')

fig.update_layout(title_text="Top 10 countries with most issued visa in 2017",
                  xaxis_title='Country',
                  yaxis_title='Number of visa issued',
                  legend_title='Country')

fig.write_html('output/visa_number_in_japan_by_country_2017.html')


df.show()

spark.stop()



#sudo docker exec -it maddy-spark-worker-1 spark-submit --master spark://172.18.0.2:7077 jobs/visualisation.py