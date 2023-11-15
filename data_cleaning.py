from database_utils import DatabaseConnector
from data_extraction import DataExtraction
import pandas as pd
from dateutil.parser import parse


class DataCleaning:

        def clean_null(self, df):
            """
            Drops rows that contain null values.
            
            Parameters:
            - df (pd.DataFrame): Input DataFrame.

            Returns:
            pd.DataFrame: DataFrame after dropping null values.
            """
            removed_null_df = df.dropna()
            return removed_null_df

        def clean_rows_by_length_condition(self, df, column_name, max_length=3):
            """
            Drop rows from a DataFrame based on a condition for a specific column.

            Parameters:
            - df (pd.DataFrame): Input DataFrame.
            - column_name (str): Name of the column to check the condition.
            - max_length (int): Maximum allowed string length for the column value.

            Returns:
            - pd.DataFrame: DataFrame after dropping rows based on the condition.
            """
            condition = df[column_name].str.len() > max_length
            cleaned_df = df[~condition]
            return cleaned_df
        
        @staticmethod
        def clean_replace_value_in_column(df, column_name, old_value, new_value):
            """
            Replace a specific value in a column of a DataFrame.

            Parameters:
            - df (pd.DataFrame): Input DataFrame.
            - column_name (str): Name of the column where the replacement will occur.
            - old_value: The value to be replaced.
            - new_value: The value to replace old_value with.

            Returns:
            - pd.DataFrame: DataFrame after the replacement.
            """
            df[column_name] = df[column_name].replace(old_value, new_value)
            return df
        
        @staticmethod
        def clean_convert_date_column(df, column_name):
            """
            Convert a column containing date strings to a datetime format.

            Parameters:
            - df (pd.DataFrame): Input DataFrame.
            - column_name (str): Name of the column to be converted.

            Returns:
            - pd.DataFrame: DataFrame with the converted column.
            """
            df[column_name] = df[column_name].apply(parse)
            df[column_name] = pd.to_datetime(df[column_name], infer_datetime_format=True)
            return df
        
