from scrapy import cmdline
from data.DbHelper import DbHelper

helper = DbHelper()
helper.init_db()

cmdline.execute("scrapy crawl douban".split())