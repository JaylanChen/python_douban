# -*- coding: utf-8 -*-
import scrapy
from douban.items import MovieTypeItem,MovieItem

class DoubanSpider(scrapy.Spider):
    #名称
    name = 'douban'
    #爬虫域
    allow_domains = ['douban.com']
    #设置URL
    start_urls = ['https://movie.douban.com/chart']

    # def start_requests(self):
    #     urls = ['https://movie.douban.com/chart']
    #     for url in urls:
    #         yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        print(response.url)
        movieTypes = response.css('div#content div.aside div.types span')

        for each in movieTypes:
            typeItem = MovieTypeItem()
            print(each)
            #名称
            typeItem['name'] = each.css('a::text').extract_first()
            typeItem['url'] = each.css('a::attr(href)').extract()[0]
            typeItem['id'] = each.css('a::attr(href)').re(r'&type=(\d+)&')[1]
            yield typeItem
    