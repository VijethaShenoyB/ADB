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


#display image for given name
@app.route("/", methods=['GET','POST'])
def display():
    getname = 'Mars'
    cursor.execute("select Picture from datab where Name = 'Mars';")
    getimage = cursor.fetchall()
    return render_template('index.html', setimage = "mars.jpg")

#Q2
#display image for given name
@app.route("/display", methods=['GET','POST'])
def displaymessage():
    
    cursor.execute("select Picture from datab where Picture is not null;")
    getimage = cursor.fetchall()
    return render_template('display.html', setimage = getimage)




   




if __name__ == '__main__':
  app.run()