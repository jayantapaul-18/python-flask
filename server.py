import os
import time
from datetime import datetime
from flask import Flask,render_template, make_response ,request , redirect, jsonify
from flask import make_response
import requests
from threading import Timer
from os import path,remove
import datetime
import sys
import json
from flask_cors import CORS
import logging
import logging.config
import logging.handlers
import unittest

app = Flask(__name__)
cors = CORS(app, resources={r"/app/*": {"origins": "*"}})
#print(os.getenv(key, default=None))

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
print("BASE_DIR :  "+ BASE_DIR)
#print(LOGGING_CONF)
# If applicable, delete the existing log file to generate a fresh log file during each execution
if path.isfile("python_logging.log"):
    remove("python_logging.log")
with open('logging.json', 'r') as logging_configuration_file:
 config_dict = json.load(logging_configuration_file)

# create logger
#logger = logging.getLogger('simpleExample')
logger = logging.getLogger(__name__)
#logging.config.fileConfig(config_dict)
logging.basicConfig(filename='app.log',datefmt='%d-%b-%y %H:%M:%S', filemode='w',format='%(name)s - %(levelname)s - %(message)s')
logger.setLevel(logging.DEBUG)
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
# Creating the security route
@app.route('/')
def sectes():
    print('Start Security Scan check...')
    logger.error('Start Security Scan check')
    logger.debug('Start Security Scan check')
    return 'Security Scan Compleated'

# Creating the route for ping
@app.route('/ping')
def hi():
    print('OK')
    return 'OK !'

@app.route('/app/healthcheck')
def healthcheck():
    a = {"name":"John", 
   "age":31,
   "message": "'Response send from server'", 
   "Salary":180000}
    print(json.dumps(a))
    return json.dumps(a)

@app.route('/app/flow/A')
def flowA():
    a = {"name":"A", 
   "id":1,
   "message": "'Response send from server A'", 
   "url":'/app/flow/A'}
    print(json.dumps(a))
    return json.dumps(a)

@app.route('/app/flow/B')
def flowB():
    b = {"name":"B", 
   "id":2,
   "message": "'Response send from server B'", 
   "url":'/app/flow/B'}
    print(json.dumps(b))
    return json.dumps(b)


@app.route('/app/array')
def arraytest():
    b = ['jay',18,'hello']
    return json.dumps(b)

@app.route('/app/json')
def jsontest():
    c = {
        "first":"test",
        "last":"test",
        "email":"test@yopmail.com",
        "contact":"email",
        "Hobby":"electronics"
    }
    return json.dumps(c)
@app.route('/app/string')
def stringtest():
    d = 'Hello string test'
    return d

@app.route('/app/count',methods = ['POST', 'GET','OPTIONS'])
def counttest():
    e = 'Hello counting test'
    return e

@app.route('/')
def index():
    return 'ACK from Python Server'
print('Python Server Started ...')

def chat(message):
    p = print
    p(message)
    return message
chat('me')

#print(os.environ)
# Connect with DB
# http://dummy.restapiexample.com/

@app.route('/app/connect')
def cf_connect():
    #query = request.args.get('query')
    api_url = 'http://dummy.restapiexample.com/api/v1/employees'
    #head = {'Authorization': 'Bearer YOUR_ACCESS_TOKEN'}
    #s = requests.Session()
    result = requests.get(api_url)
    # + query , headers=head)
    result = result.json()
    print(result)
    #result = result.get('result')
   # fulfil = result.get('fulfillment')
    # data= fulfil.get('data')
    # if data is None:
    #     speech= fulfil.get('speech')
    #     fb={"text": speech}
    # else:    
    #     fb = data.get('facebook')
    # element=[]
    # element.append(fb)
    # res = json.dumps(element, indent=4)
    # r = make_response(res)
    #r.headers['Content-Type'] = 'application/json'
    return result.json()

 
