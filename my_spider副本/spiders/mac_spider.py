#!/usr/bin/env python3
#antuor:Alan

from scrapy.spiders import Spider
from scrapy.selector import Selector
from my_spider.items import MySpiderItem


class DmozSpider(Spider):
  name = "mac"
  allowed_domains = ["www.pc6.com"]
  start_urls = [
     "http://www.pc6.com/mac/pmsj_647_1.html",
     "http://www.pc6.com/mac/pmsj_647_2.html",

  ]

  def parse(self, response):
    """
    The lines below is a spider contract. For more info see:
    http://doc.scrapy.org/en/latest/topics/contracts.html

    @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
    @scrapes name
    """
    sel = Selector(response)
    names = sel.xpath('//li')
    items = []

    for name in names:
        item = MySpiderItem()
        item['name'] = str(name.xpath('b/a/text()').extract())
        item['description'] = str(name.xpath('p/text()').extract())
        item['update'] = str(name.xpath('i/s/text()').extract())
        items.append(item)
    return (items)
