from scrapy import Item, Field


class LinkItem(Item):
    name = Field()
    url = Field()
    depth = Field()

