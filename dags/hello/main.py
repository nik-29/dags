from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
import time
import mysql.connector
def print_hello():
 #time.sleep(300)
 mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="root"
)
 print(mydb)
 return mydb

dag = DAG('hello_world', description='Hello world example', schedule_interval='0 12 * * *', start_date=datetime(2017, 3, 20), catchup=False)

dummy_operator = DummyOperator(task_id='dummy_task', retries = 3, dag=dag)

hello_operator = PythonOperator(task_id='hello_task', python_callable=print_hello, dag=dag)

dummy_operator >> hello_operator
