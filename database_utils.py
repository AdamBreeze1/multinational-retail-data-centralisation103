import yaml
from sqlalchemy import create_engine, text, inspect
import pandas as pd
import psycopg2


class DatabaseConnector:
    def __init__(self, file_path = "db_creds.yaml"):
        self.file_path = file_path
    
    def read_db_creds(self):
        with open(self.file_path, 'r') as file:
            data = yaml.safe_load(file)
        return data
    
    def init_db_engine(self):
        creds = self.read_db_creds()
        db_url = f"postgresql+psycopg2://{creds['RDS_USER']}:{creds['RDS_PASSWORD']}@{creds['RDS_HOST']}:{creds['RDS_PORT']}/{creds['RDS_DATABASE']}"
        engine = create_engine(db_url)
        return engine
    
    def list_db_tables(self):
        engine = self.init_db_engine()
        inspector = inspect(engine)
        table_list = inspector.get_table_names()
        print(table_list)


DBC = DatabaseConnector()

if __name__ == "__main__":
    DBC.init_db_engine()
    DBC.list_db_tables()
