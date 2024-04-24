from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from akamai_crawler.items import LinkItem
from akamai_crawler.report_generator import (ReportGenerator)


class AkamaiSpider(CrawlSpider):
    name = "akamai_crawler"
    allowed_domains = ["crawler-test.com"]
    start_urls = ["https://crawler-test.com/"]
    handle_httpstatus_list = [400, 403, 404, 410, 451, 500, 501, 502, 503, 504]

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def __init__(self, *args, **kwargs):
        super(AkamaiSpider, self).__init__(*args, **kwargs)
        self.report_generator = ReportGenerator()
        self.image_urls = set()

    def parse_item(self, response):
        try:
            self._process_response(response)

        except Exception as e:
            self.logger.error(f"Error processing {response.url}: {str(e)} ")

    def closed(self, reason):
        self.report_generator.generate_report()

    def _process_response(self, response):
        item = self._extract_link_item(response)

        self.report_generator.add_link(item['url'], item['depth'])
        self._handle_broken_links(response)
        self._handle_duplicate_image_urls(response)

    def _extract_link_item(self, response):
        item = LinkItem()
        item['url'] = response.url
        item['depth'] = response.meta.get('depth', 0)
        return item

    def _handle_broken_links(self, response):
        if response.status in self.handle_httpstatus_list:
            self.report_generator.add_broken_link(response.url, response.status)

    def _handle_duplicate_image_urls(self, response):
        img_urls = response.css('img::attr(src)').getall()
        for img_url in img_urls:
            if img_url is not None:
                if img_url not in self.image_urls:
                    self.image_urls.add(img_url)
                else:
                    self.report_generator.add_image_url(img_url)
