import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

MY_LAT = 50.822529
MY_LONG = -0.137163

account_sid = "AC1d6431064d99d07c6fec5c237ff00f67"

auth_token = os.environ.get("AUTH_TOKEN")

faq_key = os.environ.get("OMW_API_KEY")

OMW_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "exclude": "current,minutely,daily,alerts",
    "appid": faq_key,
}

response = requests.get(OMW_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

hour_0_id = weather_data["hourly"][0]["weather"][0]["id"]

weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
            body="It's going to rain today. Remember to bring an ☂",
            from_="+13854626954",
            to="+4407748343040"
    )

    print(message.status)