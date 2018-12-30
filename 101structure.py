# https://morvanzhou.github.io/tutorials/data-manipulation/scraping/1-01-understand-website/
# https://github.com/MorvanZhou/easy-scraping-tutorial/blob/master/notebook/1-1-urllib.ipynb
# https://morvanzhou.github.io/static/scraping/basic-structure.html
from urllib.request import urlopen
import re

html = urlopen('https://morvanzhou.github.io/static/scraping/basic-structure.html').read().decode('utf-8')
res = re.findall(r"<title>(.+?)</title>", html)
print("\nPage title is: ", res[0])

res = re.findall(r"<p>(.*?)</p>", html, flags=re.DOTALL)    # re.DOTALL if multi line
print("\nPage paragraph is: ", res[0])

res = re.findall(r'href="(.*?)"', html)
print("\nAll links: ", res)