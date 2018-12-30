# https://morvanzhou.github.io/tutorials/data-manipulation/scraping/2-04-practice-baidu-baike/
# https://github.com/MorvanZhou/easy-scraping-tutorial/blob/master/notebook/2-4-practice-baidu-baike.ipynb
# https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711
import requests
from bs4 import BeautifulSoup
import re
import random

# 用串接方式連結網址
base_url = 'https://baike.baidu.com'
his = ["/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711"]
url = base_url + his[-1]

kv = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"}
# url = 'https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711'
html = requests.get(url, headers = kv, allow_redirects=False)
html.encoding='utf-8'
html = html.text
soup = BeautifulSoup(html, features='lxml')
# print(soup.find('h1').text, 'url:', url)

# find valid urls
sub_urls = soup.find_all("a", {"target": "_blank", "href": re.compile("/item/(%.{2})+$")})
# for i in sub_urls:
#     print(i['href'])
if len(sub_urls) != 0:
    his.append(random.sample(sub_urls, 1)[0]['href'])
else:
    # no valid sub link found
    his.pop() # 移除列表中的一個
# print(his)

for i in range(20):
    url = base_url + his[-1]

    html = requests.get(url, headers = kv, allow_redirects=False)
    html.encoding='utf-8'
    html = html.text
    soup = BeautifulSoup(html, features='lxml')
    print(i, soup.find('h1').text, '    url: ', his[-1])

    # find valid urls
    sub_urls = soup.find_all("a", {"target": "_blank", "href": re.compile("/item/(%.{2})+$")})

    if len(sub_urls) != 0:
        his.append(random.sample(sub_urls, 1)[0]['href'])
    else:
        # no valid sub link found
        his.pop()