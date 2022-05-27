import requests
from bs4 import BeautifulSoup
import csv
from time import sleep

f = open("pc_parts.csv", "w", encoding="utf-8-sig", newline="\n")
file_obj = csv.writer(f)
file_obj.writerow(["Title", "Price", "Image_URL"])
h = {"Accept-Language": "en-US"}

index = 1

while index <= 5:
    try:
        url = f"https://pcroom.ge/kategoria/kompiuteris-natsilebi/page/{index}/"
        r = requests.get(url, headers=h)

        soup = BeautifulSoup(r.text, "html.parser")
        parts = soup.find("div", {"class": "products"})
        pc_parts = parts.find_all("div", {"class": "product-grid-item"})

        for book in pc_parts:
            info = book.find("h3", {"class": "wd-entities-title"}).a.text
            price = book.find("span", {"class": "price"}).ins.span.bdi.text
            image_url = book.img.attrs["src"]
            file_obj.writerow([info, price, image_url])
    except:
        print("")

    index += 1
    sleep(3)