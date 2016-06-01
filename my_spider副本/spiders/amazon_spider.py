#!/usr/bin/env python3
#antuor:Alan


from scrapy.spiders import Spider
from scrapy.selector import Selector
from my_spider.items import MySpiderItem


class DmozSpider(Spider):
  name = "dmoz"
  allowed_domains = ["www.amazon.com"]
  start_urls = [
     "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
     "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
     #"https://www.amazon.com/s/ref=sr_pg_2?me=A1R8D73GYDOBHG&rh=i%3Amerchant-items&page=2&ie=UTF8&qid=1464451300"

  ]

  def parse(self, response):
    """
    The lines below is a spider contract. For more info see:
    http://doc.scrapy.org/en/latest/topics/contracts.html

    @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
    @scrapes name
    """
    sel = Selector(response)
    sites = sel.xpath('//ul/li')
    items = []

    for site in sites:
      item = MySpiderItem()
      item['name'] = site.xpath('a/h2')
      item['url'] = site.xpath('a/@href').extract()
      item['description'] = site.xpath('text()').re('-\s([^\n]*?)\\n')
      items.append(item)

    return items

