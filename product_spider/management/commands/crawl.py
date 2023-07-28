from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from product_spider.scrapy_spiders.scrapy_spiders import settings as scrapy_settings


class Command(BaseCommand):
    def handle(self, *args, **options):
        settings = Settings()
        settings.setmodule(scrapy_settings)
        process = CrawlerProcess(settings=settings)
        process.crawl('ebay')
        process.start()