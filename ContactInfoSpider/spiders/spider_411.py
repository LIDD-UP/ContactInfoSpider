# -*- coding: utf-8 -*-
import scrapy
import pandas as pd
from TruthFinderSpider.settings import SPIDER_411_URLS_FILE
from TruthFinderSpider.spider_411_custom_settings import spider_411_custom_settings
from TruthFinderSpider.items import ContactInfoJsonItem
import datetime
from TruthFinderSpider.settings import MY_USER_AGENTS
import re



class Spider411Spider(scrapy.Spider):
    name = 'spider_411'
    allowed_domains = ['411.com']
    custom_settings = spider_411_custom_settings

    true_scrapy_start_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    true_scrapy_start_time = datetime.datetime.strptime(true_scrapy_start_time, '%Y-%m-%d %H:%M:%S')
    scrapy_start_time = true_scrapy_start_time

    spider_user_agent = MY_USER_AGENTS

    def start_requests(self):

        search_url  = list(pd.read_csv(SPIDER_411_URLS_FILE).values)
        for info in search_url:
            address_id = info[2]
            yield scrapy.Request(url=info[0], meta={'address_id': address_id}, callback=self.parse)

    # def __init__(self):
    #     super(Spider411Spider, self).__init__()
    #     self.selenium_browser =

    def parse(self, response):
        # with open('./response_spider_411.html','w') as f:
        #     f.write(response.text)

        # 加一下判断是否还有后续的页面
        each_address_info_list = []
        address_id = response.meta['address_id']
        address_middle = response.xpath('//div[contains(@class,"module")]/div[contains(@class,"section-content")]//text()').extract()
        address = ','.join([x.replace('\n','').strip() for x in address_middle if len(re.findall(r'\w',x)) != 0])

        persons = response.xpath('//ul[contains(@class,"person-card-list")]/li')
        if persons is not None:
            for person in persons:
                name = ""
                name_middle = person.xpath('./a/p[contains(@class,"assoicated-link-title")]/text()').extract_first()
                if name_middle is not None:
                    name = name_middle.replace('\n','').strip()
                age = 0
                age_middle = person.xpath('./a/p[contains(@class,"clearfix")]/text()').extract_first()
                if age_middle is not None:
                    age = re.search(r'\d+',age_middle)
                    if age is not None:
                        age = age.group()
                    if age is None:
                        age = 0


                address = address
                phone = ""
                json_result = '{"masterContactId":%s, "name":"%s", "age": %s, "address": "%s", ' \
                              '"phone":"%s"}' % (address_id, name, age, address, phone)
                each_address_info_list.append(json_result)
            contact_info = ContactInfoJsonItem()
            contact_info['contactData'] = each_address_info_list
            contact_info['addressId'] = address_id
            yield contact_info
        if persons is None:
            contact_info = ContactInfoJsonItem()
            contact_info['contactData'] = []
            contact_info['addressId'] = address_id
        pass



