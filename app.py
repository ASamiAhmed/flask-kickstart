from flask import Flask,render_template
from os import path   # for creating path
from os import path, environ   # for creating path

app = Flask(__name__)

@app.route('/')
def index():
    fruits=['Mango','Apple','Banana']
    return render_template("index.html",fruits=fruits)

@app.route('/about')
def about():
    return render_template("about.html")

PORT = int(environ.get("PORT") or 5000)
if __name__=="__main__":
    # app.run(debug=True)  
    app.run(host='0.0.0.0', port=PORT)  
