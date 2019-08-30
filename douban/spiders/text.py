# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
from scrapy import Request
from scrapy.loader import ItemLoader
from douban.items import DoubanItem
import json
with open('url.json') as jsonfile:
    topics = json.load(jsonfile)



class TextSpider(scrapy.Spider):
    name = 'text'
    allowed_domains = ['douban.com']
    start_urls =  topics.values()
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    'Cookie':'ll="118168"; bid=H4OFT_jvmrg',
}

    def start_requests(self):
    #     script = """
    # function main(splash)
    #     local num_scrolls = 10
    #     local scroll_delay = 1
    #     splash.images_enabled = false
    #     assert(splash:go{
    #         splash.args.url,
    #         headers=splash.args.headers,
    #         })
    #     local get_body_height = splash:jsfunc(
    #             "function() {return document.body.scrollHeight;}"
    #         )
    #     splash:wait(1)
    #     local scroll_to = splash:jsfunc("window.scrollTo")
    #     for _ = 1, num_scrolls do
    #         local height = get_body_height()
    #         for i = 1, 10 do
    #             scroll_to(0, height * i/10)
    #             splash:wait(scroll_delay/5)
    #         end
    #     end  
    #     return html = splash:html()
    # end
    # """

        for url in self.start_urls:
            yield SplashRequest(url, callback= self.parse, args={
                'wait':2, 'png':0,
            }, 
            )

    def parse(self, response):
        l = ItemLoader(item=DoubanItem(), response=response)
        l.add_css('article_num','span.post_count::text', re=r'\d+')
        l.add_css('viewnum','div.topic-counter::text', re=r'\d+')
        l.add_value('topic_url', response.url)
        l.add_css('title','h1.topic-title::text')
        l.add_css('topic_abs','p.topic-abstract::text')
        #l.add_css('user_text','p.status-preview::text')
        l.add_xpath('user_text','//div/p[@class="status-full hide"]/text()')
        return l.load_item()
