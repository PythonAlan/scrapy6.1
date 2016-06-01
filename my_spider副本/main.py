#!/usr/bin/env python3
#antuor:Alan


from scrapy import cmdline
#cmdline.execute('scrapy crawl dmoz -o items.csv -t csv'.split())
cmdline.execute('scrapy crawl mac -o items.csv -t csv'.split())