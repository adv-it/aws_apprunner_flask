from flask import Flask, render_template
import os

application = Flask(__name__)


@application.route("/")
def root():
    return render_template("index.html")

@application.route("/help")
def helppage():
    return render_template("help.html")

@application.route("/hello")
def hellopage():
    NAME_F = os.getenv('NAME_FIRST', "Stupido") # Read Environment Variable
    NAME_L = os.getenv('NAME_LAST',  "Usero")   # Read Environment Variable
    HELLO_MESSAGE = "Hello to: <b>" + NAME_F + " " + NAME_L + "</b> :)"
    return HELLO_MESSAGE

#--------Main------------------
if __name__ == "__main__":
    application.run(host="0.0.0.0", port=8080)
#------------------------------
