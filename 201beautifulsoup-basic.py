# https://morvanzhou.github.io/tutorials/data-manipulation/scraping/2-01-beautifulsoup-basic/
# https://github.com/MorvanZhou/easy-scraping-tutorial/blob/master/notebook/2-1-beautifulsoup-basic.ipynb
# https://morvanzhou.github.io/static/scraping/basic-structure.html
from bs4 import BeautifulSoup
import requests

html = requests.get('https://morvanzhou.github.io/static/scraping/basic-structure.html').text

soup = BeautifulSoup(html, features='lxml')

all_herf = soup.find_all('a')
all_herf = [l['href'] for l in all_herf]
print(all_herf)

all_herf = soup.find_all('a')
for l in all_herf:
    print(l['href'])