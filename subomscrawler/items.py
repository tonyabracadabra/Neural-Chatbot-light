__author__ = "Xupeng Tong"
__copyright__ = "Copyright 2017, subtitle scrawler"
__email__ = "tongxupeng.cpu@gmail.com"

import scrapy

class SubtitleItem(scrapy.Item):
    url = scrapy.Field()
    file_name = scrapy.Field()
    sub_type = scrapy.Field()