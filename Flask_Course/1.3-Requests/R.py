from flask import Flask,request

app = Flask(__name__)

@app.route("/")
def hello():
    ip = request.remote_addr
    return f"Hello + {ip}" 

app.run("0.0.0.0",2888,debug=True)