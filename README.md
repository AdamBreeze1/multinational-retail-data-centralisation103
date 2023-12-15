# Multinational Retail Data Centralisation Project

## Table of Contents
1. [Brief](#brief)
1. [Project Description](#project-description)
1. [Installation Instructions](#installation-instructions)
1. [Usage Instructions](#usage-instructions)
1. [File Structure](#file-structure)
1. [License Information](#liscense-information)

## Brief
You work for a multinational company that sells various goods across the globe.

Currently, their sales data is spread across many different data sources making it not easily accessible or analysable by current members of the team.

### Project Aim
This project aim is to develope multiple data pipelines to access the sales data all in one place.

### Order of actions:
1. Retrieve data from different sources.
1. Clean the data (removing junk data, corecting typos, etc...)
1. Upload the data to a central PostgeSQL database.
1. Use SQL to correct the data types.
1. Link the tables together with the central orders_table by setting the primary and foreign keys.
1. Query the data to answer questions from the boss to give up-to-date information on the sales data.

## What I Have Learned
This project has helped me develop Data Engineering skills through real-world practical applications such as:
- Creating data pipelines from a variety of sources.
- Cleaning data through Python functions.
- Developing a star based database schema with and correcting data types.
- Write SQL queries that provide up to date information.

## Installation Instructions
Copy the repository from the GitHub page
https://github.com/AdamBreeze1/multinational-retail-data-centralisation103.git

Then clone in your terminal using:
'git clone https://github.com/example_repository folder-name'

## Usage Instructions
The credentials for this demonstration are hidden to protect the sources, however, the below is how the project works.

1. Run all in "main.ipynb" 
1. Open and run the required .sql query from "Folder SQL Files" in PGAdmin.

## File Structure
- main.ipynb (main file that run the code)
- .gitignore
- database_utils.py (base engine creation and uploads)
- data_extraction.py (extraction from different data sources)
- data_cleaning.py (cleans data, removing errors)
- db_creds.yaml (not added to repository)
- store_header.py (not added to repository)
- Folder original_dfs (contains the original extracted data)
- Folder cleaned_dfs (empty folder location to store cleaned data for review)
- Folder SQL Files (SQL code to answer a number of analysis questions)


## License information
This project is open-source and available under the MIT License.