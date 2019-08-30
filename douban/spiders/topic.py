# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem
from scrapy.http import Request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
}


class TopicSpider(scrapy.Spider):
    name = 'topic'
    allowed_domains = ['douban.com']
    start_urls = ['https://www.douban.com/gallery/all']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, headers=headers, encoding='utf-8', callback=self.parse)

    def parse(self, response):
        for sel in response.css('a.topic-tab-btn'):
            typo = sel.xpath('./span[1]/text()').extract()
            num = sel.xpath('./span[2]/text()').re(r'\d+')
            new_url = sel.xpath('./@href').extract()
            new_url = 'https://www.douban.com' + new_url[0]
            self.logger.info('{},{},{}'.format(typo, num, new_url))
            item = DoubanItem()
            item['typo'] = typo
            item['typo_num'] = num
            item['typo_url'] = new_url
            request = Request(new_url, headers=headers,
                    callback=self.parse_topic)
            request.meta['item'] = item
            yield request

    def parse_topic(self, response):
        item = response.meta['item']
        for sel in response.xpath('//li[@class="topic-link"]'):
            item['title'] = sel.xpath('./a/text()').extract()
            item['text_num'] = sel.xpath('./span[1]/text()').extract()
            item['topic_url'] = sel.xpath('./a/@href').extract()
            yield item