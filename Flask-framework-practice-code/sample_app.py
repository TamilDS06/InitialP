from flask import Flask
import requests


app = Flask(__name__)

# API_KEY = 'sample-api-key-openweather'
API_KEY = 'bb700d38129771c8513ef021a9fe4347'

API_URL = ('http://api.openweathermap.org/data/2.5/weather?zip={},{}&mode=json&units=imperial&appid={}')


def query_api(zip, country_code):
    """submit the API query using variables for zip and API_KEY"""
    try:
        # print(API_URL.format(zip, API_KEY))
        data = requests.get(API_URL.format(zip, API_KEY, country_code)).json()
    except Exception as exc:
        print(exc)
        data = None
    return data


@app.route('/weather/<zip>/<country_code>')
def result(zip, country_code):
    # get the json file from the OpenWeather API
    resp = query_api(zip, country_code)
    # construct a string using the json data items for temp and
    # description
    try:
        text = resp["name"] + " temperature is " + str(resp["main"]["temp"]) + " degrees Fahrenheit with " + resp["weather"][0]["description"] + "."
    except:
        text = "There was an error.<br>Did you include a valid U.S. zip code in the URL?"
    return text

@app.route('/')
def hello():
    greet = '<h1>Hello, Gators!</h1>'
    link = '<p><a href="user/Albert">Click me!</a></p>'
    return greet + link

@app.route('/user/<name>')
def userr(name):
    personal = f'<h1>Hello, {name}!</h1>'
    # above - the curly braces {} hold a variable; when this runs,
    # the value will replace the braces and the variable name
    instruc = '<p>Change the name in the <em>browser address bar</em> \
        and reload the page.</p>'
    return personal + instruc


if __name__ == '__main__':
    app.run(host='127.0.0.1', port="5000", debug=True)
