from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/login', methods=['POST'])
def login_():
    name = request.form['name']
    password = request.form['pwd']
    return render_template('login.html', name=name, pwd=password)

    
if __name__ == "__main__":
    app.run(port=5000, host="127.0.0.1", debug=True)
    