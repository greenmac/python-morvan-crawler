# https://morvanzhou.github.io/tutorials/data-manipulation/scraping/2-03-beautifulsoup-regex/
# https://github.com/MorvanZhou/easy-scraping-tutorial/blob/master/notebook/2-3-beautifulsoup-regex.ipynb
# https://morvanzhou.github.io/static/scraping/table.html
import requests
from bs4 import BeautifulSoup
import re

res = requests.get('https://morvanzhou.github.io/static/scraping/table.html')
html = res.text

soup = BeautifulSoup(html, features='lxml')

img_links = soup.find_all('img', {'src':re.compile('.*?\.jpg')})
for link in img_links:
    print(link['src'])

print('----------')

course_links = soup.find_all('a', {'href':re.compile('https://morvan.*')})
for link in course_links:
    print(link['href'])