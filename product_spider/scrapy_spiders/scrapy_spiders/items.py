import scrapy


class ProductItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    price = scrapy.Field()
    image_url = scrapy.Field()