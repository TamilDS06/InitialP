from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port='5001')

### Rendering templates Flask ###
# https://flask.palletsprojects.com/en/1.1.x/quickstart/#rendering-templates
