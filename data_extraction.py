import pandas as pd
from database_utils import DatabaseConnector


class DataExtraction:
    def read_rds_table(self, table_name, engine):
        query = f"SELECT * FROM {table_name}"
        df = pd.read_sql_query(query, con=engine, index_col="index")
        return df

if __name__ == "__main__":
    DBC = DatabaseConnector("db_creds.yaml")
    DE = DataExtraction(DBC)
