# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3

class DoubanPipeline(object):
    insert_sql = "insert into MovieType (Id,Name,Url) values (?,?,?)"  #?为占位符
    def process_item(self, item, spider):
        values = (item['id'],item['name'],item['url'])
        con = sqlite3.connect(r'/data/movie.db')
        cur = con.cursor()
        cur.execute(self.insert_sql, values)
        cur.close()
        con.close()
        return item
