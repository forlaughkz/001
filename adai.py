from datetime import datetime

from airflow import DAG

from airflow.operators.python_operator import PythonOperator


def print_time():

    print('ATTENTION!!!!!!----------------------- Airflow_Time: ',

        datetime.now(),'Thank you for Attention!')


dag = DAG('adai_time_major_dag_v2', description='A simple time DAG',

          schedule_interval=None,

          start_date=datetime(2024, 5, 10), catchup=False)


time_operator = PythonOperator(task_id='time_task', python_callable=print_time, dag=dag)
