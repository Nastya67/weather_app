from flask import render_template
from . import main


@main.errorhandler(404)
def page_not_found(er):
    return render_template("404.html", error=str(er)), 404


@main.errorhandler(500)
def server_error(er):
    return render_template("500.html", error=str(er)), 500


