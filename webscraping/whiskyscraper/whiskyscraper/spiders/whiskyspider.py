#!/usr/bin/env python3
"""Module containing the scraper Spider WhiskeySpider.
"""

import scrapy
from whiskyscraper.items import WhiskyscraperItem
from scrapy.loader import ItemLoader


class WhiskySpider(scrapy.Spider):
    """ Scrapy spider for getting whisky information off of whiskyshop.com.
    """
    name = 'whisky'
    start_urls = ['https://www.whiskyshop.com/scotch-whisky?item_availability=In+Stock']

    def parse(self, response):
        """Function that pulls the name, price, and link for each whiskey from
        the start url and all next pages.

        Args:
            response (scrapy.Request): response from scrapy fetch.
        """
        for products in response.css('div.product-item-info'):
            l = ItemLoader(item = WhiskyscraperItem(), selector=products)
            l.add_css('name', 'a.product-item-link')
            l.add_css('price', 'span.price')
            l.add_css('link', 'a.product-item-link::attr(href)')

            yield l.load_item()
        
        next_page = response.css('a.action.next').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

