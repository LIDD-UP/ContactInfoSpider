from urllib import parse, request
import json
import os

import smtplib
from email.mime.text import MIMEText
import pandas as pd
ROOT_URL = "http://138.197.143.39:8081/AmericaContactDataSave/"
# ROOT_URL = "http://localhost:8081/AmericaContactDataSave/"
START_URL_FROM_URL = ROOT_URL + "index/querySearchBugSpiderData"


def get_json_data_from_server():
    req = request.Request(START_URL_FROM_URL)
    post_data = {
        "spiderFrom": "searchbug",
        "limit": 300
    }
    data = parse.urlencode(post_data).encode(encoding='utf-8')
    opener = request.build_opener(request.HTTPCookieProcessor())
    resp = opener.open(req, data, timeout=60)
    res = resp.read()
    result = res.decode(encoding='utf-8')
    result = json.loads(str(result))
    return result


def spider_411_data_format(data):
    url_pattern2 = 'https://www.411.com/address/{address}/{city_state}/'
    list_url = [url_pattern2.format(address='-'.join(info['address'].replace('#','apt').split(' ')),city_state='-'.join(info['city'].split(' '))+'-'+info['state']) for info in data]
    url_df = pd.DataFrame()
    url_df['search_url'] = list_url
    address = [info['address']+','+info['city'] +','+ info['state']+info['zipCode'] for info in data]
    masterContactId = [info['id'] for info in data]
    url_df['address'] = address
    url_df['address_id'] = masterContactId
    url_df.to_csv('./spider_411_url2.csv', index=False)
    pass


def get_truth_finder_url(dict_data):
    # url_partern = 'https://www.truthfinder.com/address-lookup/nj/toms-river/route-37-w-%23/1228/'
    url_partern2 = 'https://www.truthfinder.com/address-lookup/{province_code}/{city}/{street}/{number}/?zip={zipcode}&search=true'
    list_url = [url_partern2.format(number=info['address'].split(' ')[0],street='-'.join(info['address'].replace('#','%23').split(' ')[1:]),city='-'.join(info['city'].split(' ')),province_code=info['state'].lower(),zipcode=info['zipCode']).lower() for info in data]
    url_df = pd.DataFrame()
    url_df['search_url'] = list_url
    address = [info['address']+','+info['city'] +','+ info['state']+info['zipCode'] for info in data]
    masterContactId = [info['id'] for info in data]
    url_df['address'] = address
    url_df['address_id'] = masterContactId

    url_df.to_csv('./truth_finder_url_new.csv',index=False)




def generate_url_from_dict_data(dict_data):
    pass


if __name__ == "__main__":
    url_pattern1 = 'https://www.truthfinder.com/address/1117-karluk-street/anchorage/ak/99501/'
    url_pattern3 = 'https://www.truthfinder.com/address/{address}/{city}/{province_code}/{zipcode}/'

    data = get_json_data_from_server()
    print('获取数据成功')



    spider_411_data_format(data)
    # get_truth_finder_url(data)



    # for info in data:
    #     print(info['address'])





