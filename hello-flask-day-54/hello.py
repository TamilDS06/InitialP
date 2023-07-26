from flask import Flask # https://flask.palletsprojects.com/en/2.3.x/quickstart/


def make_bold(fun):
    def wrapper():
        return f"<b> {fun()} </b>"
    return wrapper

def make_empathesis(fun):
    def wrapper():
        return f"<em> {fun()} </em>"
    return wrapper

def make_underline(fun):
    def wrapper():
        return f"<u> {fun()} </u>"
    return wrapper

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/bye")
@make_underline
@make_bold
@make_empathesis
def say_bye():
    return "Bye"


@app.route("/<path:name>") # valiable rules
def user_(name):
    return f"Welcome {name} to hello flask "


@app.route("/username/<name>/<int:number>") # valiable rules
def user(name, number):
    return f"Welcome {name} to hello flask {number}"


# Here the __name__ is special attribute and it is one of the python built in attribute
if __name__ == '__main__': # https://docs.python.org/3/library/stdtypes.html?highlight=__name__#special-attributes
    # Run the app debug mode to auto-reload
    app.run(debug=True)

### command line windows###
# https://www.cs.columbia.edu/~sedwards/classes/2015/1102-fall/Command%20Prompt%20Cheatsheet.pdf
### command line mac/linux###
# https://github.com/appbrewery/terminal-mac-cheatsheet

### python flask variable-rules doc ###
# https://flask.palletsprojects.com/en/1.1.x/quickstart/#variable-rules

### python flask routing doc ###
# https://flask.palletsprojects.com/en/1.1.x/quickstart/#routing