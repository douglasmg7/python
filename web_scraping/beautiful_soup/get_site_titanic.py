#!/home/douglasmg7/miniconda3/envs/web_scraping/bin/python3

from time import perf_counter

import requests
from bs4 import BeautifulSoup
from bs4.formatter import HTMLFormatter

html_source = "https://subslikescript.com/movie/Titanic-120338"
file_name = "titanic.html"
file_path = f"./{file_name}"
content = ""

formatter = HTMLFormatter()
formatter.indent = "    "


# Write enourmeus html to temp.html.
def write_temp(soup_content):
    with open("./temp.html", "w", encoding="utf-8") as file:
        file.write(soup_content.prettify(formatter=formatter))


# Load content from file or web.
try:
    with open(file_path) as file:
        content = file.read()
except FileNotFoundError:
    print("The html does not exist.")
    print("Downloading html Titanic")

    # Load html from web.
    time_start = perf_counter()
    content = requests.get("https://subslikescript.com/movie/Titanic-120338").text
    print(f"Time to request html: {perf_counter() - time_start}")
    print(content)

    # Write html to file.
    time_start = perf_counter()
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)
    print(f"Time to write html to file: {perf_counter() - time_start}")

# print(content)
# raise SystemExit(0)

soup = BeautifulSoup(content, "lxml")
box = soup.find("article", class_="main-article")
title = box.find("h1").get_text()
full_script = box.find("div", class_="full-script").get_text()
# full_script = box.find("div", class_="full-script").get_text(strip=True, separator=" ")
print(full_script)


# print(title.prettify(formatter=formatter))

# write_temp(box)
# print(box.prettify(formatter=formatter))

#  print(soup.find(id='some_id'))
#  print(soup.find('article', class_='main-article'))
# print(soup.find("p"))
# print(soup.find_all("p"))
