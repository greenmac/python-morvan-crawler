# https://morvanzhou.github.io/tutorials/data-manipulation/scraping/5-02-scrapy/
# https://github.com/MorvanZhou/easy-scraping-tutorial/blob/master/notebook/5-2-scrapy.ipynb
import scrapy

class MofanSpider(scrapy.Spider):
    name = 'mofan'
    start_urls = ['https://morvanzhou.github.io/',]

    # unseen = set()
    # seen = set()      # we don't need these two as scrapy will deal with them automatically

    def parse(self, response):
        yield {     # return some results
            'title': response.css('h1::text').extract_first(default='Missing').strip().replace('"', ""),
            'url': response.url,
        }

        urls = response.css('a::attr(href)').re(r'^/.+?/$') # find all sub urls
        for url in urls:
            yield response.follow(url, callback=self.parse) # it will filter duplication automatically
# pip install pypiwin32
# lastly, run this in terminal
# scrapy runspider 502scrapy.py -o res.json