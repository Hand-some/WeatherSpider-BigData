# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WeatherspiderItem(scrapy.Item):
    # define the fields for your item here like:
    area = scrapy.Field()
    date = scrapy.Field()
    max_t = scrapy.Field()
    min_t = scrapy.Field()
    weather = scrapy.Field()
    wind_direction = scrapy.Field()
    wind_power = scrapy.Field()