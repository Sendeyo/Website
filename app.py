from flask import Flask, render_template, request, url_for, redirect, session
import os
from passlib.hash import sha256_crypt
import data
from flask_mail import Mail, Message


app = Flask(__name__)
app.secret_key = os.urandom(24)

# configure server to send emails
app.config.update(
	DEBUG=True,
	#EMAIL SETTINGS
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME = 'anonymaxdashone@gmail.com',
	MAIL_PASSWORD = '17571757'
	)
mail = Mail(app)

@app.route("/send_mail")
def SendMail():
    try:
        msg = Message("Hey? This is a Test",
        sender = "anonymaxdashone@gmail.com",
        recipients = ["maxmuthomi@gmail.com"])
        msg.body = "Yo! This should be awesome"
        mail.send(msg)
        return "<html><h1>Hopefully that has been sent</h1></html>"
    except Exception as e:
        return e





@app.route("/home/<string:tile>", methods=["GET", "POST"])
def Tiles(tile):
    if tile == "Requests":
        return redirect("/kite")
    elif tile == "Errors":
        return redirect ("/errors")
    elif tile == "Raw":
        return redirect ("/raw")
    elif tile == "Send Email":
        return redirect ("/send_mail")
    else:
        return "{}".format(tile)


tiles = ["Send Email", "Errors", "Raw", "Requests"]


@app.route("/home")
def Home():
    return render_template("home.html", tiles=tiles)


@app.route("/kite")
def Kite():
    rows = data.DashData()
    return render_template("/kite/home.html", rows = rows)

@app.route("/errors")
def Errors():
    rows = data.ErrorResponses()
    return render_template("/kite/errors.html", rows = rows)

@app.route("/raw")
def Raw():
    rows = data.Responces()
    return render_template("/kite/raw.html", rows = rows)

@app.route("/")
def Login():
    return redirect("/home")


if __name__ == "__main__":
    app.run(debug=True)
