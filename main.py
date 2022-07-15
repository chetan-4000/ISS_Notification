import requests
from datetime import datetime

MY_LAT = 28.636391
MY_LONG = 76.921349

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")

    data = response.json()
    iss_longitude =data["iss_position"]["longitude"]
    iss_latitude = data["iss_position"]["latitude"]

    iss_position = (iss_longitude,iss_latitude)

    if MY_LAT-5<=iss_latitude<=MY_LAT+5 and MY_LONG-5<=iss_longitude<=MY_LONG+5:
        return True


def is_night():
    parameters = {
        "lat":MY_LAT,
        "long":MY_LONG,
        "formatted":0
    }

    RESPONSE = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
    RESPONSE.raise_for_status()
    DATA = RESPONSE.json()
    sunrise = int(DATA["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(DATA["results"]["sunset"].split("T")[1].split(":")[0])


    time_now =datetime.now().hour
    if time_now>=sunset or time_now<=sunrise:
        return True

if is_night() and is_iss_overhead():
    print("Send an email to lookup")
else:
    print("It is not visible")