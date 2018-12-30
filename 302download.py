# https://morvanzhou.github.io/tutorials/data-manipulation/scraping/3-02-download/
# https://github.com/MorvanZhou/easy-scraping-tutorial/blob/master/notebook/3-2-download.ipynb
import os
from urllib.request import urlretrieve
import requests

os.makedirs('./img/', exist_ok=True)
IMAGE_URL = 'https://morvanzhou.github.io/static/img/description/learning_step_flowchart.png'

# # urlretrieve
# urlretrieve(IMAGE_URL, './img/image1.png')

# # request download
# r = requests.get(IMAGE_URL)
# with open('./img/image2.png', 'wb') as f:
#     f.write(r.content) # 圖片不是用r.text, 要用r.content(二進制) # whole document

# download chunk by chunk 大型文件, 一部分一部分存取
r = requests.get(IMAGE_URL, stream=True)    # stream loading

with open('./img/image3.png', 'wb') as f:
    for chunk in r.iter_content(chunk_size=32): # 每32單位元寫入
        f.write(chunk)