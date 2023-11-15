import pandas as pd
from database_utils import DatabaseConnector
import tabula

database_connector = DatabaseConnector()


class DataExtraction:
    def read_rds_table(self, table_name):
        with database_connector.init_db_engine().connect() as con:
            query = f"SELECT * FROM {table_name}"
            df = pd.read_sql_query(query, con=con, index_col="index")
            return df
        
    def retrieve_pdf_data(self, path_to_pdf="https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf"):
        df = tabula.read_pdf(path_to_pdf)
        return df
