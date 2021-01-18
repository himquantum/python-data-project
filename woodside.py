import requests
from bs4 import BeautifulSoup  # to parse the data from url
wood_url = "https://www.woodsidehomes.com/california-east-bay-sacramento/california-community-zephyr-at-ellis-station"
headers = {"user-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/87.0.4280.88 Safari/537.36'}
page = requests.get(wood_url, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id='computers')
plan_3 = str(title).find("From $611,990")

if plan_3 < 0:
    print("Zephyr plan 3 price has changed !! CHECK NOW")
