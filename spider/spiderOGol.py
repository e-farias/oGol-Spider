import scrapy
from scrapy.crawler import CrawlerProcess

class OGolSpider(scrapy.Spider):
    name = 'oGol'
    start_urls = ['https://www.ogol.com.br/proximos_jogos.php']

    def parse(self, response):
        #Scraping the data
        teamsHome = response.xpath('//tr//td[re:test(@class, "text home")]//div//a[re:test(@href, "equipa.php?")]/text()').getall()
        teamsAway = response.xpath('//tr//td[re:test(@class, "text away")]//div//a[re:test(@href, "equipa.php?")]/text()').getall()
        gamesUrls = response.xpath('//tr//td//a[re:test(@href, "match_live.php?")]/@href').getall() + response.xpath('//tr//td[re:test(@class, "vs")]//a[re:test(@href, "jogo.php?")]/@href').getall()
        dates = response.xpath('//tr//td[re:test(@class, "date")]/text()').getall()
        datesPhasesAndHours = response.xpath('//tr//td/text()').getall()
        hours = [datesPhasesAndHours[i] for i in range(1, len(datesPhasesAndHours), 3)]
        #hours = [response.xpath('//tr//td/text()').getall()[i] for i in range(1, len(response.xpath('//tr//td/text()').getall()), 3)]

        #Formatting and cleaning data
        gamesUrls = [url.replace('/', '') for url in gamesUrls]
        hours = [hour.replace(':', 'h') for hour in hours]
        dates = [date.replace('-', '/') for date in dates]
        dataExport = [[home]+[away]+[hour]+[date]+[url] for home, away, hour, date, url in zip(teamsHome, teamsAway, hours, dates, gamesUrls)]
        
        print('\nJogos Disponíveis:', dataExport, '\n')
        print('Número de Jogos:', len(dataExport), '\n')

        pass
    
process = CrawlerProcess()
process.crawl(OGolSpider)
process.start()
