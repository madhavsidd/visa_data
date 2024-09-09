from pyspark.sql import SparkSession


spark = SparkSession.builder.appName('Processing').getOrCreate()
print("SparkSession created successfully.")


#df = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("inputs/visa_number_in_japan.csv")
#df = spark.read.csv('/opt/bitnami/spark/input/*', header=True, inferSchema=True)
data = [("Alice", 1), ("Bob", 2), ("Cathy", 3)]
df = spark.createDataFrame(data, ["Name", "Id"])

# standardize or clean the columns
#new_column_names = [col_name.replace(' ', '_')
#                   .replace('/', '')
 #                  .replace('.', '')
  #                  .replace(',', '')
   #                 for col_name in df.columns]
#df = df.toDF(*new_column_names)

#df= df.dropna(how='all')

#df = df.select('year', 'country', 'number_of_issued_numerical')

df.show()

spark.stop()



#sudo docker exec -it maddy-spark-worker-1 spark-submit --master spark://172.18.0.2:7077 jobs/visualisation.py