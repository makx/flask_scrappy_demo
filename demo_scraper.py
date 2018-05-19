import re
import scrapy
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from pprint import pprint



class QuoteSpider(scrapy.Spider):
    name = 'quote'
    
    def start_requests(self):
        pprint('el start requests ' + self.url['url'])
        # return [scrapy.FormRequest(self.url['url'])]
        yield scrapy.Request(self.url['url'])

    def parse(self, response):
        # titles = response.xpath('//article[@class="nota]"]//h6/text()')
        titles = response.xpath('/html/head/title/text()')
        pprint('funciona el print')
        pprint(titles)
        # next_page = response.xpath('//article/a//h6/text()')
        # pprint("la proxima página ", next_page)
        print(titles)
        for quote in titles:
            # extract quote
            
            quote_text = quote.extract()
            # quote_text = self.quotation_mark_pattern.sub('', quote_text)
            
            # extract author
            # author = quote.xpath('.//span//small[@class="author"]/text()').extract_first()

            # extract tags
            # tags = []
            # for tag in quote.xpath('.//div[@class="tags"]//a[@class="tag"]/text()'):
            #     tags.append(tag.extract())

            # append to list
            # NOTE: quotes_list is passed as a keyword arg in the Flask app
            self.quotes_list.append({
                'title': quote_text
                })

    #     # if there's next page, scrape it next
    #     # next_page = response.xpath('//nav//ul//li[@class="next"]//@href').extract_first()
    #     # if next_page is not None:
    #     #     yield response.follow(next_page)


# class LinkSpider(scrapy.Spider):
#     urls = self.urls_to_scrap
#     start_urls = urls[0]['url']

#     def parse(self, response):
#         href = response.xpath('//a/href()')
        
    