# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ElementItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    price = scrapy.Field()
    old_price = scrapy.Field()
    rating = scrapy.Field()
    reviews = scrapy.Field()
    review_text = scrapy.Field()
    brand = scrapy.Field()
