import requests

class Post:


    def __init__(self, fake_blog_url):
        self.url = fake_blog_url

    
    def get_blog(self):
        response = requests.get(url=self.url)
        all_blogs = response.json()
        return all_blogs

