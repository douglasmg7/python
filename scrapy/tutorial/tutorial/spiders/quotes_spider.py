import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    #  def start_requests(self):
        #  urls = [
            #  'http://quotes.toscrape.com/page/1/',
            #  'http://quotes.toscrape.com/page/2/',
        #  ]
        #  for url in urls:
            #  yield scrapy.Request(url=url, callback=self.parse)

    #  def parse(self, response):
        #  page = response.url.split("/")[-2]
        #  filename = f'quotes-{page}.html'
        #  with open(filename, 'wb') as f:
            #  f.write(response.body)
        #  self.log(f'Saved file {filename}')

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }