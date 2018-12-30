# https://morvanzhou.github.io/tutorials/data-manipulation/scraping/3-03-practice-download-image/
# https://github.com/MorvanZhou/easy-scraping-tutorial/blob/master/notebook/3-3-practice-download-images.ipynb
# http://www.ngchina.com.cn/animals/
from bs4 import BeautifulSoup
import requests
import os

URL = "http://www.nationalgeographic.com.cn/animals/"

# find list of image holder
html = requests.get(URL).text
soup = BeautifulSoup(html, 'lxml')
img_ul = soup.find_all('ul', {"class": "img_list"})
# print(img_ul)

os.makedirs('./img/', exist_ok=True)
for ul in img_ul:
    imgs = ul.find_all('img')
    for img in imgs:
        url = img['src']
        r = requests.get(url, stream=True)
        image_name = url.split('/')[-1]
        with open('./img/%s' % image_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=128):
                f.write(chunk)
        print('Saved %s' % image_name)