from flask import Flask, render_template
from random import randint
from datetime import datetime
import requests

year = datetime.now().year
agify_url = "https://agify.io"
genderize_url = "https://genderize.io"
app = Flask(__name__)


@app.route('/')
def home():
    random_number = randint(1, 10)
    year = datetime.now().year
    return render_template('index.html', number=random_number, year=year)


@app.route('/guess/<string:user_name>')
def guess_age_gender(user_name):
    try:
        gender_response = requests.get(url=f"{genderize_url}?name={user_name}")
        gender_data = gender_response.json()
        age_response = requests.get(url=f"{agify_url}?name={user_name}")
        age_data = age_response.json()
        return render_template('age_gender.html', year=year, name=user_name, gender=gender_data['gender'], age=age_data['age'])
    except:
        return "<h1>Invalid url</h1>"


@app.route('/blog')
def blog():
    fake_blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url=fake_blog_url)
    all_blogs_data = response.json()
    return render_template('blog.html', all_blogs=all_blogs_data)


if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1', debug=True)


### To update your footer of your webpage ###
# https://updateyourfooter.com/

### jinja documentation ###
# https://jinja.palletsprojects.com/en/2.11.x/templates/

### Rendering templates ###
# https://flask.palletsprojects.com/en/1.1.x/quickstart/#rendering-templates

### To create your own blogs ###
# https://www.npoint.io/