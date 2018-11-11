from flask import Flask

# from config import FlaskInternalConfig

app = Flask(__name__)
app.config.from_object("app.etc.config.FlaskInternalConfig")

from app.views import foo
