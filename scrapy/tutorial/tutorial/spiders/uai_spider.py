import scrapy
import re

class QuotesSpider(scrapy.Spider):
    name = "uai"

    def start_requests(self):
        urls = [
            #  'http://www.uai.com.br',
            'file:///home/douglasmg7/code/python/scrapy/tutorial/uai.html'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
            #  l = response.css('span.news::text').getall()
            #  len(response.css('span.news.-title').getall())
            #  >>> l =response.css('span.news.-title::text').getall()
            #  >>> [x for x in l if 'Bolsa' in x]
            #  [x for x in l if re.search(r'\bBolsa\b', x)]
            #  [x for x in l if re.search(r'\bbolsa\b', x, flags=re.IGNORECASE)]

            #  re_bolsa = re.compile(r'\bBolsa\b')
            re_bolsa = re.compile(r'\bem\b', flags=re.IGNORECASE)

            for item in response.css('a.news'):
                title = item.css('span.news::text').get()
                #  print(f'type: {type(title)}')
                if title != None and re_bolsa.search(title) != None:
                    link = item.css('a::attr(href)').get()
                    yield {
                        'title': title,
                        'link': link,
                    }
                    #  print(title)
                    #  print(link)



    #  def parse(self, response):
        #  filename = 'uai_temp.html'
        #  with open(filename, 'wb') as f:
            #  f.write(response.body)
            #  #  l = response.css('span.news::text').getall()
            #  #  len(response.css('span.news.-title').getall())
            #  #  >>> l =response.css('span.news.-title::text').getall()
            #  #  >>> [x for x in l if 'Bolsa' in x]
            #  #  [x for x in l if re.search(r'\bBolsa\b', x)]
            #  #  [x for x in l if re.search(r'\bbolsa\b', x, flags=re.IGNORECASE)]


            #  r = response.css('a.news')[0]
            #  title = r.css('span.news::text').get()
            #  link = r.css('a::attr(href)').get()

        #  self.log(f'Saved file {filename}')