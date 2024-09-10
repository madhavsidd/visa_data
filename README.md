
# Japan Visa Analysis: GCP End-to-End Data Engineering 🌐

This project contains a comprehensive solution for analyzing and visualizing visa issuance data in Japan. The project uses PySpark for data processing and Plotly for visualization, running in a Dockerized Spark environment on Google Cloud Platform (GCP).

## 📚 Overview
- [Architecture](docs/architecture.md)
- [Setup Guide](docs/setup.md)
- [How to Run](docs/run.md)
- [Features & Capabilities](docs/features.md)

# Architecture

![flow drawio](https://github.com/user-attachments/assets/0e150f5f-2276-403e-8f42-aa3c037fda6c)


## System Design

This project leverages a Dockerized Spark cluster on Google Cloud Platform (GCP) to handle data processing. The architecture includes:

- **Spark Master**: Orchestrates the cluster and coordinates tasks.
- **Spark Workers**: Perform distributed data processing.

The cluster setup is containerized using Docker, which provides a flexible and scalable environment for handling large datasets.

# Setup Guide

## Prerequisites

1. **Google Cloud Platform (GCP) Account**: Ensure you have a GCP account with the necessary permissions.
2. **Docker**: Make sure Docker is installed to manage the Spark containers.
3. **Python Libraries**: Install these libraries to run the data processing script:
   - `pyspark`
   - `plotly`
   - `pycountry`
   - `pycountry_convert`
   - `fuzzywuzzy`
   
   Install using pip:
   
   pip install pyspark plotly pycountry pycountry_convert fuzzywuzzy


### 4. `docs/run.md`

## Installation Steps

**Clone the Repository**:
   
   git clone https://github.com/this-repo.git
   cd this-repo-directory

# How to Run

## Data Preparation

Place your CSV file, `visa_number_in_japan.csv`, into the `input` directory of the project.

## Executing the Script

Run the following command to start the data processing with Spark:

spark-submit --master spark://<spark-master-url>:7077 jobs/visualisation.py



### 5. `docs/features.md`


# Features & Capabilities

- **Dockerized Spark Cluster**: The project runs on a scalable Spark cluster managed by Docker on GCP.
- **Data Ingestion**: Processes CSV data files for visa numbers.
- **Data Cleaning**: Includes standardization and correction of country names.
- **Data Transformation**: Enriches data with continent information for enhanced insights.
- **Visualization**: Utilizes Plotly to create interactive and insightful visualizations of visa data trends.


# Additional Notes

- **Configuration**: Ensure that GCP and Docker are properly configured for seamless integration with Spark.

## Inspiration

This project was inspired by the YouTube video:

[**Japan Visa Analysis: Azure End to End Data Engineering**](https://www.youtube.com/watch?v=f-IcM8mFmDc)

The video provided valuable insights and guidance for setting up the end-to-end data engineering pipeline. The original project used Azure, and this version has been adapted to use Google Cloud Platform (GCP).

