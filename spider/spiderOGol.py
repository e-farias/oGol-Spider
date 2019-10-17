import scrapy

class OGolSpider(scrapy.Spider):
    name = 'oGol'
    start_urls = ['https://www.ogol.com.br/proximos_jogos.php']
    data = []
    

    def parse(self, response):
        teamsHome = response.xpath('//tr//td[re:test(@class, "text home")]//div//a[re:test(@href, "equipa.php?")]/text()').getall()
        teamsAway = response.xpath('//tr//td[re:test(@class, "text away")]//div//a[re:test(@href, "equipa.php?")]/text()').getall()
        games = [x+' vs '+y for x, y in zip(teamsHome, teamsAway)]
        gamesUrls = response.xpath('//tr//td//a[re:test(@href, "match_live.php?")]/@href').getall() + response.xpath('//tr//td[re:test(@class, "vs")]//a[re:test(@href, "jogo.php?")]/@href').getall()
        dates = response.xpath('//tr//td[re:test(@class, "date")]/text()').getall()
        datesPhasesAndHours = response.xpath('//tr//td/text()').getall()
        hours = [datesPhasesAndHours[i] for i in range(1, len(datesPhasesAndHours), 3)]
        #hours = [response.xpath('//tr//td/text()').getall()[i] for i in range(1, len(response.xpath('//tr//td/text()').getall()), 3)]

        def printData():
            print('------------- teamsHome -------------\n', teamsHome)
            print('\nlen(teamsHome): ', len(teamsHome))
            print('------------- teamsAway -------------\n', teamsAway)
            print('\nlen(teamsAway): ', len(teamsAway))
            print('--------------- games ---------------\n', games)
            print('\nlen(games): ', len(games))
            print('------------- gamesUrls -------------\n', gamesUrls)
            print('\nlen(gamesUrls): ', len(gamesUrls))
            print('--------------- dates ---------------\n', dates)
            print('\nlen(dates): ', len(dates))
            print('--------------- hours ---------------\n', hours)
            print('\nlen(hours): ', len(hours))
        
        printData()