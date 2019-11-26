from flask import Flask, render_template, request, url_for, redirect, session
import os
from passlib.hash import sha256_crypt
import data

app = Flask(__name__)
app.secret_key = os.urandom(24)


app.config.update(
    DEBUG=True,
)





@app.route("/home/<string:tile>", methods=["GET", "POST"])
def Tiles(tile):
    if tile == "Requests":
        return redirect("/kite")
    elif tile == "Responces":
        return redirect ("/responces")
    elif tile == "Raw":
        return redirect ("/raw")
    else:
        return "{}".format(tile)


tiles = ["Responces", "Raw", "Requests"]


@app.route("/home")
def Home():
    return render_template("home.html", tiles=tiles)


@app.route("/kite")
def Kite():
    rows = data.DashData()
    return render_template("/kite/home.html", rows = rows)

@app.route("/responces")
def Responces():
    rows = data.Responces()
    return render_template("/kite/responces.html", rows = rows)

@app.route("/raw")
def Raw():
    rows = data.Responces()
    return render_template("/kite/raw.html", rows = rows)

@app.route("/")
def Login():
    return redirect("/home")


if __name__ == "__main__":
    app.run(debug=True)
