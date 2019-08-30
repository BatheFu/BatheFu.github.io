# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import AmazonbookItem
from scrapy.loader import ItemLoader
from fake_useragent import UserAgent

class BookSpider(CrawlSpider):
    name = 'book'
    allowed_domains = ['amazon.cn']
    start_urls = ['https://www.amazon.cn/b/ref=s9_acss_bw_h1_CNKCD_md1_w?node=1337022071&pf_rd_m=A1U5RCOVU0NYF2&pf_rd_s=merchandised-search-top-2&pf_rd_r=WKS62GSNQ8NWABYV0RQE&pf_rd_t=101&pf_rd_p=e4094f9d-f473-42d0-846a-719ccba0de7e&pf_rd_i=116169071']

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//span[@class="a-list-item"]/a[@class="a-link-normal s-ref-text-link"]',deny='ref'), follow=True),
        Rule(LinkExtractor(restrict_xpaths='//li[@class="a-normal"]'), callback='parse_item', follow=True),
    )

    # def start_requests(self):
    #     yield scrapy.Request(i for i in self.start_urls, headers= headers)

    def parse_item(self, response):
        selector = response.xpath('//div[@class="sg-col-inner"]')
        l = ItemLoader(item=AmazonbookItem(), selector=selector)
        l.add_xpath('title','.//span[@class="a-size-medium a-color-base a-text-normal"]/text()')
        l.add_xpath('author','.//div[@class="a-row a-size-base a-color-secondary"]//span[@class="a-size-base"]/text()', re=r"\w+")
        l.add_xpath('publish_time','.//span[@class="a-size-base a-color-secondary a-text-normal"]/text()')
        l.add_xpath('rates','.//span[@class="a-icon-alt"]/text()',re=r'\d.\d')
        l.add_xpath('comment_num','.//span//a[@class="a-link-normal"]//span/text()',re=r'\d+')
        return l.load_item()
