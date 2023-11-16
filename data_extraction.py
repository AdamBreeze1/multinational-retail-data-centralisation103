import pandas as pd
from database_utils import DatabaseConnector
import tabula
import store_header
import requests

database_connector = DatabaseConnector()


class DataExtraction:
    def read_rds_table(self, table_name):
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
        for store_number in list(range(451)):
            url = f"https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/{store_number}"
            response = requests.get(url=url, headers=header)
            store_data_json = response.json()
            store_data_df = pd.json_normalize(store_data_json)
            return store_data_df
    
