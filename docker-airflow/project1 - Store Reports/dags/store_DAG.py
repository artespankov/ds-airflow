from datetime import datetime, timedelta
from airflow import DAG, BashOperator


default_args = {
    "owner": "AirFlow",
    "start_date": datetime(2024, 3, 8),
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG('store_dag', default_args, schedule_interval='@daily', catchup=False)

# 1. Check if file is present in input folder
t1 = BashOperator(task_id='check_file_exists', bash_command='shasum ~/store_files/raw_store_transactions.csv')