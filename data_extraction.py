import pandas as pd
from database_utils import DatabaseConnector
import tabula
import store_header
import requests
import boto3
from botocore import UNSIGNED
from botocore.config import Config
import json


class DataExtraction:
    def read_rds_table(self, table_name):
        '''
        Reads the table and returns a DataFrame

        Parameters:
        table_name (string): table name you want to read 

        Returns:
        pd.DataFrame: of the table
        '''
        with database_connector.init_db_engine().connect() as con:
            query = f"SELECT * FROM {table_name}"
            df = pd.read_sql_query(query, con=con, index_col="index")
            return df
        
    def retrieve_pdf_data(self, path_to_pdf):
        '''
        Reads a table in a pdf and returns a DataFrame

        Parameters:
        path_to_pdf (string): the url for the pdf table you want to read

        Returns:
        pd.DataFrame: of the table
        '''
        list_of_df = tabula.read_pdf(path_to_pdf, pages="all")
        df = pd.concat(list_of_df, ignore_index=True)
        return df
    
    def list_number_of_stores(self, url, header=store_header.api_key):
        '''
        Returns the number of stores from the url

        parameters:
        url (string): url of the data for the stores number

        Returns: 
        int: the number of stores as an integer
        '''
        response = requests.get(url=url, headers=header)
        data = response.json()
        number_stores = data['number_stores']
        return int(number_stores)
    
    def retrieve_stores_data(self, data_url_path, number_stores_url, header=store_header.api_key):
        '''
        Retrieves stores dat line by line.
        ***Takes a long time (10 minutes)***

        Parameters:
        - number_stores_url (string): url for the stores data.
        - data_url_path (string): url for the count of stores.

        Returns:
        pd.DataFrame: df of all the stores data
        '''
        # Create an empty DataFrame to store the results
        all_store_data_df = pd.DataFrame()

        for store_number in range(self.list_number_of_stores(number_stores_url)):
            url = data_url_path + str(store_number)
            response = requests.get(url=url, headers=header)
            
            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                store_data_json = response.json()
                store_data_df = pd.json_normalize(store_data_json)

                # Append the data to the main DataFrame
                all_store_data_df = pd.concat([all_store_data_df, store_data_df], ignore_index=True)

        return all_store_data_df
    
    def extract_from_s3(self, bucket_name, object_name, local_file_path):
        s3 = boto3.client("s3", region_name="eu-west-1", config=Config(signature_version=UNSIGNED))

        # Download the file from S3 to the local file path
        s3.download_file(bucket_name, object_name, local_file_path) 
        print(f"Download successful. File saved at {local_file_path}")

        # Read the CSV file into a DataFrame
        df = pd.read_csv(local_file_path)
        return df
