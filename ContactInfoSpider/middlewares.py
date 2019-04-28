# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import datetime
import time
import random
import os
from TruthFinderSpider.settings import URLS_FILE

from fake_useragent import UserAgent
from tools.sliding_capcha.sliding_capthca_411 import CrackGeetest


from scrapy.http import HtmlResponse

from TruthFinderSpider.settings import MY_USER_AGENTS


class TruthfinderspiderSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(s.spider_close, signal=signals.spider_closed)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


    def spider_close(self, spider):
        spider.logger.info('Spider close: %s' % spider.name)


class TruthfinderspiderCloseSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_close, signal=signals.spider_closed)
        return s

    def spider_close(self, spider):
        print("关闭爬虫")
        if os.path.exists(URLS_FILE):
            os.remove(URLS_FILE)


class TruthfinderspiderDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)




class TruthFinderAntiCrawlDownloaderMiddleware(object):

    def process_request(self, request, spider):

        return None

    def process_response(self, request, response, spider):

        return response


class TimeToStopMiddleware(object):
    def __init__(self):
        super(TimeToStopMiddleware, self).__init__()
        self.stop_signal = 1

    def process_request(self, request, spider):

        # 爬虫爬取3个小时后停止31分钟
        spider_scrapy_start_time = spider.scrapy_start_time
        if spider_scrapy_start_time is not None:
            scrapy_time_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            true_scrapy_time_now = datetime.datetime.strptime(scrapy_time_now, '%Y-%m-%d %H:%M:%S')
            time_seconds_subtract = true_scrapy_time_now - spider_scrapy_start_time
            print(time_seconds_subtract.seconds)
            time_seconds_subtract = int(time_seconds_subtract.seconds)

            print('时间间隔：', time_seconds_subtract)
            if time_seconds_subtract % 3600 == 0 and time_seconds_subtract !=0:
                print('sleep中')
                time.sleep(900)

    def process_response(self, request, response, spider):
        print('状态码',response.status)
        if response.status in range(100,300):
            with open('./validation_url_truth_finder.text','a+') as f:
                f.write(response.url +'\n')
            with open('./truth_finder_200_user_agent.text', 'a+') as f:
                f.write(request.headers['user-agent'].decode() + '\n')


        if response.status == 403:
            with open('./truth_finder_403_url.text', 'a+') as f:
                f.write(response.url + '\n')


            with open('./truth_finder_403_user_agent.text', 'a+') as f:
                f.write(request.headers['user-agent'].decode() + '\n')

            request.headers['user-agent'] = UserAgent().random
            import time
            time.sleep(1)
            self.stop_signal += 1
            print(self.stop_signal)

            if self.stop_signal > 2000:
                spider.crawler.engine.close_spider(spider, '更换了100次user-agent了,爬虫已经被发现了')
            return request



        if response.status == 404:
            with open('./truth_finder_404_url.text', 'a+') as f:
                f.write(response.url + '\n')

        if response.status in range(300,400):
            with open('./redirection_url_truth_finder.text','a+') as f:
                f.write(response.url+'\n')

        if response.status in range(400,600) and response.status!= 404:
            with open('./invalidation_url_truth_finder.text','a+') as f:
                f.write(response.url+','+str(response.status)+'\n')
            print('被发现了,更换user-agent')
            import time
            time.sleep(1)
            self.stop_signal += 1
            print(self.stop_signal)

            if self.stop_signal > 2000:
                spider.crawler.engine.close_spider(spider, '更换了100次user-agent了,爬虫已经被发现了')

        return response



class Spider411TimeToStopMiddleware(object):
    def __init__(self):
        super(Spider411TimeToStopMiddleware, self).__init__()
        self.stop_signal = 1

    def process_request(self, request, spider):

        # 爬虫爬取3个小时后停止31分钟
        spider_scrapy_start_time = spider.scrapy_start_time
        if spider_scrapy_start_time is not None:
            scrapy_time_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            true_scrapy_time_now = datetime.datetime.strptime(scrapy_time_now, '%Y-%m-%d %H:%M:%S')
            time_seconds_subtract = true_scrapy_time_now - spider_scrapy_start_time
            print(time_seconds_subtract.seconds)
            time_seconds_subtract = int(time_seconds_subtract.seconds)

            print('时间间隔：', time_seconds_subtract)
            if time_seconds_subtract % 3600 == 0 and time_seconds_subtract !=0:
                print('sleep中')
                time.sleep(900)

    def process_response(self, request, response, spider):
        print('状态码',response.status)
        if response.status in range(100,300):
            with open('./validation_url_411.text','a+') as f:
                f.write(response.url +'\n')

        if response.status in range(400,600):
            with open('./invalidation_url_411.text','a+') as f:
                f.write(response.url+'\n')
            print('被发现了,更换user-agent')
            with open('./spider_411_response.html','w') as f:
                f.write(response.text)
            import time
            time.sleep(1)
            self.stop_signal += 1
            print(self.stop_signal)

            if self.stop_signal > 5:
                spider.crawler.engine.close_spider(spider, '更换了100次user-agent了,爬虫已经被发现了')


            # print('出现验证码,验证码的url为:{}'.format(response.url))
            crack = CrackGeetest(url=response.url)
            crack.crack()
            print('验证码识别完成')
            # print('返回信息')
            # # spider.crawler.engine.close_spider(spider, '更换了100次user-agent了,爬虫已经被发现了')
            return HtmlResponse(url=request.url,
                                body=crack.browser.page_source,
                                request=request,
                                # 最好根据网页的具体编码而定
                                encoding='utf-8',
                                status=200)

        return response



class RandomUserAgentMiddleware(object):

    def process_request(self,request,spider):
        random_number = random.choice(range(len(spider.spider_user_agent)))

        current_request_user_agent = spider.spider_user_agent[random_number]
        request.headers.setdefault('user-agent',current_request_user_agent)


class RandomUserAgentFakeMiddleware(object):

    def __init__(self,crawler):
        super(RandomUserAgentFakeMiddleware,self).__init__()
        self.ua = UserAgent()
        self.ua_type = crawler.settings.get("RANDOM_UA_TYPE",'random')

    @classmethod
    def from_crawler(cls,crawler):
        return cls(crawler)

    def process_request(self,request,spider):
        def get_ua():
            return getattr(self.ua,self.ua_type)

        random_user_agent = get_ua()
        request.headers.setdefault('user-agent',random_user_agent)

