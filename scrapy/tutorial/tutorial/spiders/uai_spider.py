import scrapy

class QuotesSpider(scrapy.Spider):
    name = "uai"

    def start_requests(self):
        urls = [
            'http://www.uai.com.br',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        filename = 'uai.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')