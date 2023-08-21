from flask import Flask, render_template
from post import Post

def all_blogs_():
    fake_blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    post_ = Post(fake_blog_url=fake_blog_url)
    all_blogs = post_.get_blog()
    return all_blogs

app = Flask(__name__)


@app.route('/')
def home():
    all_blogs = all_blogs_()
    return render_template("index.html", all_blogs=all_blogs)


@app.route('/post/<num>')
def get_blog_(num):
    all_blogs = all_blogs_()
    for blog in all_blogs:
        if blog['id'] == int(num):
            return render_template("post.html", Title=blog['title'], Body=blog['body'])


if __name__ == "__main__":
    app.run(debug=True)
