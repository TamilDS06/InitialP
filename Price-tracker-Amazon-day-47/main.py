import requests
from bs4 import BeautifulSoup
import smtplib


def send_mail(content_, to_mail):
    my_mail = "fortest@gmail.com"  # address to log in.
    password = "gtrgvvpzntyjsssu"  # app password.
    with smtplib.SMTP("smtp.gmail.com") as connection:  # email provider address.
        connection.starttls()
        connection.login(user=my_mail, password=password)
        connection.sendmail(
            from_addr=my_mail,
            to_addrs=to_mail,  # to address.
            msg=f"Subject:{content_}"  # Subject and body of the letter.
        )


Target_price = 100
URL = 'https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6'
HEADERS = {'sec-ch-ua-platform': "Windows", 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                                                          '(KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}
response = requests.get(url=URL, headers=HEADERS)
amazon_web_page = response.text
soup = BeautifulSoup(amazon_web_page, 'html.parser')
product = soup.find(name='span', class_='a-size-large product-title-word-break').getText().strip()
print(product)
Today_price = float((soup.find(name='span', class_='a-price-whole').getText().split('.')[0]))
if Today_price <= Target_price:
    content = f'The product {product} price is {Today_price} less than {Target_price}. Go and buy it.'
    to_mail = 'testdummy@gmail.com'
    send_mail(to_mail, content)
