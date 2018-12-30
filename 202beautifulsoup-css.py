# https://morvanzhou.github.io/tutorials/data-manipulation/scraping/2-02-beautifulsoup-css/
# https://github.com/MorvanZhou/easy-scraping-tutorial/blob/master/notebook/2-2-beautifulsoup-css.ipynb
# https://morvanzhou.github.io/static/scraping/list.html
import requests
from bs4 import BeautifulSoup

res = requests.get('https://morvanzhou.github.io/static/scraping/list.html')
html = res.text

soup = BeautifulSoup(html, features='lxml')

# use class to narrow search
month = soup.find_all('li', {'class':'month'})
for m in month:
    print(m.text)

print('----------')

jan = soup.find('ul', {'class':'jan'})
d_jan = jan.find_all('li')
for d in d_jan:
    print(d.text)