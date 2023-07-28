import scrapy
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError, TCPTimedOutError
from product_spider.scrapy_spiders.scrapy_spiders.items import ProductItem


class EbaySpider(scrapy.Spider):
    name = 'ebay'
    urls = ['https://www.ebay.com/deals']

    def start_requests(self):
        self.logger.info('Starting the spider')

        for url in self.urls:
            self.logger.debug('Crawling URL: %s', url)
            yield scrapy.Request(url=url, callback=self.get_category_links, errback=self.handle_failure)

    def handle_failure(self, failure):
        self.logger.error(repr(failure))

        if failure.check(HttpError):
            response = failure.value.response
            self.logger.error('HttpError occurred on %s', response.url)

        elif failure.check(DNSLookupError):
            request = failure.request
            self.logger.error('DNSLookupError occurred on %s', request.url)

        elif failure.check(TimeoutError, TCPTimedOutError):
            request = failure.request
            self.logger.error('TimeoutError occurred on %s', request.url)

    def get_category_links(self, response):
        self.logger.info('Getting category links from: %s', response.url)
        menu_links = response.xpath('//ul[@role="menubar"]/li/a/@href').extract()

        for link in menu_links:
            yield scrapy.Request(url=link, callback=self.get_products_by_section)

    def get_products_by_section(self, response):
        self.logger.info('Getting products from section: %s', response.url)
        sections = response.xpath('//div[@class="sections-container"]/div')

        for section in sections:
            show_more = section.xpath('.//div[@class="dne-show-more-link"]/a/@href')

            if show_more.get():
                yield scrapy.Request(url=show_more.get(), callback=self.show_more_products)

            else:
                products = response.xpath('.//div[@class="row"]/div/div/a/@href').extract()

                for product in products:
                    yield scrapy.Request(url=product, callback=self.parse_product_details)

    def show_more_products(self, response):
        self.logger.info('Showing more products from: %s', response.url)
        products = response.xpath('.//div[@class="row"]/div/div/a/@href').extract()

        for product in products:
            yield scrapy.Request(url=product, callback=self.parse_product_details)

    def parse_product_details(self, response):
        self.logger.info('Parsing product details from: %s', response.url)

        name = response.xpath('//h1[@class="x-item-title__mainTitle"]/span/text()').get()
        price = response.xpath('//div[@class="x-bin-price__content"]/div/span/text()').get()
        image = response.xpath('//div[@class="ux-image-magnify__container"]/img/@src').get()

        item = ProductItem()
        item['name'] = name
        item['price'] = price
        item['image_url'] = image
        item['url'] = response.url

        self.logger.debug('Item created: %s', item)

        yield item
