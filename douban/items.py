# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    typo = scrapy.Field()
    title = scrapy.Field()
    typo_num = scrapy.Field()
    typo_url = scrapy.Field()
    article_num = scrapy.Field()
    viewnum = scrapy.Field()
    topic_url = scrapy.Field()
    topic_abs = scrapy.Field()
    user_name = scrapy.Field()
    user_text = scrapy.Field()
    likes = scrapy.Field()
    dislikes = scrapy.Field()
    create_time = scrapy.Field()
    replies = scrapy.Field()
    retweets = scrapy.Field()