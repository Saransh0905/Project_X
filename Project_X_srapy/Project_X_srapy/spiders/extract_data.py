import scrapy 
global l
l = []
with open ("/home/saransh/Documents/Project_X/Project_X/organisedData/d.csv","r") as data:
    
    for line in data:
        array = line.split(',')
        l.append(array[1])
    print(l[5])
class Protease(scrapy.Spider):
    global l
    name = 'Protease'
    start_urls = [l[5]]
    

    def parse(self,response):
        print(response.url)
        GO_MF = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "molecular_function", " " ))]//a[not(ancestor-or-self::div[@typeof="ScholarlyArticle"])]/text()').extract()
        K_MF = response.xpath("//*[(@id = 'function')]//tr[(((count(preceding-sibling::*) + 1) = 1) and parent::*)]//a[not(ancestor::span[@class='evidenceContainer'])]/text()").extract()
        combined = GO_MF + K_MF
        yield {
            'entry': combined
        }        
    