import os

from pyspark.sql import SparkSession
from lib.ConfigReader import get_pyspark_config


def get_spark_session(env):
    log4j_path = os.path.abspath("log4j.properties").replace("\\", "/").replace("lib/", "")
    print("Using log4j path:", log4j_path)
    if env == "LOCAL":
        return (
            SparkSession.builder
            .config(conf=get_pyspark_config(env))
            .config('spark.driver.extraJavaOptions', f'-Dlog4j.configuration=file:{log4j_path}')
            .master("local[2]")
            .getOrCreate()
        )

    else:
        return SparkSession.builder \
        .config(conf = get_pyspark_config(env)) \
        .enableHiveSupport() \
        .getOrCreate()