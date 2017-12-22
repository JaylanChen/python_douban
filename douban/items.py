# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item,Field

class MovieTypeItem(Item):
    id = Field()
    name = Field()
    url = Field()

class MovieItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = Field()
    #名称
    name = Field()
    #上映时间
    showDate = Field()
    #别名
    alias = Field()
    #主演
    leadingRole = Field()
    #类型
    movieType = Field()
    #语言
    language = Field()
    #时长
    duration = Field()
    #评分
    grade = Field()
    #剧情简介
    introduction = Field()
    #评价数
    comments = Field()
