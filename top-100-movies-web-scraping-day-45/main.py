import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(url=URL)
top_movies_web_page = response.text
soup = BeautifulSoup(top_movies_web_page, 'html.parser')
article_tags = soup.find_all(name='h3', class_='title')
article_Text_list = [article_tag.getText() for article_tag in article_tags][::-1]
with open('./Top_100_movies.txt', mode='w', encoding='utf8') as movies_file:
    for movie in article_Text_list:
        movies_file.write(f'{movie}\n')

