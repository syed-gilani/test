# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import SitemapSpider
from datetime import date
from sputnik.items import SputnikItem

class SputnikbotSpider(SitemapSpider):
    name = 'sputnikbot'
    allowed_domains = ['sputniknews.com']
    sitemap_urls = ['https://sputniknews.com/sitemap_article_index.xml?date='+date.today().strftime("%Y%m%d")]

    def parse(self, response):
        article_name = response.xpath("//div[contains(@class, 'b-article__header-title')]/h1//text()").extract()
        publish_date = response.xpath("//time[contains(@class, 'b-article__refs-date')]//text()").extract()
        article_heading = response.xpath("//div[contains(@class, 'b-article__lead')]//text()").extract()
        article_text = response.xpath("//div[contains(@class, 'b-article__text')]//text()").extract()
        s = SputnikItem(article_headline=article_name, publication_date=publish_date,article_text=article_heading+article_text)
        yield s 
