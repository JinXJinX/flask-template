from flask import render_template

from app import app


@app.route("/d1")
def d1():
    """Undefined Error
    Raised if a template tries to operate on Undefined.
    """
    return render_template("jinja_debug/d1.html")


@app.route("/d2")
def d2():
    """Template Not Found
    Raised if a template does not exist.
    """
    return render_template("jinja_debug/not_exist.html")


@app.route("/d3")
def d3():
    """Template Syntax Error
    Raised to tell the user that there is a problem with the template's syntax.
    """
    return render_template("jinja_debug/d3.html")


@app.route("/d4")
def d4():
    """Use jinja comment systax
    """
    return render_template("jinja_debug/d4.html")


@app.route("/d5")
def d5():
    """Python runtime error"""
    None > 1
    return "d5"
