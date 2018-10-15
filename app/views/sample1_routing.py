from app import app


@app.route("/")
def index():
    """
    Example:
        Open 127.0.0.1:3333 in browser. It will show "Hello World!"
    """
    return "Hello World!"


@app.route("/hello")
def hello():
    """You can customize URI (Uniform Resource Identifier)

    Example:
        Open 127.0.0.1:3333/hello in browser. It will show "Hello!"
    """
    return "Hello!"


@app.route("/hello/<name>")
def hello2(name):
    """You can add variables to a URL by seround variable with angle
    brackets. Like this: <variable_name>. Your function then receives
    the <variable_name> as a keyword argument

    Args:
        name (str): any string

    Example:
        Open 127.0.0.1:3333/hello/alan in browser. It will show "Hello alan!"
    """
    return "Hello {}!".format(name)


@app.route("/greeting")
@app.route("/hola")
@app.route("/hallo")
def hello3():
    """You can use multiple decorators for one function

    Example:
        Try 127.0.0.1:3333/greeting
            127.0.0.1:3333/hola
            127.0.0.1:3333/hallo
        There all will return "Hello 3!"
    """
    return "Hello 3!"


@app.route("/hello4")
@app.route("/hello4/<name>")
def hello4(name=None):
    """Input variables can has a default value

    Args:
        name (str, optional): any string, default is None

    Example:
        127.0.0.1:3333/hello4 will return "Hello there!"
        127.0.0.1:3333/hello4/cindy will return "Hello cindy!"
    """
    if name:
        return "Hello {}!".format(name)
    return "Hello there!"


@app.route("/bad_add/<a>/<b>")
def bad_add(a, b):
    """notice that variables' type is not integer

    Args:
        a (str): string variable
        b (str): string variable

    Returns:
        str: concatenate a and b

    Example:
        127.0.0.1:3333/bad_add/1/2 will return "12"
        127.0.0.1:3333/bad_add/aa/bb will return "aabb"
    """
    return a + b


@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    """Optionally, you can use a converter to specify the type of the
    argument like <converter:variable_name>. And you can create your
    own converter.

    If converter can't converte variable successfuly, Flask will return a
    "404 Not Found" page.

    More about builtin converter:
    http://flask.pocoo.org/docs/1.0/quickstart/#variable-rules

    Args:
        a (int): integer variable
        b (int): integer variable

    Returns:
        str: sum of a and b in string format

    Example:
        127.0.0.1:3333/add/1/2 will return "3"
        127.0.0.1:3333/add/x/y will return "Not Found"
    """
    return str(a + b)
