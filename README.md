# Multinational Retail Data Centralisation Project

## Table of Contents
1. (Brief)[#brief]
1. (Project Discription)[#project-discription]
1. (Installation Instructions)[#installation-instructions]
1. (Usage Instructions)[#usage-instructions]
1. (File Structure)[#file-structure]
1. (Liscense Information)[#liscense-information]

## Brief
You work for a multinational company that sells various goods across the globe.

Currently, their sales data is spread across many different data sources making it not easily accessible or analysable by current members of the team.

## Project Discription
This project aim is the develope multiple data pipelines to access the sales data all in one place.

Order of actions:
1. Retrieve data from different sources.
1. Clean the data (removing junk data, corecting typos, changing data types, etc...)
1. Upload the data to a central postgeSQL database.

## Installation Instructions
Copy the repository from the GitHub page
https://github.com/AdamBreeze1/multinational-retail-data-centralisation103.git

Then clone in your terminal using:
'git clone https://github.com/example_repository folder-name'

## Usage Instructions
The credentials for this demonstration are hidden to protect the sources, however, the below is how the project works.

1. Run all in "main.ipynb" 

## File Structure
- .gitignore
- database_utils.py
- data_extraction.py
- data_cleaning.py
- main.ipynb
- db_creds.yaml (not added to repository)
- store_header.py (not added to repository)
- Folder original_dfs
- Folder cleaned_dfs


## License information
