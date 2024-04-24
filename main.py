from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from crawler.spiders.crawling_spider import Spider


def main():
    process = CrawlerProcess(get_project_settings())
    process.crawl(Spider)
    process.start()


if __name__ == "__main__":
    main()
