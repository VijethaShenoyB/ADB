from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello():
   return "<h1>Hi</h1>"

@app.route('/page1')
def hello():
   return render_template("page1.html")

@app.route('/page2')
def hello():
   return render_template("page2.html")
 
if __name__ == '__main__':
  app.run()