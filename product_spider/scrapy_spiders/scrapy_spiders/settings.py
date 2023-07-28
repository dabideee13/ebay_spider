import os
import datetime


def create_log_file_path():
    if not os.path.exists('logs'):
        os.makedirs('logs')

    now = datetime.datetime.now()
    log_file_path = f'logs/ebay_spider_{now.strftime("%Y-%m-%d_%H-%M-%S")}.log'
    
    return log_file_path


BOT_NAME = 'scrapy_spiders'

SPIDER_MODULES = ['product_spider.scrapy_spiders.scrapy_spiders.spiders']
NEWSPIDER_MODULE = 'product_spider.scrapy_spiders.scrapy_spiders.spiders'

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
   'product_spider.scrapy_spiders.scrapy_spiders.pipelines.ScrapySpidersPipeline': 300,
}

DOWNLOAD_DELAY = 0.25

AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 5    
AUTOTHROTTLE_MAX_DELAY = 60   
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0 

CONCURRENT_REQUESTS = 32

COOKIES_ENABLED = False 

DOWNLOADER_MIDDLEWARES = {
   'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
   'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
   'scrapy.downloadermiddlewares.retry.RetryMiddleware': 500,
   'scrapy_proxies.RandomProxy': 100,
   'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
   'product_spider.scrapy_spiders.scrapy_spiders.middlewares.ScrapySpidersDownloaderMiddleware': 543,
}

RETRY_TIMES = 10
RETRY_HTTP_CODES = [500, 502, 503, 504, 400, 403, 404, 408]

EXTENSIONS = {
   'scrapy.extensions.throttle.AutoThrottle': 300,
}

PROXY_MODE = 0
RANDOM_UA_PER_PROXY = True

DEFAULT_REQUEST_HEADERS = {
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Language': 'en',
}

HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 0 
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

PROXY_LIST = 'product_spider/scrapy_spiders/proxy_list_cleaned.txt'

LOG_LEVEL = 'INFO'
LOG_FILE = create_log_file_path()
LOG_STDOUT = True
LOG_SHORT_NAMES = True
