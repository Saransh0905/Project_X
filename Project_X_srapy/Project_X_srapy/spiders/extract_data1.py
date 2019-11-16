        
import scrapy,csv
from scrapy.http import Request

l = []
with open ("/home/saransh/Documents/Github/Project_X/organisedData/data_main.csv","r") as data:

    for line in data:
        array = line.split(',')
        l.append(array[1])
    l = l[1:len(l)]
    #scrapy.Spider.start_urls = [l[1]]

class Protease(scrapy.Spider):
    global l
    start_urls = []
    start_urls = l
    name = 'Proteas'
    def __init__(self):
        self.infile = open("output.csv","w",newline="")

    def start_requests(self):
        for link in self.start_urls:
            print('hellohellohel-----------hello',str(link))
            
            yield self.make_requests_from_url(url = str(link))
        print('_______________',str(l[0]))
    def parse(self,response):
        #response = response[1]
        #print(response.url)
        GO_MF = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "molecular_function", " " ))]//a[not(ancestor-or-self::div[@typeof="ScholarlyArticle"])]/text()').extract()
        K_MF = response.xpath("//*[(@id = 'function')]//tr[(((count(preceding-sibling::*) + 1) = 1) and parent::*)]//a[not(ancestor::span[@class='evidenceContainer'])]/text()").extract()
        combined = GO_MF + K_MF
        writer = csv.writer(self.infile)
        writer.writerow(combined)

        yield {
            'entry': combined
        } 
        #print("_-_-_-_--_-_-_-_-_-_--_-_-_-_-_-_-_-_-__-_-_-_--___-___-___-__-___-____-_-_-_-_-_-_-_-____-__-_-_-_")   
            
        
        
        

    