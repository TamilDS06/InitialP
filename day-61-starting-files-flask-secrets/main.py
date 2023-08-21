from flask import Flask, render_template, request
from forms import MyLoginForm
from flask_bootstrap import Bootstrap4

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''
# Flask-WTF doc: https://flask-wtf.readthedocs.io/en/1.0.x/quickstart/#validating-forms
# Differnent fields in Flask-WTF: https://wtforms.readthedocs.io/en/3.0.x/fields/#basic-fields


app = Flask(__name__)
app.secret_key = "Secret1234"
bootstrap = Bootstrap4(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = MyLoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=login_form)


@app.route("/success", methods=['POST'])
def success():
    return f"<h1>Your email is {request.form['email']}, password is {request.form['password']}."


if __name__ == '__main__':
    app.run(debug=True)
