# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider
from items import UrlItem


class LoggerSpider(scrapy.spiders.Spider):
    # The name of the spider
    name = "datalogger"

    # The domains that are allowed (links to other domains are skipped)
    allowed_domains = []

    # The URLs to start with
    start_urls = ["http://www.celerative.com"]

    EXTENSIONS = {
        'scrapy.extensions.closespider.CloseSpider': 500
    }

    custom_settings = {
        'CLOSESPIDER_TIMEOUT': 10,
        'ITEM_PIPELINES': {
            'pipelines.MongoPipeline': 1,
        }
    }

    ITEM_PIPELINES = {
        'MongoPipeline': 300,
    }

    # This spider has one rule: extract all (unique and canonicalized) links, follow them and parse them using the parse_items method
    # rules = [
    #     Rule(
    #         LinkExtractor(
    #             canonicalize=True,
    #             unique=True
    #         ),
    #         follow=True,
    #         callback="parse_items"
    #     )
    # ]

    # Method which starts the requests by visiting all URLs specified in start_urls
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse, dont_filter=True)

    # Method for parsing items
    def parse(self, response):
        print('entro aqua')
        # links = LinkExtractor(canonicalize=False, unique=True).extract_links(response)
        # print(links)
        item = UrlItem()
        item['name'] = 'Lala'
        print(item.keys())
        # item['url'] = 'LALA '
        # item['name'] = response.xpath('/html/head/title/text()').extract()
        yield item
        # The list of items that are found on the particular page
        # items = []
        # Only extract canonicalized and unique links (with respect to the current page)
        # links = LinkExtractor(canonicalize=False, unique=True).extract_links(response)
        
        # Now go through all the found links
        # for link in links:
        #     # Check whether the domain of the URL of the link is allowed; so whether it is in one of the allowed domains
        #     # print(link)
        #     is_allowed = False
        #     for allowed_domain in self.allowed_domains:
        #         if allowed_domain in link.url:
        #             is_allowed = True
        #     # If it is allowed, create a new item and add it to the list of found items
        #     if is_allowed:
        #         item['url_from'] = response.url
        #         item['url_to'] = link.url
        #         items.append(item)
        # Return all the found items
        


