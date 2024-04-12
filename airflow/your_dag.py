from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 4, 9),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'your_dag',
    default_args=default_args,
    description='A simple DAG to process CSV files with Kafka and Spark',
    schedule_interval='@hourly',
)

# Task to trigger Kafka producer
kafka_producer_task = BashOperator(
    task_id='trigger_kafka_producer',
    bash_command='python /app/kafka/producer.py',
    dag=dag,
)

# Task to trigger Spark job
spark_job_task = BashOperator(
    task_id='trigger_spark_job',
    bash_command='spark-submit /app/spark/spark_job.py',
    dag=dag,
)

# Define task dependencies
kafka_producer_task >> spark_job_task
