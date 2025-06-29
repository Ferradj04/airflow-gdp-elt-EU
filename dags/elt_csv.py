from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import sqlalchemy

default_args = {'start_date': datetime(2025, 6, 1)}

def extract():
    df = pd.read_csv('../data/data_eu_gdp.csv')
    df.to_csv('/opt/airflow/data/data_eu_gdp_tmp.csv', index=False)

def load():
    df = pd.read_csv('/opt/airflow/data/data_eu_gdp_tmp.csv')
    engine = sqlalchemy.create_engine('sqlite:////opt/airflow/data/db.sqlite3')
    df.to_sql('EU_GDP_2024', engine, if_exists='replace', index=False)

def transform():
    engine = sqlalchemy.create_engine('sqlite:////opt/airflow/data/db.sqlite3')
    df = pd.read_sql('SELECT * FROM EU_GDP_2024 ORDER BY GDP_mi_eu_2024 DESC', engine)
    df['state_name'] = df['state_name'].str.upper()
    df.to_sql('sorted_data', engine, if_exists='replace', index=False)

with DAG('elt_csv_pipeline', default_args=default_args, schedule_interval='@daily', catchup=False) as dag:
    t1 = PythonOperator(task_id='extract_csv', python_callable=extract)
    t2 = PythonOperator(task_id='load_to_db', python_callable=load)
    t3 = PythonOperator(task_id='transform_data', python_callable=transform)
    t1 >> t2 >> t3
