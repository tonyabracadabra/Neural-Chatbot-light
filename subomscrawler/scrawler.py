__author__ = "Xupeng Tong"
__copyright__ = "Copyright 2017, subtitle scrawler"
__email__ = "tongxupeng.cpu@gmail.com"

import scrapy
from scrapy.spiders import BaseSpider
from items import SubtitleItem
from scrapy.http import Request
from scrapy.selector import Selector
import scrapy
import re

class SubtitleSpider(BaseSpider):
    name = 'subom subtitle'
    allowed_domains = ['subom.net']
    max_cid = 100

    def start_requests(self):
        for i in range(1, self.max_cid):
            yield Request('http://www.subom.net/sinfo/{0}'.format(i))

    def parse(self, response):
        subtitle = SubtitleItem()

        # parse from the javascript parameter
        download = response.xpath("//a[contains(@href,'javascript:#')]/@onclick").extract_first()
        file_name = response.xpath("//a[contains(@href,'javascript:#')]/text()").extract_first()
        id_1, id_2 = map(int, re.split("[()'\s,]+", download)[1:3])

        # retrieve the url for download
        subtitle['url'] = 'http://www.subom.net/index.php?m=down&a=sub&id={0}&s_id={1}'.format(id_1, id_2)
        subtitle['file_name'] = file_name

        # urllib.urlretrieve(subtitle['url'], subtitle['file_name'])

        return subtitle