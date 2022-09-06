import io

from bs4 import BeautifulSoup
import requests
import time
import random
import json

#url ="https://www.avito.ru/moskva/avtomobili/nissan/pathfinder-ASgBAgICAkTgtg36mCjitg3crCg"
headers = {
   "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
  "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
       }
#
#req = requests.get(url, headers=headers)
#rc = req.text
#print(src)
#
#with open("index.html", 'w') as file:
#   file.write(src)

with io.open("index.html", encoding='utf-8') as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")
#print(soup.text)

all_cars_hrefs = soup.find_all(class_="iva-item-sliderLink-uLz1v")

all_cars_dict = {}

for item in all_cars_hrefs:
    item_text = item.get("title")
    item_href = "https://www.avito.ru" + item.get("href")
    # item_img = item.find(class_="photo-slider-item-nKXVO photo-slider-keepImageRatio-C5mWU")
    # print(item_img)
    # print(f'{item_text}: {item_href}')
    all_cars_dict[item_text] = item_href

    req = requests.get(url=item_href, headers=headers)
    src = req.text

    with open(f'{item_text}.html', "w") as file:
        file.write(src)

# with open("all_cars_dict.json", "w") as file:
#     json.dump(all_cars_dict, file, indent=4, ensure_ascii=False)

# with open("all_cars_dict.json") as file:
#     all_cars = json.load(file)

# print(all_cars)