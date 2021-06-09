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


#Q3
#display image for given name
@app.route("/range", methods=['GET','POST'])
def displayrange():
    getrange1 = str(request.args.get('frange1'))
    getrange2 = str(request.args.get('frange2'))
    cursor.execute("select Name, Distance, Picture, Keywords from datab where Distance between "+getrange1 +" and "+ getrange2+" ;")
    getdetails = cursor.fetchall()
    return render_template('dispsalless.html', setdetails = getdetails)


#Q5Edit details enter the name:
@app.route("/editgetname", methods=['GET','POST'])
def editgetname():
     egetname = str(request.args.get('egetname'))
     cursor.execute("select * from datab where Name= '"+egetname+"';")
     edetails = cursor.fetchall()
     return render_template('editdetails.html', setdetails = edetails)


#Edit details for the given name:
@app.route("/editdetails", methods=['GET','POST'])
def editdetails():
    getauth = str(request.args.get('estate'))
    getename = str(request.args.get('ename'))

    cursor.execute("UPDATE datab SET Author = '"+getauth+"' WHERE Name='"+getename+"';")
    return render_template('index.html', message="Record has been updated")
   

#ADD or update image
@app.route("/uploadimg", methods=['GET','POST'])
def uploadimg():
     getimguser = str(request.args.get('imguser'))
     cursor.execute("select * from datab where Name= '"+getimguser+"';")
     iedetails = cursor.fetchall()
     return render_template('uploadimage.html', isetdetails = iedetails[0][4])


#Browse and submit the image
@app.route("/submitimage", methods=['POST'])
def submitimage():
     getmyfile = request.files["myfile"] #file path
     getimagename = getmyfile.filename   #file name
     getimgguy = request.form["imgguy"]  #inside the submit image page one more time name
     print(getimgguy)
     print(getmyfile)
     print(getimagename)
    
     getmyfile.save(os.path.join("/Users/amrutha/PROJECTS/Python/MyFlaskApp/static", getimagename))
     print("Image has been saved to static directory")
     cursor.execute("UPDATE datab SET Picture = '"+getimagename+"' WHERE Name='"+getimgguy+"';")
     return render_template('index.html', imessage="Image has been updated")
    

    









if __name__ == '__main__':
  app.run()