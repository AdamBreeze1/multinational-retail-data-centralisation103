import yaml


class DatabaseConnector:
    # def __init__(self):
    #     return self
    
    def read_db_creds(file_path):
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
        return data
    

Data_dict = DatabaseConnector.read_db_creds("db_creds.yaml")
print(Data_dict)

