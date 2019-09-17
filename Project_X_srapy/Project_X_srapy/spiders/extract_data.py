import scrapy 
class Protease(scrapy.Spider):
    name = 'Protease'
    start_urls = [
        'https://www.uniprot.org/uniprot/Q3Y6B8https://www.uniprot.org/uniprot/?query=taenia+solium+protease&sort=score'
    ]

    def parse(self,response):
         self.entry_list = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "entryID", " " ))]//a/@href')[1].extract()
         new_url = 'https://www.uniprot.org' + 
         yield {
            'entry': self.entry_list
        }        


    '''def parse2(self,response):
         title = response.css('title::text').extract()
         GO_MF = response.css(".molecular_function a::text").extract()
         #entry_list = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "entryID", " " ))]//a/@href').extract()
         yield {
         'title': title,
         'GO_MF':GO_MF
         }'''
