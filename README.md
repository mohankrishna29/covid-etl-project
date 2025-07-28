# 🦠 COVID-19 Data ETL Project

This project is a simple **ETL (Extract, Transform, Load)** pipeline that fetches COVID-19 data from a public API and loads it into a PostgreSQL database for further analysis.

---

##  Project Overview

- **Extract**: Fetches global COVID-19 statistics from the `disease.sh` API
- **Transform**: Selects and formats relevant data (e.g. country name, cases, deaths, etc.)
- **Load**: Inserts the transformed data into a PostgreSQL table (`covid_stats`)

Built using **Python**, with libraries like `requests`, `psycopg2`, and `pandas`.

---

## 📁 Project Structure

covid-data-etl/
├── etl.py # Main ETL pipeline script
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── .gitignore # Git exclusions

## Steps Followed
Created a new Python project folder
Wrote an ETL script (etl.py) to:
Call the API
Process the response
Insert it into a PostgreSQL table
Set up PostgreSQL locally, created a new database and table
Ran the script and verified that data is correctly inserted into the database
Created a GitHub repository and pushed all files using Git
