import scrapy
from ..items import ElementItem
from scrapy.linkextractors import LinkExtractor

class ElementScrapySpider(scrapy.Spider):

    name = 'element_scrapy'
    count = 1
    start_urls = [
         'https://5element.by/catalog/377-smartfony'
        # 'https://5element.by/catalog/1403-televizory'
        #'https://5element.by/catalog/1383-noutbuki'
        # 'https://5element.by/catalog/513-holodilniki'
        # 'https://5element.by/catalog/1141-stiralnye-mashiny'

    ]


    def parse(self, response):

        for link in response.css('a.c-text ::attr(href)'):
            yield response.follow(link, callback=self.parse_items)

        self.count += 1
        # next_page = f"https://5element.by/catalog/377-smartfony?page={self.count}"
        next_page = f'https://5element.by/catalog/1383-noutbuki?page={self.count}'
        # next_page = f'https://5element.by/catalog/1403-televizory?page={self.count}'
        # next_page = f'https://5element.by/catalog/513-holodilniki?page={self.count}'
        # next_page = f'https://5element.by/catalog/1141-stiralnye-mashiny?page={self.count}'

        yield response.follow(next_page, callback=self.parse)



    def parse_items(self, response):

        product = ElementItem()

        brand = response.css('div.breadcrumbs a::text')[5].get()
        name = response.css('h1.section-heading__title::text').get()
        price_div = response.css('div.pp-coast__item')
        price = price_div.css('div.pp-price::text, sub::text').get()
        old_price = price_div.css('div.pp-discount span::text').get()
        rating = response.css('div.pp-rating-count::text').get().strip()
        reviews_string = response.css('a._anchor-info::text').get().strip()
        numeric_filter = filter(str.isdigit, reviews_string)
        reviews = "".join(numeric_filter)

        dict_reviews = {r.css('div.pp-info-item ::attr(href)').get(): r.css('.p-communication__body p::text').getall()
                        for r in response.css('div.product-communications.product-communications-reviews')}

        review_text = [i for i in dict_reviews.values()][0]
        product['brand'] = brand
        product['name'] = name
        product['price'] = price
        product['old_price'] = old_price
        product['rating'] = rating
        product['reviews'] = reviews
        product['review_text'] = review_text

        yield product










