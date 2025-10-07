from __future__ import annotations
import os
import pendulum
from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator
from etl.common_functions import get_json_files
from etl.flight_segments.flight_segments_etl import transform_segments_and_store_parquet

TZ = pendulum.timezone("UTC")

ENV = os.getenv("ENV", "dev")
SCHEDULE = "0 5 * * *" if ENV == "prod" else None

with DAG(
    dag_id="my_dag_id",
    description="my description",
    start_date=pendulum.datetime(2025, 4, 1, tz=TZ),
    schedule=SCHEDULE,
    catchup=False,
    tags=["tags"],
    params={
        "aws_region": "eu-south-2",
    },
) as dag:
    
    get_json_files_task = PythonOperator(
        task_id="get_json_files_task",
        python_callable=get_json_files,
        op_args=[
            "{{ data_interval_start }}", 
            "{{ params.source_s3_path }}"
        ],
    )

    clean_json_and_store_parquet_task = PythonOperator(
        task_id="transform_segments_and_store_parquet",
        python_callable=transform_segments_and_store_parquet,
    )
        
    get_json_files_task >> clean_json_and_store_parquet_task
