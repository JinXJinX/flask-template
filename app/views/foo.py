from flask import render_template, request, redirect
from app import app

from app.dblogic import blog as blog_db


@app.route("/")
def index():
    return "Hello World!"


@app.route("/blog_list")
def blog_list():
    blogs = list(blog_db.get_all_blog())
    print(blogs)
    data = {
        "blogs": blogs
    }
    return render_template("blog_list.html", **data)


@app.route("/blog_new")
def blog_new():
    args = request.args
    title = args.get("title")
    content = args.get("content")
    rst = blog_db.add_blog(title, content)
    return redirect("/blog_list")


@app.route("/blog_delete/<id>")
def blog_delete(id):
    raise NotImplementedError()
