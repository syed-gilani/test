# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SputnikItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    article_headline = scrapy.Field()
    publication_date = scrapy.Field()
    article_text = scrapy.Field()
