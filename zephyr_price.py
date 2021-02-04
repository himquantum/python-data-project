import requests
import time
from bs4 import BeautifulSoup  # to parse the data from url
from playsound import playsound

sound_file = "C:\\kislay\\train_duck.wav"
wood_url = "https://www.woodsidehomes.com/california-east-bay-sacramento/california-community-zephyr-at-ellis-station"
response = requests.get(wood_url)
response_text = response.text
soup = BeautifulSoup(response_text, features='html.parser')
title = soup.find(id='computers')


def check_price():
    plan_3 = str(title).find("From $626,990")
    if plan_3 != 4185:
        print("Zephyr plan 3 price has changed!! CHECK NOW")
        playsound(sound_file)
    else:
        t = time.localtime()
        print(time.strftime("%H:%M:%S", t))


while True:
    check_price()
    time.sleep(180)
