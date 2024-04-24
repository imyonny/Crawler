from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from akamai_crawler.spiders.crawling_spider import AkamaiSpider


def main():
    process = CrawlerProcess(get_project_settings())
    process.crawl(AkamaiSpider)
    process.start()


if __name__ == "__main__":
    main()
