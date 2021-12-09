import scrapy
from scrapy import Request
from arxiv_crawler.items import Publish

class ArxivSpider(scrapy.Spider):
    name = 'arxiv'
    allowed_domains = ['arxiv.org']
    def __init__(self, url, search_word, *args, **kwargs):
        super(ArxivSpider, self).__init__( *args, **kwargs)
        self.start_urls = [url]
        self.search_word = search_word
        self.total = 0

    def parse(self, response):

        list_response = response.xpath('//ol/li[@class="arxiv-result"]')
        links = response.xpath('//ol/li[@class="arxiv-result"]').css('.list-title').xpath('a/@href').getall()
        for link in links:
            yield Request(url=link, callback=self.parse_detail)

        self.total = self.total + len(list_response)

        print(self.total)

        try :
            next_page = response.xpath('//a[@class="pagination-next"]/@href').get()
            next_page = 'https://arxiv.org' + next_page
            yield Request(next_page, callback=self.parse)
        except TypeError:
            pass
    def parse_detail(self, response):
        title = response.xpath("//h1").css('.title::text').get()
        abstract = response.xpath("//blockquote/text()").getall()[1]
        field = response.css('.subheader').xpath('h1/text()').get()
        publish = Publish(title=title, abstract=abstract, field=field, search_word=self.search_word)
        return publish
