
"""
GeneratedTest1 by airflow console
fileName:  test/test_2_test_dag_ylm.py
date    :  2021-07-22 16:44:37
"""


from airflow import DAG
from datetime import datetime
from dag_utils import compass_utils

def on_failure():
    fail_dingding_conn_id='dingding'
    fail_receivers=''
    failure='dingding'
    if failure:
      if failure.find('dingding')==-1:
        fail_dingding_conn_id=None
      if failure.find('email')==-1:
        fail_receivers=None

      return compass_utils.failure_callback(dingding_conn_id=fail_dingding_conn_id, receivers=fail_receivers)
    return None

def on_success():
    succ_dingding_conn_id='dingding'
    succ_receivers=''
    success='dingding'
    if success:
      if success.find('dingding')==-1:
        succ_dingding_conn_id=None
      if success.find('email')==-1:
        succ_receivers=None
      return compass_utils.success_callback(dingding_conn_id=succ_dingding_conn_id, receivers=succ_receivers)
    return None

default_args = {
    'owner': 'test_dag_test',
    'depends_on_past': False,
    'on_failure_callback': on_failure(),
    'on_success_callback': on_success(),
    'start_date': datetime(2021,7,21),
    'retries': 2
}

dag = DAG(
    'test_2_test_dag_ylm',
    description='test',
    default_args=default_args,
    schedule_interval="0 3 * * *")


from airflow.operators.http_operator import SimpleHttpOperator
import json




ylm_task_http_dingding = SimpleHttpOperator(
    task_id='ylm_task_http_dingding',
    http_conn_id='dingding',
    method='GET',
    endpoint='api/v1/conns/',
    
    
    
    dag=dag
)


ylm_task_http_dingding.doc = """
    undefined
"""


ylm_task_http_dingding