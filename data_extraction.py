import pandas as pd
from database_utils import DatabaseConnector
import tabula
import store_header
import requests
import boto3
from botocore import UNSIGNED
from botocore.config import Config


class DataExtraction:
    def read_rds_table(self, table_name):
        database_connector = DatabaseConnector()
        with database_connector.init_db_engine().connect() as con:
            query = f"SELECT * FROM {table_name}"
            df = pd.read_sql_query(query, con=con, index_col="index")
            return df
        
    def retrieve_pdf_data(self, path_to_pdf="https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf"):
        list_of_df = tabula.read_pdf(path_to_pdf, pages="all")
        df = pd.concat(list_of_df, ignore_index=True)
        return df
    
    def list_number_of_stores(self, url="https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores", header=store_header.header_dict):
        respose = requests.get(url=url, headers=header)
        return respose.text
    
    def retrieve_stores_data(self, header=store_header.header_dict):
        '''
        Retrieves stores dat line by line.
        ***Takes a long time (10 minutes)***
        '''
        # Create an empty DataFrame to store the results
        all_store_data_df = pd.DataFrame()

        for store_number in range(451):
            url = f"https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/{store_number}"
            response = requests.get(url=url, headers=header)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                store_data_json = response.json()
                store_data_df = pd.json_normalize(store_data_json)

                # Append the data to the main DataFrame
                all_store_data_df = pd.concat([all_store_data_df, store_data_df], ignore_index=True)

        return all_store_data_df
    
    def extract_from_s3(self):
        s3 = boto3.client("s3", region_name="eu-west-1", config=Config(signature_version=UNSIGNED))

        # Specify the S3 bucket name, object key, and local file path
        bucket_name = "data-handling-public"
        object_name = "products.csv"
        local_file_path = "original_dfs/original_products.csv"

        # Download the file from S3 to the local file path
        s3.download_file(bucket_name, object_name, local_file_path) 
        print(f"Download successful. File saved at {local_file_path}")

        # Read the CSV file into a DataFrame
        df = pd.read_csv(local_file_path)
        return df
