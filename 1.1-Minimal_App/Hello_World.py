from flask import Flask

Aplication=Flask(__name__)

@Aplication.route("/")

def Hello_World():
    return "<p>Candela</p>"