@app.route('/app/employee', methods=['GET'])
def home():
    r = requests.get('http://dummy.restapiexample.com/api/v1/employees')
    print(r)
    return r.json()

# SQLite DB --------------------------------------------------------------------
import sqlite3

conn = sqlite3.connect('example.db')
db_c = conn.cursor()


def commit_close_db():
             conn.commit()
             conn.close()
             return True
# Create table
try:
  db_c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')
  commit_close_db()
except sqlite3.OperationalError: 
     logger.error('Create Table error , Table already exists ')

# Insert a row of data
# now = datetime.datetime.now()
# try:
#   db_c.execute("INSERT INTO stocks VALUES (now.isoformat(),'BUY','RHAT',100,35.14)")
#   commit_close_db()
# except sqlite3.OperationalError:
#     logger.error('Database is lockd')
# # Save (commit) the changes
# conn.commit()
# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
#conn.close()
# Do this instead
t = ('RHAT',)
db_c.execute('SELECT * FROM stocks WHERE symbol=?', t)
logger.info(db_c.fetchone())


# Larger example that inserts many records at a time
# purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
#              ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
#              ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
#             ]
# db_c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)
now = datetime.datetime.now()
@app.route('/app/data/insert', methods=['GET'])
def insert():
    conn = sqlite3.connect('example.db')
    db_c = conn.cursor()
    
    try:
      db_c.execute("INSERT INTO stocks VALUES ('2019','BUY','RHAT',100,35.14)")
      logger.debug('Insert into DB Success ..')
      commit_close_db()
      return ('Success',db_c.fetchone())
    except sqlite3.OperationalError:
        logger.error('Database is lockd')
    return ('Error !',db_c.fetchone())

@app.route('/app/data/delete', methods=['GET'])
def delete():
    conn = sqlite3.connect('example.db')
    db_c = conn.cursor()
    p = ('RHAT',)
    db_c.execute('DELETE FROM stocks WHERE symbol=?', p)
    logger.debug('Delete success .. ')
    return ('Success')

# End of SQLite DB ------------------------------------------------------------------
# Array 
AR = [99,76,26,1,8,2,6,7,4,49,37,15,6,2,15,6,8,412,66555]
print(list(AR)) , print(len(AR))
# print(AR[-1]) , print (AR.append(15)) , print(AR)
# print(AR.extend('Hi')) , print(AR)
# print(AR.append('Hi')) , print(AR)
# print(AR.remove(15)) , print(AR)
# print(AR.pop()) , print(AR)
# ----------------------------------------------------- 
#Binary Search 
def binary_Search(arr,L,R,x):
    if R >= L:
       mid = L+(R-L)/2
       if arr[mid] == x:
           return mid
       elif arr[mid] > x:
           return binary_Search(arr,mid-1,R,x)
       else:
            return binary_Search(arr,mid+1,R,x)
    else:
        return -1

# Test binary Search array
arr = [0,2,3,4,10,40]
x = 10 
# Function call
# Rl = len(arr)-1
# result = binary_Search(arr,0,Rl,x)
# if result != -1:
#     print('Element is present at index %d' % result)
# else:
#     print('Element is not present in array')
# -----------------------------------------------------    
# TypeError: list indices must be integers or slices, not float
# https://github.com/donnemartin/system-design-primer
# Server Run # https://github.com/humiaozuzu/awesome-flask
if __name__ == "__main__":
	print('Server Started on port:',PORT ,'~', 'Debug Enable: ',ENABLE_DEBUGGER,'~', 'USE_RELOADER: ',USE_RELOADER,'http://127.0.0.1:5000')
    #print('Server Started on port:',PORT ,'~', 'Debug Enable: ',ENABLE_DEBUGGER,'~', 'USE_RELOADER: ',USE_RELOADER,'http://127.0.0.1:5000')
	app.run(port=5000,debug=True,use_reloader=True)
# -----------------------------------------------------UP----------------------------------------------------------

