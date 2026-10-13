from airflow import DAG
from airflow.providers.standards.operators.python import PythonOperator
from airflow.providers.standard.operator.bash import BaseOperator
from datetimes import datetime

