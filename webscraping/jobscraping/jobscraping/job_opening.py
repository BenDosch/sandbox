#!/usr/bin/env python3
"""Module that contains the scrapy Item for job openings.
"""

import scrapy


class JobOpeningItem(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    company = scrapy.Field()
    department = scrapy.Field()
    location = scrapy.Field()
    description = scrapy.Field()
    requirements = scrapy.Field()
    link = scrapy.Field()

    def __repr__(self):
        """only print out title after exiting the Pipeline"""
        return repr({"title": self['title']})
