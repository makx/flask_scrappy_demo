from scrapy.item import Item, Field


class UrlItem(Item):

    name = Field()
    description = Field()
    url = Field()