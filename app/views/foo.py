from app import app


@app.route("/")
def index():
    return "Hello World!"


@app.route("/hello")
def hello():
    return "Hello!"


@app.route("/hello/<name>")
def hello2(name):
    """You can add variables to a URL by seround variable with angle
    brackets. Like this: <variable_name>. Your function then receives
    the <variable_name> as a keyword argument

    :param name: any string
    """
    return "Hello {}!".format(name)


@app.route("/greeting")
@app.route("/hola")
@app.route("/greeting/<name>")
def greeting(name=None):
    """You can use more than one decorator for a function

    :param name: None or any string
    """
    if name:
        return "Hi {}".format(name)
    return "Hi there"


@app.route("/bad_add/<a>/<b>")
def bad_add(a, b):
    """notice that variables' type is not integer

    :param a: str
    :param b: str
    """
    return a + b


@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    """Optionally, you can use a converter to specify the type of the
    argument like <converter:variable_name>. And you can create your
    own converter.

    If converter can't converte variable successfuly, Flask will return a
    '404 Not Found' page.

    More about builtin converter:
    http://flask.pocoo.org/docs/1.0/quickstart/#variable-rules

    :param a: an integer
    :param b: an integer
    """
    return str(a + b)
