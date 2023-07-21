from bs4 import BeautifulSoup
# import lxml
import requests

response = requests.get(url="https://news.ycombinator.com/news")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, 'html.parser')
articles = soup.find_all(name='a', rel='noreferrer')
article_Text = [article_tag.getText() for article_tag in articles]
article_Link = [article_tag.get('href') for article_tag in articles]
article_upvote = soup.find_all(name='span', class_='score')
article_upvote_score = [int(article_tag.getText().split(' ')[0]) for article_tag in article_upvote]
max_score_index = article_upvote_score.index(max(article_upvote_score))
print(article_Text[max_score_index])
print(article_Link[max_score_index])
print(article_upvote_score[max_score_index])
# with open('./website.html', mode='r', encoding="utf8") as file:
#     contents = file.read()
# soup = BeautifulSoup(contents, 'html.parser')
# # soup = BeautifulSoup(contents, 'lxml')
# # print(soup)
# # print(soup.prettify())
# # print(soup.title)
# # print(soup.title.name)
# # print(soup.title.string)
# # print(soup.p)
# # print(soup.a)
# # To find all the elements for example all paragraph tags or anchor tags
# all_anchor_tags = soup.find_all(name='a')
# print(all_anchor_tags)  # It gives the list of all anchor tags
#
# # To get the text and href of the all anchor tags
# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get('href'))
#
# # To find only one element using find() method using attributes(like h1, p, id, class)
# print(soup.find(name='h1', id='name'))
# heading = soup.find(name='h3', class_='heading')
# print(heading.name)
# print(heading.getText())
# print(heading.get('class'))
#
# # To select a particular tag using unique Identity as like css selector
# company_url = soup.select_one(selector='p a')
# print(company_url)
# name = soup.select_one(selector='#name')
# print(name)
# heading = soup.select_one(selector='.heading')
# print(heading)
