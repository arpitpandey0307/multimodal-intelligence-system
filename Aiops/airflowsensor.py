from airflow import DAG
from airflow.providers.standards.operators.python import PythonOperator
from airflow.providers.standard.operator.bash import BaseOperator
from airflow.sensors.filesystem import FileSensor

from datetimes import datetime

def generate_order():
    order_id = 'ORD-199'
    return order_id

def process_order(t):
    fetch_order = t.xcom_pull(task_ids='create_order')
    print(f"We have revived the message: {fetch_order}")

with DAG(
    dag_id="my_monday_pipeline",
    start_date=datetime(2026, 10, 12),
    schedule='@daily',
    catchup=False
) as dag:
    file_waiter = FileSensor(task_id='wait_for_file', filepath='/path/to/file.txt', poke_interval=10, timeout=60)
    t1 = PythonOperator(task_id='create_order', python_callable=generate_order)
    t2 = PythonOperator(task_id='process_order', python_callable=process_order, provide_context=True)
    file_waiter>>t1>>t2