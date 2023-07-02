import requests
from tkinter import *
from datetime import datetime
import smtplib

MY_LAT = 51.178844
MY_LNG = -1.826323


def send_mail(content_, to_mail_):
    my_mail = "fortest@gmail.com"  # address to log in.
    password = "gtrgvvpzntyjsssu"  # app password.
    with smtplib.SMTP("smtp.gmail.com") as connection:  # email provider address.
        connection.starttls()
        connection.login(user=my_mail, password=password)
        connection.sendmail(
            from_addr=my_mail,
            to_addrs=to_mail_,  # to address.
            msg=f"Subject:{content_}"  # Subject and body of the letter.
        )


def iss_overhead():
    response_ = requests.get(url='http://api.open-notify.org/iss-now.json')
    response_.raise_for_status()
    data = response_.json()

    iss_latitude = float(data['iss_position']['latitude'])
    iss_longitude = float(data['iss_position']['longitude'])

    if iss_latitude - 5 <= MY_LAT <= iss_latitude + 5 and iss_longitude - 5 <= MY_LNG <= iss_longitude + 5:
        return True


def is_night():
    parameters = {
        'lat': MY_LAT,
        'lng': MY_LNG,
        'formatted': 0
    }
    response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
    # response = requests.get(url=f'https://api.sunrise-sunset.org/json?lat={MY_LAT}&lng={MY_LNG}&formatted={0}')  #
    # It is another way of send request with parameters.
    response.raise_for_status()
    data_ = response.json()
    sunrise = int(data_['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data_['results']['sunset'].split('T')[1].split(':')[0])
    print((sunrise, sunset))
    current_hour = datetime.now().hour
    if current_hour <= sunrise or current_hour >= sunset:
        return True


if iss_overhead() and is_night():
    content = "Sunrise"
    to_mail = "fortestinfo@gmail.com"
    send_mail(to_mail, content)
# reference links
# https://en.wikipedia.org/wiki/International_Space_Station
# https://en.wikipedia.org/wiki/API
# http://open-notify.org/Open-Notify-API/ISS-Location-Now/
# https://chrome.google.com/webstore/detail/json-viewer/gbmdgpbipfallnflgajpaliibnhdgobh
# https://www.webfx.com/web-development/glossary/http-status-codes/
# https://www.latlong.net/Show-Latitude-Longitude.html
# https://docs.python-requests.org/en/latest/
# https://sunrise-sunset.org/api


# kanye_quotes
# def get_quote():
#     response_ = requests.get(url="https://api.kanye.rest")
#     response_.raise_for_status()
#     quote = response_.json()['quote']
#     print(quote)
#     canvas.itemconfig(quote_text, text=quote)
#
#
# window = Tk()
# window.title("Kanye Says...")
# window.config(padx=50, pady=50)
#
# canvas = Canvas(width=300, height=414)
# background_img = PhotoImage(file="background.png")
# canvas.create_image(150, 207, image=background_img)
# quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250,
# font=("Arial", 30, "bold"), fill="white")
# canvas.grid(row=0, column=0)
#
# kanye_img = PhotoImage(file="kanye.png")
# kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
# kanye_button.grid(row=1, column=0)
#
# window.mainloop()
