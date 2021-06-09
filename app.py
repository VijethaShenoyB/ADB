from flask import Flask, render_template, request
import pyodbc

app = Flask(__name__)

server = 'shenoyserver.database.windows.net'
database = 'ShenoyDB'
username = 'vijethashenoy'
password = 'Vijushenoy96'
driver= '{ODBC Driver 17 for SQL Server}'

cnxn = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()

#display image for given name
@app.route("/", methods=['GET','POST'])
def display():
    getname = 'Mars'
    cursor.execute("select Picture from datab where Name = 'Mars';")
    getimage = cursor.fetchall()
    return render_template('index.html', setimage = "mars.jpg")


@app.route('/')
def hello():
   return render_template("index.html")

@app.route('/page1')
def page1():
   return render_template("./page1.html")

@app.route('/page2')
def page2():
   return render_template("./page2.html")
 
if __name__ == '__main__':
  app.run()