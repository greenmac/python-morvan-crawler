# https://morvanzhou.github.io/tutorials/data-manipulation/scraping/3-01-requests/
# https://github.com/MorvanZhou/easy-scraping-tutorial/blob/master/notebook/3-1-requests.ipynb
import requests
import webbrowser # 自動打開網頁

# param = {'wd':'莫烦Python'}
# r = requests.get('http://www.baidu.com/s', params=param)
# print(r.url)
# webbrowser.open(r.url)

# # http://pythonscraping.com/pages/files/form.html
# data = {'firstname': '莫烦', 'lastname': '周'}
# r = requests.post('http://pythonscraping.com/files/processing.php', data=data)
# print(r.text)

# # upload image
# # http://pythonscraping.com/files/form2.html
# file = {'uploadFile': open('./image.png', 'rb')}
# r = requests.post('http://pythonscraping.com/files/processing2.php', files=file)
# print(r.text)

# # login
# payload = {'username': 'Morvan', 'password': 'password'}
# r = requests.post('http://pythonscraping.com/pages/cookies/welcome.php', data=payload)
# print(r.cookies.get_dict())
# r = requests.get('http://pythonscraping.com/pages/cookies/profile.php', cookies=r.cookies)
# print(r.text)

# # another general way to login
# session = requests.Session()
# payload = {'username': 'Morvan', 'password': 'password'}
# r = session.post('http://pythonscraping.com/pages/cookies/welcome.php', data=payload)
# print(r.cookies.get_dict())
# r = session.get("http://pythonscraping.com/pages/cookies/profile.php")
# print(r.text)