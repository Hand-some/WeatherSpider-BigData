# -*- coding: utf-8 -*-
import scrapy

from WeatherSpider.items import WeatherspiderItem

class HistoryweatherSpider(scrapy.Spider):
    name = 'historyWeather'
    allowed_domains = ['tianqi.com']
    start_urls = ['http://lishi.tianqi.com/']

    def parse(self, response):
    
        # Get the name list of all regions
        area_list = response.xpath("//div[@id='tool_site']/div[2]/ul/li/a/text()").extract()
        # Get the url list of all regions
        url_list = response.xpath("//div[@id='tool_site']/div[2]/ul/li/a/@href").extract()
        print(len(url_list))
        
        for area, url in zip(area_list, url_list):
            # print area,"------",url
            if url == '#':
                continue
            yield scrapy.Request(url, callback=self.parse_area, meta={'area_name': area})

    def parse_area(self, response):
        area = response.meta['area_name']
        # print area

        url_list = response.xpath("//*[@id='tool_site']/div[2]/ul/li/a/@href").extract()
        for url in url_list:
            # print url
            yield scrapy.Request(url, callback=self.parse_data, meta={'area_name': area})

    def parse_data(self, response):
        area = response.meta['area_name']
        # print area, '---', response.url
        data_list = response.xpath("//*[@id='tool_site']/div[@class='tqtongji2']/ul")
        # print(len(data_list),'---')

        for data in data_list:
            
            item = WeatherspiderItem()
            
            item['area'] = area
            item['date'] = data.xpath("./li[1]/text()").extract_first()
            if item['date'] == None:
                item['date'] = data.xpath("./li[1]/a/text()").extract_first()

            item['max_t'] = data.xpath("./li[2]/text()").extract_first()
            item['min_t'] = data.xpath("./li[3]/text()").extract_first()
            item['weather'] = data.xpath("./li[4]/text()").extract_first()
            item['wind_direction'] = data.xpath("./li[5]/text()").extract_first()
            item['wind_power'] = data.xpath("./li[6]/text()").extract_first()
            # print(area, item['date'])
            yield item
