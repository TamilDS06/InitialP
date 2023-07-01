# import smtplib
#
# my_mail = "fortest@gmail.com"  # address to login.
# password = "gtrgvvpzntyjsssu"  # app password.
# with smtplib.SMTP("smtp.gmail.com") as connection:  # email provider address.
#     connection.starttls()
#     connection.login(user=my_mail, password=password)
#     connection.sendmail(
#         from_addr=my_mail,
#         to_addrs="fortestinfo@gmail.com",  # to address.
#         msg="Subject:Hello\n\nThis is my body of the letter."  # Subject and body of the letter.
#     )


# from datetime import datetime
# # Basics
# date = datetime.now()
# print(date)
# year = date.year
# month = date.month
# day = date.day
# print(f"{year}\n{month}\n{day}")
# date = date.strftime("%H-%M-%S")
# print(f'custom_date :{date}')
# custom_date = datetime(year=1996, month=9, day=15, hour=11)
# print(f'custom_date :{custom_date}')

# from datetime import datetime
# import smtplib
# from random import choice
#
# my_mail = "fortest@gmail.com"  # address to log in.
# password = "gtrgvvpzntyjsssu"  # app password.
#
# current_date = datetime.now()
# day = current_date.day
#
# if day == 0:
#
#     with open("quotes.txt") as quotes:  # https://www.positivityblog.com/monday-motivation-quotes/
#         quotes_list = quotes.readlines()
#         # quote = choice(quotes_list)
#         # print(quote)
#
#     with smtplib.SMTP("smtp.gmail.com") as connection:  # email provider address.
#         connection.starttls()
#         connection.login(user=my_mail, password=password)
#         connection.sendmail(
#             from_addr=my_mail,
#             to_addrs="fortestinfo@gmail.com",  # to address.
#             msg=f"Subject:Monday_Greetings\n\n{choice(quotes_list)}"  # Subject and body of the letter.
#         )


from datetime import datetime
import pandas as pd
from random import choice
import smtplib


def send_mail(content_, to_mail):
    my_mail = "fortest@gmail.com"  # address to login.
    password = "gtrgvvpzntyjsssu"  # app password.
    with smtplib.SMTP("smtp.gmail.com") as connection:  # email provider address.
        connection.starttls()
        connection.login(user=my_mail, password=password)
        connection.sendmail(
            from_addr=my_mail,
            to_addrs=to_mail,  # to address.
            msg=f"Subject:{content_}"  # Subject and body of the letter.
        )


# Get current date time
date = datetime.now()
current_month = date.month
current_day = date.day
current_hour = date.hour

# Get data from csv
birthday_data = pd.read_csv('birthdays.csv')
print(birthday_data)
letter_template_list = ['./letter_templates/letter_1.txt', './letter_templates/letter_2.txt',
                        './letter_templates/letter_3.txt', ]

# Filter with current month and day
current_day_data = birthday_data[birthday_data['month'] == current_month]
current_day_data = current_day_data[current_day_data['day'] == current_day]

# Iterate through rows
for index, row in current_day_data.iterrows():
    if current_hour == 8:
        with open(choice(letter_template_list), mode='r') as letter_template:
            content = letter_template.readlines()
            content[0] = content[0].replace('[NAME]', row["name"])
            to_letter = ''
            for con in content:
                to_letter += con
            print(to_letter)
        send_mail(to_letter, row['email'])
