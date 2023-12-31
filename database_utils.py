import yaml
from sqlalchemy import create_engine, inspect


class DatabaseConnector:
    def __init__(self, creds_file_path):
        '''
        Initializes the database connector

        Parameters:
        creds_file_path (string): the file name containing the credentials
        '''
        self.creds_file_path = creds_file_path
    
    def read_db_creds(self):
        '''
        Reads the credentials initialized in "__init__"

        Returns:
        yaml: credentials needed for the database engine
        '''
        with open(self.creds_file_path, 'r') as file:
            data = yaml.safe_load(file)
        return data
    
    def init_db_engine(self):
        '''
        Initializes the engine to link to the original database

        Returns:
        Engine: created to link to database
        '''
        creds = self.read_db_creds()
        db_url = f"postgresql+psycopg2://{creds['RDS_USER']}:{creds['RDS_PASSWORD']}@{creds['RDS_HOST']}:{creds['RDS_PORT']}/{creds['RDS_DATABASE']}"
        engine = create_engine(db_url)
        return engine
    
    def list_db_tables(self):
        '''
        Lists the table names in the database
        '''
        engine = self.init_db_engine()
        inspector = inspect(engine)
        table_list = inspector.get_table_names()
        print(table_list)
        
    def upload_to_db(self, df, table_name):
        '''
        Upload a Pandas DataFrame to a specified database table.

        Parameters:
        - df (pd.DataFrame): DataFrame to be uploaded.
        - table_name (str): Name of the destination database table.
        '''
        engine = self.init_db_engine()
        df.to_sql(table_name, engine)
            
            
if __name__ == "__main__":
    DBC = DatabaseConnector()
    DBC.init_db_engine()
    DBC.list_db_tables()
