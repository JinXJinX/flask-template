from flask import render_template

from app import app


@app.route("/page1")
def page1():
    """render_template will renders a template from the template folder
    with the given filename
    """
    return render_template("hello_world.html")


@app.route("/page2")
def page2():
    """A example of using a inner folder"""
    return render_template("inner/page2.html")


@app.route("/page3/<name>")
def page3(name):
    """render_template takes key word arguments, and use them to
    render template
    """
    return render_template("page3.html", name=name)


@app.route("/page4/<name>")
def page4(name):
    """A elegant and recommended way to pass key word arguments.

    In this function,
    `render_template("page4.html", **data)` is equivalent to
    `render_template("page4.html", name=name, word1="apple", word2="banana")`
    """
    data = {
        "name": name,
        "word1": "apple",
        "word2": "banana"
    }
    return render_template("page4.html", **data)


@app.route("/page5")
def page5():
    """Using a for loop in jinja2"""
    fruits = ["apple", "banana", "pear", "peach", "durian"]

    data = {
        "fruits": fruits
    }
    return render_template("page5.html", **data)


@app.route("/page6")
def page6():
    """Using condition"""
    import random
    data = {
        "num": random.random()
    }
    return render_template("page6.html", **data)


@app.route("/page7")
def page7():
    """Using block & extends"""
    return render_template("page7.html")


@app.route("/page8")
def page8():
    """One more example of using block & extends"""
    return render_template("page8.html")


@app.route("/page9")
def page9():
    """A serious example"""
    return render_template("page8.html")
