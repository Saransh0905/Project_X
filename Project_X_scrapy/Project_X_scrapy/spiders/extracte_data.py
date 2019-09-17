import scrapy

class Protease(scrapy.Spider):
    name = 'Protease'
    start_urls = [
       'https://qoutes.toscrape.com/'
    ]
    
    def parse(self,response):
        title = response.css("title").extract()

        yield {'title':title}


