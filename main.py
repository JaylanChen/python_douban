from scrapy import cmdline
# from douban.data.DbHelper import DbHelper

# helper = DbHelper()
# helper.init_db()

cmdline.execute("scrapy crawl movie".split())