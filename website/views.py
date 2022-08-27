from flask import Blueprint, render_template

views = Blueprint("views",  __name__)

@views.route("/")
def index():
    return render_template("index.html")

@views.route("/vita")
def vita():
    return render_template("base.html")

@views.route("/galerie")
def galery():
    return render_template("galery.html", images=[1, 2, 3, 4])