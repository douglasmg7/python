#!/home/douglasmg7/miniconda3/envs/web_scraping/bin/python3
from bs4 import BeautifulSoup
import requests
import lxml

#  result = requests.get('https://www.google.com')
#  content = result.text

def load_html():
    with open('./html_example.html') as file:
        return file.read()

content = load_html()
soup = BeautifulSoup(content, 'lxml')

print(soup.prettify())

#  print(soup.find(id='some_id'))
#  print(soup.find('article', class_='main-article'))
#  print(soup.find('p'))
#  print(soup.findAll('p'))
#  print(soup.find_all('p'))
