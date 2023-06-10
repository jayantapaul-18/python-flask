import os
import time
from datetime import datetime
from flask import Flask, render_template, make_response, request, redirect, jsonify
from threading import Timer
from os import path, remove
import datetime
import sys
import json
import logging
import logging.config
import logging.handlers
import requests

app = Flask(__name__)

USE_RELOADER = True
TIMEOUT = 60
ENABLE_DEBUGGER = True
PLATFORM_LIST = ("darwin", "win32", "cygwin")
if sys.platform in PLATFORM_LIST:
    ENABLE_PI = False
    PORT = 5000

LOGGING_CONF = os.path.dirname(os.path.realpath(__file__)) + "/logging.json"
LOG_FILE = os.path.dirname(os.path.realpath(__file__)) + "/error.log"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print("BASE_DIR :  " + BASE_DIR)
# print(LOGGING_CONF)
# If applicable, delete the existing log file to generate a fresh log file during each execution
if path.isfile("python_logging.log"):
    remove("python_logging.log")
with open("logging.json", "r") as logging_configuration_file:
    config_dict = json.load(logging_configuration_file)

# create logger
# logger = logging.getLogger('simpleExample')
logger = logging.getLogger(__name__)
# logging.config.fileConfig(config_dict)
logging.basicConfig(
    filename="app.log",
    datefmt="%d-%b-%y %H:%M:%S",
    filemode="w",
    format="%(name)s - %(levelname)s - %(message)s",
)
logger.setLevel(logging.DEBUG)
logger.debug("debug message")
logger.info("info message")
logger.warning("warn message")
logger.error("error message")
logger.critical("critical message")
# Creating the security route


@app.route("/api-request")
def sectes():
    api_url = "https://jsonplaceholder.typicode.com/todos/1"
    response = requests.get(api_url)
    logger.debug("making api request")
    return response.json()


# Creating the route for ping


@app.route("/ping")
def hi():
    print("OK")
    return "OK !"


@app.route("/app/healthcheck")
def healthcheck():
    return {"Status": "Server Up & running"}


@app.route("/")
def index():
    return "ACK from Python Server"


# Creating Web App
@app.route("/home")
def home():
    return render_template("index.html")




def calculate_auto_future_date(expiration_date):
  """
  Calculates the auto future date for token rotation.

  Args:
    expiration_date (datetime): The expiration date of the token.

  Returns:
    datetime: The auto future date.
  """
  # Get the current date.
  current_date = datetime.datetime.now()
  # Calculate the future date.
  future_date = expiration_date - datetime.timedelta(days=1)
  # Check if the future date is before the current date.
  if future_date < current_date:
    # If the future date is before the current date, then set it to the next month.
    future_date = current_date + datetime.timedelta(days=30)
    
  return future_date

expiration_date = datetime.datetime(2023, 6, 10)
future_date = calculate_auto_future_date(expiration_date)
print(future_date)

print("Python Server Started ...")

# Server Run
if __name__ == "__main__":
    print(
        "Server Started on port:",
        "~",
        "Debug Enable: ",
        ENABLE_DEBUGGER,
        "~",
        "USE_RELOADER: ",
        USE_RELOADER,
    )
    app.run(port=5000, debug=True, use_reloader=True)
# -----------------------------------------------------UP----------------------------------------------------------
