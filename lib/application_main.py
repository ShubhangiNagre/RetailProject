import configparser
import os
import sys
from lib import Utils,DataReader,DataManipulation
from pyspark.sql.functions import *
from lib.logger import log4j

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print("please specify the environment")
        sys.exit(-1)
    else:
        print(f"Executing on {sys.argv[-1]}")

    job_run_env = sys.argv[-1]

    print("Creating Spark Session")
    spark = Utils.get_spark_session(job_run_env)

    logger = log4j(spark)

    logger.warn("Created Spark Session")# loading the pyspark configs and creating a spark conf object

    orders_df = DataReader.read_orders(spark, job_run_env)

    orders_filtered = DataManipulation.filter_closed_orders(orders_df)

    customers_df = DataReader.read_customers(spark,job_run_env)

    joined_df = DataManipulation.join_orders_customers(orders_filtered,customers_df)

    aggregated_results = DataManipulation.count_order_state(joined_df)

    aggregated_results.show()

    logger.info("this is the end of main")