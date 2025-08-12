from flask import Flask,request,make_response,redirect

app = Flask(__name__)

@app.route("/index")

def index():
    ip = request.remote_addr
    response = make_response(redirect("/candela"))
    response.set_cookie("User_Ip_Information",ip)
    return response

@app.route("/candela")
def Show_Information_Address():
    user_ip = request.cookies.get("User_Ip_Information")
    return f"Hi ,your ip direction is {user_ip}"


app.run(host='0.0.0.0',port=2332,debug=True)
