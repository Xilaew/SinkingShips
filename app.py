from flask import Flask, requests

app = Flask(__name__,static_folder="static")


@app.route('/')
def hello():
    return 'blah World!'

@app.route("/schiessen",methods = ['POST'])
def shiessen():
    print (requests.form["key"])
    return ""
