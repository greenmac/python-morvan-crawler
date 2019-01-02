# https://morvanzhou.github.io/tutorials/data-manipulation/scraping/4-02-asyncio/
# https://github.com/MorvanZhou/easy-scraping-tutorial/blob/master/notebook/4-2-asyncio.ipynb
import time
import asyncio
import requests
import aiohttp
from bs4 import BeautifulSoup
from urllib.request import urlopen, urljoin
import re
import multiprocessing as mp

# # //////////
# # normal
# def job(t):
#     print('start job ', t)
#     time.sleep(t)
#     print('Job ', t, ' takes ', t, ' s')
# def main():
#     [job(t) for t in range(1, 3)]
# t1 = time.time()
# main()
# print("NO async total time : ", time.time() - t1)

# # //////////
# # asyncio
# async def job(t):
#     print('start job ', t)
#     await asyncio.sleep(t) # wsit for 't' seconds, it will look for another job while await
#     print('Job ', t, ' takes ', t, ' s')
# async def main(loop):
#     takes = [loop.create_task(job(t)) for t in range(1, 3)]
#     await asyncio.wait(takes)
# t1 = time.time()
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main(loop))
# # loop.close() # # Ipython notebook gives error if close loop
# print("Async total time : ", time.time() - t1)

# # //////////
# # normal crawler
# URL = 'https://morvanzhou.github.io/'
# def normal():
#     for _ in range(2):
#         r = requests.get(URL)
#         url = r.url
#         print(url)
# t1 = time.time()
# normal()
# print("Normal total time:", time.time()-t1)

# # //////////
# # aiohttp(要先 import asyncio)
# URL = 'https://morvanzhou.github.io/'
# async def job(session):
#     response = await session.get(URL)
#     return str(response.url)
# async def main(loop):
#     async with aiohttp.ClientSession() as session:
#         tasks = [loop.create_task(job(session)) for _ in range(2)]
#         finshed, unfinished = await asyncio.wait(tasks)
#         all_results = [r.result() for r in finshed]
#         print(all_results)
# t1 = time.time()
# loop = asyncio.get_event_loop() # 得到当前上下文的事件循环
# loop.run_until_complete(main(loop))
# # loop.close()                      # Ipython notebook gives error if close loop
# print("Async total time:", time.time() - t1)

# # //////////
# # normal crawler test
# base_url = "https://morvanzhou.github.io/"
# # base_url = "http://127.0.0.1:4000/"

# # DON'T OVER CRAWL THE WEBSITE OR YOU MAY NEVER VISIT AGAIN
# if base_url != "http://127.0.0.1:4000/":
#     restricted_crawl = True
# else:
#     restricted_crawl = False
             
# seen = set()
# unseen = set([base_url])

# def parse(html):
#     soup = BeautifulSoup(html, 'lxml')
#     urls = soup.find_all('a', {"href": re.compile('^/.+?/$')})
#     title = soup.find('h1').get_text().strip()
#     page_urls = set([urljoin(base_url, url['href']) for url in urls])
#     url = soup.find('meta', {'property': "og:url"})['content']
#     return title, page_urls, url

# async def crawl(url, session):
#     r = await session.get(url)
#     html = await r.text()
#     await asyncio.sleep(0.1)        # slightly delay for downloading
#     return html

# async def main(loop):
#     pool = mp.Pool(8)               # slightly affected
#     async with aiohttp.ClientSession() as session:
#         count = 1
#         while len(unseen) != 0:
#             print('\nAsync Crawling...')
#             tasks = [loop.create_task(crawl(url, session)) for url in unseen]
#             finished, unfinished = await asyncio.wait(tasks)
#             htmls = [f.result() for f in finished]
            
#             print('\nDistributed Parsing...')
#             parse_jobs = [pool.apply_async(parse, args=(html,)) for html in htmls]
#             results = [j.get() for j in parse_jobs]
            
#             print('\nAnalysing...')
#             seen.update(unseen)
#             unseen.clear()
#             for title, page_urls, url in results:
#                 # print(count, title, url)
#                 unseen.update(page_urls - seen)
#                 count += 1

# if __name__ == "__main__":
#     t1 = time.time()
#     loop = asyncio.get_event_loop() # 得到当前上下文的事件循环
#     loop.run_until_complete(main(loop))
#     # loop.close()
#     print("Async total time: ", time.time() - t1)


# //////////
# pool crawler
base_url = 'https://morvanzhou.github.io/'
# base_url = "http://127.0.0.1:4000/"

def crawl(url):
    response = urlopen(url)
    time.sleep(0.1)             # slightly delay for downloading
    return response.read().decode()


def parse(html):
    soup = BeautifulSoup(html, 'lxml')
    urls = soup.find_all('a', {"href": re.compile('^/.+?/$')})
    title = soup.find('h1').get_text().strip()
    page_urls = set([urljoin(base_url, url['href']) for url in urls])
    url = soup.find('meta', {'property': "og:url"})['content']
    return title, page_urls, url


if __name__ == '__main__':        
    # DON'T OVER CRAWL THE WEBSITE OR YOU MAY NEVER VISIT AGAIN
    if base_url != "http://127.0.0.1:4000/":
        restricted_crawl = True
    else:
        restricted_crawl = False
        
    unseen = set([base_url,])
    seen = set()

    pool = mp.Pool(8)                       # number strongly affected
    count, t1 = 1, time.time()
    while len(unseen) != 0:                 # still get some url to visit
        if restricted_crawl and len(seen) > 20:
            break
        print('\nDistributed Crawling...')
        crawl_jobs = [pool.apply_async(crawl, args=(url,)) for url in unseen]
        htmls = [j.get() for j in crawl_jobs]                                       # request connection
        htmls = [h for h in htmls if h is not None]     # remove None

        print('\nDistributed Parsing...')
        parse_jobs = [pool.apply_async(parse, args=(html,)) for html in htmls]
        results = [j.get() for j in parse_jobs]                                     # parse html

        print('\nAnalysing...')
        seen.update(unseen)
        unseen.clear()

        for title, page_urls, url in results:
            # print(count, title, url)
            count += 1
            unseen.update(page_urls - seen)

    print('Total time: %.1f s' % (time.time()-t1, ))