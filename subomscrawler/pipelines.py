__author__ = "Xupeng Tong"
__copyright__ = "Copyright 2017, subtitle scrawler"
__email__ = "tongxupeng.cpu@gmail.com"


import scrapy
from scrapy.exceptions import DropItem

class DropBadPipeline(object):

    def process_item(self, item, spider):
        if item['file_name'][-3:]:
            if item['price_excludes_vat']:
                item['price'] = item['price'] * self.vat_factor
            return item
        else:
            raise DropItem("nvm %s" % item)


# class DownloadPipeline(object):
#     def process_item(self, item, spider):
#         print "------------------------"
#         print item['url']
#         # if len(urllib.urlopen(item['url']).readline() < 10):
#         #     return

#         urllib.retrieve(item['url'], item['file_name'])

#         return item