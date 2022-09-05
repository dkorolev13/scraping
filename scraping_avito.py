from urllib import response
from bs4 import BeautifulSoup
import requests
import time
import random


url ="https://www.avito.ru/moskva/avtomobili/nissan/pathfinder-ASgBAgICAkTgtg36mCjitg3crCg"
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
        }

req = requests.get(url, headers=headers)
src = req.text
#print(src)

with open("index.html", 'w') as file:
    file.write(src)


 