from scrapy.item import Item, Field


class UrlItem(Item):

    title = Field()
    description = Field()
    url = Field()