from flask import Flask,request,make_response,redirect,render_template

app = Flask(__name__)

@app.route("/index")
def index():
    ip = request.remote_addr
    response = make_response(redirect("/candela"))
    response.set_cookie("Candelita",ip)
    return response

@app.route("/candela")
def candela():
    user_ip = request.cookies.get("Candelita")
    return render_template("ip.html",user_ip=user_ip)

app.run(host='0.0.0.0',port='3360',debug=True)