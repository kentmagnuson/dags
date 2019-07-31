from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.models import Variable
from datetime import datetime, timedelta

ENV = Variable.get("env")

if ENV == "develop" or ENV == "feature":
    success_email = "TODO"
else:
    success_email = "TODO 2"

default_args = {
    'retires': 0,
    'start_date': datetime(2019, 8, 1),
    'depend_on_past': False,
}

dag_name = "feature/testing"
dag = DAG(
    dag_name, default_args=default_args, schedule_interval=timedelta(days=7))

task_1 = BashOperator(
    task_id='timestamp',
    bash_command='date',
    dag=dag)

task_2 = BashOperator(
    task_id='setup',
    bash_command='bash setup.sh',
    dag=dag)

task_3 = BashOperator(
    task_id='run',
    bash_command='bash workflow.sh',
    dag=dag)

task_2.set_upstream(task_1)
task_3.set_upstrean(task_2)

