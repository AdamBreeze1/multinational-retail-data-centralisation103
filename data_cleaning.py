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
            removed_null_df = df.replace('NULL', pd.NA).dropna()
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
            df[column_name] = pd.to_datetime(df[column_name])
            return df
        
        def check_for_duplicates(self, df, column_names):
            """
            Parameters:
            - df (pd.DataFrame): Input DataFrame.
            - column_names (str): Name of the column(s) to be checked for duplicates.
            """
            duplicates_mask = df[column_names].duplicated(keep=False)
            duplicated_df = df[duplicates_mask]
            return duplicated_df
        
        def convert_product_weight(self, weight_str):
            '''
            Converts a string of various weights into a float in kg

            Parameter:
            - weight_str (string): single weight string to convert
            '''
            if 'x' in weight_str:
                # Handle cases like '5 x 820g'
                parts = weight_str.split('x')
                multiplier = float(parts[0].strip())
                weight_value = float(parts[1].replace('g', '').strip()) / 1000  # Convert grams to kilograms
                total_weight_value = multiplier * weight_value
                return total_weight_value
            else:
                # Handle other cases ending 'kg', 'g' or 'ml'
                weight_value = float(weight_str.replace('kg', '').replace('g', '').replace('ml', '').replace('oz', '').strip())
                if 'kg' in weight_str:
                    return weight_value
                elif 'oz' in weight_str:
                    weight_value *= (28.413075/1000) # Convert oz to kg
                    return weight_value
                else:
                    weight_value /= 1000  # Convert grams or ml (estimate) to kilograms
                    return weight_value
        
        def concatenate_columns(self, df, new_column, columns, separator=' '):
            '''
            Concatinates values in a columns to create a new column

            Parameters:
            - df (pd.DataFrame): Input DataFrame.
            - columns (list): List of columns in order you want them concatinated
            - separator (string): default is ' '
            '''
            df[new_column] = df[columns].astype(str).apply(lambda row: separator.join(row), axis=1)
            return df