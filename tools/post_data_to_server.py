import json
from urllib import parse, request
import json
from TruthFinderSpider.settings import SAVE_DATA_URL
from tools import get_sql_con
from TruthFinderSpider.items import ContactInfoJsonItem


def post_url( url, insert_item):
    contact_list = []
    # for new_item in insert_item:
    for row in insert_item["contactData"]:
        print(type(json.loads(row)))
        # contact_list.append(json.loads(row))
        contact_list.append(json.dumps(json.loads(row)))
    post_data = {
        "resultData": contact_list,
        "spiderFrom": "truthfinder"
    }

    data = post_data
    req = request.Request(url)
    data = parse.urlencode(data).encode(encoding='utf-8')
    opener = request.build_opener(request.HTTPCookieProcessor())
    resp = opener.open(req, data)
    res = resp.read()
    return res.decode(encoding='utf-8')


if __name__ == "__main__":
    data_dict = {
	'addressId': 234120,
	'contactData': ['{"masterContactId":234120, "name":"Carrie Baker ", "age": '
		'47, "address": "792 42nd St Sw,Loveland, COLORADO 80537", '
		'"phone":""}',
		'{"masterContactId":234120, "name":"Edmund R. Kahle ", "age": '
		'67, "address": "792 42nd St Sw,Loveland, COLORADO 80537", '
		'"phone":""}'
	]
    }


    for row in data_dict["contactData"]:
        print(type(row))
        print(row)
    a = post_url(SAVE_DATA_URL,data_dict)
    print(a)