from flask import Flask


app = Flask(__name__)
app.config.from_object("config")

from app.views import sample1_routing
from app.views import sample2_jinja2
