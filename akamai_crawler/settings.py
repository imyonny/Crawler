BOT_NAME = "crawler_project"

SPIDER_MODULES = ["akamai_crawler.spiders"]
NEWSPIDER_MODULE = "akamai_crawler.spiders"

LOG_LEVEL = 'ERROR'  # Adjust log level as needed for debugging or monitoring

ROBOTSTXT_OBEY = True

CONCURRENT_REQUESTS = 16  # Adjust based on server capacity and network conditions

RETRY_ENABLED = True
RETRY_TIMES = 3
RETRY_HTTP_CODES = [500, 502, 503, 504, 408]

DOWNLOAD_TIMEOUT = 5  # Increase timeout to handle slow responses

AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 1  # Start with a small delay
AUTOTHROTTLE_MAX_DELAY = 10  # Increase max delay to handle high latencies
AUTOTHROTTLE_TARGET_CONCURRENCY = 4.0  # Adjust concurrency target based on server capacity

HTTPCACHE_ENABLED = False  # Disable HTTP caching for now

# Set deprecated settings to future-proof values
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
