from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

def print_hello():
    return 'Hello world from first Airflow DAG!'

def print_hello2():
    return 'rajeev - Hello world from first Airflow DAG! -- rajeev'


dag = DAG('hello_world', description='Hello World DAG',
          schedule_interval='0 15 * * *',
          start_date=datetime(2022, 10, 8), catchup=False) ## YYYY,MM,DD

hello_operator = PythonOperator(task_id='hello_task', python_callable=print_hello, dag=dag)

hello2_operator = PythonOperator(task_id='hello2_task', python_callable=print_hello2, dag=dag)

hello_operator >> hello2_operator