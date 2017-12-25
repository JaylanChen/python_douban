# -*- coding: utf-8 -*-
import scrapy
import json
from douban.items import MovieTypeItem,MovieItem

class MovieSpider(scrapy.Spider):
    #名称
    name = 'movie'
    #爬虫域
    allow_domains = ['douban.com']
    #设置URL
    start_urls = ['https://movie.douban.com/chart']

    # def start_requests(self):
    #     urls = ['https://movie.douban.com/chart']
    #     for url in urls:
    #         yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        movieTypes = response.css('div#content div.aside div.types span')
        movieItems = []
        for each in movieTypes:
            typeItem = MovieTypeItem()
            #名称
            typeItem['name'] = each.css('a::text').extract_first()
            typeItem['url'] = each.css('a::attr(href)').extract()[0]
            typeItem['id'] = each.css('a::attr(href)').re(r'&type=(\d+)&')[0]
            movieItems.append(typeItem)
            yield typeItem

        for item in movieItems[1:2]:
            listUrl = 'https://movie.douban.com/j/chart/top_list?type='+ item['id'] +'&interval_id=100%3A90&action=&start=0&limit=20'
            yield scrapy.Request(url=listUrl, meta={'type':item}, callback=self.parseMovies)

    def parseMovies(self, response):
        print(response.url)
        movieType = response.meta['type']
        #jsonModies = json.dumps(response.body.decode('utf-8'))
        print(response.body.decode('utf-8'))

