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
    """A example of using a inner folder. This template is located in
    flask_template/app/templates/inner/
    """
    return render_template("inner/page2.html")


@app.route("/page3/<name>")
def page3(name):
    """function `render_template` takes keyword arguments. Those
    variables are available when rendering template
    """
    return render_template("page3.html", name=name)


@app.route("/page4/<name>")
def page4(name):
    """A elegant and recommended way to pass keyword arguments to
    `render_template`.

    In this example,
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
    """Loop

    References:
        http://jinja.pocoo.org/docs/2.10/templates/#for
    """
    fruits = ["apple", "banana", "pear", "peach", "durian"]

    data = {
        "fruits": fruits
    }
    return render_template("page5.html", **data)


@app.route("/page6")
def page6():
    """If Statements

    References:
        http://jinja.pocoo.org/docs/2.10/templates/#if
    """
    import random
    data = {
        "num": random.random()
    }
    return render_template("page6.html", **data)


@app.route("/page7")
def page7():
    """Template Inheritance

    References:
        http://jinja.pocoo.org/docs/2.10/templates/#template-inheritance
    """
    return render_template("page7.html")


@app.route("/page8")
def page8():
    """Template Inheritance. One more example"""
    return render_template("page8.html")


@app.route("/page9")
def page9():
    """A serious example"""
    data = {
        "title": "a title",
        "name": "The Zen of Python",
        "aphorisms": [
            "Beautiful is better than ugly.",
            "Explicit is better than implicit.",
            "Simple is better than complex.",
            "..."
        ]
    }
    return render_template("serious_temp/index.html", **data)
