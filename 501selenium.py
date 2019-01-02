# https://morvanzhou.github.io/tutorials/data-manipulation/scraping/5-01-selenium/
# https://github.com/MorvanZhou/easy-scraping-tutorial/blob/master/notebook/5-1-selenium.ipynb
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# # normal show html
# driver = webdriver.Chrome()
# driver.get('https://morvanzhou.github.io/')
# driver.find_element_by_xpath(u"//img[@alt='强化学习 (Reinforcement Learning)']").click()
# driver.find_element_by_link_text("About").click()
# driver.find_element_by_link_text(u"赞助").click()
# driver.find_element_by_link_text(u"教程 ▾").click()
# driver.find_element_by_link_text(u"数据处理 ▾").click()
# driver.find_element_by_link_text(u"网页爬虫").click()

# html = driver.page_source
# driver.get_screenshot_as_file('./img/screenshot1.png')
# driver.close()
# print(html[:200]) # html的前200個字節


# //////////
# hidden html
chrome_options = Options()
chrome_options.add_argument("--headless")       # define headless

# add the option when creating driver
driver = webdriver.Chrome(chrome_options=chrome_options)    
driver.get("https://morvanzhou.github.io/")
driver.find_element_by_xpath(u"//img[@alt='强化学习 (Reinforcement Learning)']").click()
driver.find_element_by_link_text("About").click()
driver.find_element_by_link_text(u"赞助").click()
driver.find_element_by_link_text(u"教程 ▾").click()
driver.find_element_by_link_text(u"数据处理 ▾").click()
driver.find_element_by_link_text(u"网页爬虫").click()

html = driver.page_source           # get html
driver.get_screenshot_as_file("./img/screenshot2.png")
driver.close()
print(html[:200])