import configparser
import os

config = configparser.ConfigParser()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

config.read(os.path.join(BASE_DIR, "config.ini"))

DB_DRIVER = config["DATABASE"]["driver"]
DB_SERVER = config["DATABASE"]["server"]
DB_NAME = config["DATABASE"]["database"]
DB_USER = config["DATABASE"]["username"]
DB_PASS = config["DATABASE"]["password"]