from flask import Flask, render_template, url_for
import requests

BLOG_URL = "https://api.npoint.io/540bbefa0484fb86e6f8"
app = Flask(__name__)


def all_blogs_():
    response = requests.get(url=BLOG_URL)
    all_blogs = response.json()
    return all_blogs


@app.route('/')
def home():
    all_blogs = all_blogs_()
    return render_template('index.html',  all_blogs=all_blogs)


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/post/<blog_num>')
def get_blog(blog_num):
    all_blogs = all_blogs_()
    for blog in all_blogs:
        if blog['id']==int(blog_num):
            return render_template('post.html', blog=blog)
        else:
            # return "<h1>Page not found.</h1>"
            continue
    

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)