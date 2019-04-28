from urllib import parse, request
import json
import os
from TruthFinderSpider.settings import SPIDER_411_URLS_FILE
from TruthFinderSpider.settings import EMAIL_SETTING
from TruthFinderSpider.settings import START_URL_FROM_URL
import smtplib
from email.mime.text import MIMEText
import pandas as pd
import logging


def start():
    if not os.path.exists(SPIDER_411_URLS_FILE):
        print('url文件不存在,查询数据进行爬取')
        write_url_to_csv()
    if os.path.exists(SPIDER_411_URLS_FILE):
        print('url文件准备完毕，开始执行爬虫')
        os.system("scrapy crawl spider_411")
        # os.system("conda activate tensorflow && scrapy crawl SearchBug")
        print('爬虫执行完毕，再次查询数据进行执行爬虫')
        # start()


def send_email(title='', content=''):
    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = EMAIL_SETTING['from_name']
    message['To'] = ','.join(EMAIL_SETTING['to'])
    message['Subject'] = EMAIL_SETTING['subject'] + title
    smtp_obj = smtplib.SMTP_SSL(EMAIL_SETTING['smtp'], EMAIL_SETTING['smtp_port'])
    smtp_obj.login(EMAIL_SETTING['username'], EMAIL_SETTING['password'])
    smtp_obj.sendmail(EMAIL_SETTING['username'], EMAIL_SETTING['to'], message.as_string())
    print('mail has been send successfully.')


def get_json_data_from_server():
    req = request.Request(START_URL_FROM_URL)
    post_data = {
        "spiderFrom": "truthfinder",
        "limit": 300
    }
    data = parse.urlencode(post_data).encode(encoding='utf-8')
    opener = request.build_opener(request.HTTPCookieProcessor())
    resp = opener.open(req, data, timeout=500)
    res = resp.read()
    result = res.decode(encoding='utf-8')
    result = json.loads(str(result))
    return result


def write_url_to_csv():
    data = get_json_data_from_server()
    url_pattern2 = 'https://www.411.com/address/{address}/{city_state}/'
    list_url = [url_pattern2.format(address='-'.join(info['address'].replace('#', 'apt').split(' ')),
                                    city_state='-'.join(info['city'].split(' ')) + '-' + info['state']) for info in
                data]
    url_df = pd.DataFrame()
    url_df['search_url'] = list_url
    address = [info['address'] + ',' + info['city'] + ',' + info['state'] + info['zipCode'] for info in data]
    masterContactId = [info['id'] for info in data]
    url_df['address'] = address
    url_df['address_id'] = masterContactId
    url_df.to_csv(SPIDER_411_URLS_FILE, index=False)


if __name__ == '__main__':
    start()