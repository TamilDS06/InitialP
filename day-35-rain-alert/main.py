import requests
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


api_key = "bb700d38129771c8513ef021a9fe4347"
parameters = {
    'lat': 11.016844,
    'lon': 76.955833,
    'exclude' 'current,minutely,daily'
    'appid': api_key.lower()
}

response = requests.get(url=f"https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()
weather_slice = data['hourly'][:12]

will_rain = False
for hour in weather_slice:
    condition_code = hour['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    send_mail("totestfor@gmail.com", "Bring an Umbrella.")


# print(data['hourly'][0]['weather'][0]['id'])
# https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2
# https://www.ventusky.com/
# https://www.pythonanywhere.com/
# https://apilist.fun/
