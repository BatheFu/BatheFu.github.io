from fake_useragent import UserAgent
ua = UserAgent()
# -*- coding: utf-8 -*-

# Scrapy settings for amazonbook project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'amazonbook'

SPIDER_MODULES = ['amazonbook.spiders']
NEWSPIDER_MODULE = 'amazonbook.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'amazonbook (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
CONCURRENT_REQUESTS_PER_IP = 8

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'User-Agent': ua.ie,
    'Cookie': 'x-wl-uid=1D0pBm2QtLNwqdEFRvAFb7VCbc4vYLwKuD/lRv6mLAwBpD1I/lx7IPpwh23m4x1wc3s8OqMnvhEs=; session-id=460-3275149-1245261; ubid-acbcn=461-1654159-0688800; lc-acbcn=zh_CN; i18n-prefs=CNY; session-token=4inkV93hASMeg75hquQk2sTRWzd8I3CJb+mBCNp/9Qqrci5yW4qMSynmakkLRuGFa7OYyspMG+HZNzc8hQ8G8iRkSGVHDbPVnXjBD6UXo+Y5qjweSrSjc6thro9bTorlRAS0rgPVGkKj3ImB4rVZ5BRZ/URpe3oDKYA3j7Sj5DbplWeECuHcSS14ftUSagpi; session-id-time=2082729601l; csm-hit=tb:2T2HPYJPZ9TB643K32VM+s-4VJME9HRMPZFMHBJZG3E|1567149497074&adb:adblk_no&t:1567149497074',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'amazonbook.middlewares.AmazonbookSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'amazonbook.middlewares.AmazonbookDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'amazonbook.pipelines.AmazonbookPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
