from flask import render_template
from . import main


@main.route("/")
def index():
    return render_template("index.html");


@main.app_errorhandler(404)
def page404(e):
    return render_template("404.html"), 404


@main.app_errorhandler(500)
def page500(e):
    return render_template("500.html"), 500


@main.app_errorhandler(502)
def page502(e):
    return render_template("502.html"), 502
