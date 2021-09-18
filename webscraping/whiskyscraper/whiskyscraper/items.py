# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags


def remove_currency(value):
    """Removes the £ symbol and trailing whitespace from a string.

    Args:
        value (str): String to clean.
    """
    return value.replace('£', '').strip()

class WhiskyscraperItem(scrapy.Item):
    """Item to contain information about Wihisky found by a spider.
    """
    name = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
    price = scrapy.Field(input_processor = MapCompose(remove_tags, remove_currency), output_processor = TakeFirst())
    link = scrapy.Field()
