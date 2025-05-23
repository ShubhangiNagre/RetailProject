import configparser
import os

from pyspark import SparkConf

# loading the application configs in python dictionary
def get_app_config(env):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_path = os.path.join(base_dir, "config", "application.conf")

    config = configparser.ConfigParser()

    if not config.read(config_path):
        raise FileNotFoundError(f"Could not read config file at: {config_path}")

    if not config.has_section(env):
        raise ValueError(f"No section [{env}] found in {config_path}")
    app_conf = {}
    for (key,val) in config.items(env):
        app_conf[key] = val
    return app_conf

# loading the pyspark configs and creating a spark conf object
import configparser
import os
from pyspark import SparkConf

def get_pyspark_config(env):
    # Get the base directory (project root)
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_path = os.path.join(base_dir, "config", "pyspark.conf")

    config = configparser.ConfigParser()

    if not config.read(config_path):
        raise FileNotFoundError(f"Could not read config file at: {config_path}")

    if not config.has_section(env):
        raise ValueError(f"No section [{env}] found in {config_path}")

    pyspark_conf = SparkConf()
    for key, val in config.items(env):
        pyspark_conf.set(key, val)

    return pyspark_conf
