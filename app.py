import os
from flask import Flask, render_template, request
import pandas as pd
import pyodbc


app = Flask(__name__)

server = 'shenoyserver.database.windows.net'
database = 'ShenoyDB'
username = 'vijethashenoy'
password = 'Vijushenoy96'
driver= '{ODBC Driver 17 for SQL Server}'


cnxn = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()


@app.route('/')
def hello():
   return "<h1>Hi</h1>"



   




if __name__ == '__main__':
  app.run()