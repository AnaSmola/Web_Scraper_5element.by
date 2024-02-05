import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class CategoryScrapySpider(CrawlSpider):
    name = 'all_categories'
    start_urls = ['https://5element.by/catalog/9-smartfony-i-gadzhety']
# 'https://5element.by/catalog/9-smartfony-i-gadzhety'
# 'https://5element.by/catalog/13-televizory-i-video'
# 'https://5element.by/catalog/1403-televizory'
# 'https://5element.by/catalog/377-smartfony'
# 'https://5element.by/products/767076-smartfon-xiaomi-poco-m5-6gb-128gb-zelenyy-eu'

    rules = {
        Rule(LinkExtractor(allow='catalog')),
        Rule(LinkExtractor(allow='characteristics')),
        Rule(LinkExtractor(allow='reviews')),
        Rule(LinkExtractor(allow='products'), callback='parse_items')
    }

    def parse_items(self, response):
        yield {
            'name': response.css('h1.section-heading__title::text').get(),
            'price': response.css('div.pp-price::text').get(),
            'rating': response.css('div.pp-rating-count::text').get().strip(),
            'reviews_string': response.css('a._anchor-info::text').get().strip(),
            'brand': response.css('div.breadcrumbs a::text')[5].get(),
            'reviews_text': response.css('.p-communication__body p::text')
        }