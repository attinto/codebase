from __future__ import annotations
import os
import pendulum
from airflow.decorators import dag, task
from etl.package_details import package_details_etl as pkg

TZ = pendulum.timezone("UTC")
ENV = os.getenv("ENV", "dev")
SCHEDULE = "0 8 * * *" if ENV == "prod" else None

@dag(
    dag_id="my_dag_id",
    description="my description",
    start_date=pendulum.datetime(2025, 4, 1, tz=TZ),
    schedule=SCHEDULE,
    catchup=False,
    tags=["package"],
)
def package_details_dag():
    
    @task
    def process_pkg_flightbook():
        return pkg.pkg_flightbook()

    @task
    def process_pkg_hotelbook(res):
        return pkg.pkg_hotelbook(res)
    

    res_flightbook = process_pkg_flightbook()
    
    res_hotelbook = process_pkg_hotelbook(res_flightbook)


package_details_dag()

