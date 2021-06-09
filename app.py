from flask import Flask, render_template, request
import csv


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
   return render_template("index.html")

@app.route('/data', methods=['GET', 'POST'])
def data():
   if request.method == 'POST':
      f = request.form['csvfile']
      data = []
      with open(f) as file:
         csvfile = csv.reader(file)
         for row in csvfile:
            data.append(row)  
      return render_template('data.html', data=data)


@app.route('/page1')
def page1():
   return render_template("./page1.html")

@app.route('/page2')
def page2():
   return render_template("./page2.html")
 
if __name__ == '__main__':
  app.run()