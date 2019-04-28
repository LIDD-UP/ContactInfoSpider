import json

our_cookie='D_IID=32CFDAE8-B684-3FC1-81A3-94F7BDD1CAE0; D_UID=85FEA9F7-DC88-3D18-B216-FA29881BC4CD; D_ZID=7C189B9D-49CF-3462-AF13-945DDB03B9A7; D_ZUID=1AF99673-E77E-3A80-9624-F42DC8FE82B9; D_HID=57974DC0-DCC7-3806-BCBD-72529CF3E565; D_SID=103.101.177.248:6tnDK41XIhyhhVdnt1zvzuxXO3OmKDSq6VnhLuxqmco; wp_pid=b4b97584bd521b8781a7215f40e34bfb; initial_referrer=; initial_referring_domain=; device_id=f22fca86-ff2a-4cea-ab3a-d6b13059ae29R; __gads=ID=1917b5b8836ae2f2:T=1556244688:S=ALNI_MakZmZZKsU2qLT3CeCSaXs8yvQjyg; _ga=GA1.2.427249897.1556244688; _gid=GA1.2.894580025.1556244696; _pubcid=8392935a-bb9f-4864-8dc8-f5a41d131fae; __qca=P0-502956382-1556244698411; OX_plg=pm; _411_session=WE45SWZvazdkYzYxQ3c5MHpFd0JqOWtaLzAyK1hmMkpWZlhUVDZtb1RKa0t6Y3dYMmRLMzRGRG5LK0VNdmRlVFo4WEFHaVJ6MDNBcmppNm9RZ1FiNjhQVFNJb1huY3BUMnBqTlBRQUx2NkFCVmhpZTRZV1ZpRG9sM0lVa2dPbFE0TW9jMHJBcUxvaVc4aFlqaFNQU2xnPT0tLW9jL1c5MVB4OFE5NmFUNmZUdXBWQWc9PQ%3D%3D--90506b732ddfabb836b9e33097507cd5cf1cb4cd; amplitude_id_4452f969da1962f05527ab14f5db83da_premium_api411.com=eyJkZXZpY2VJZCI6ImYyMmZjYTg2LWZmMmEtNGNlYS1hYjNhLWQ2YjEzMDU5YWUyOVIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTU1NjI0NDY4NTgzOSwibGFzdEV2ZW50VGltZSI6MTU1NjI0NDk0MTI1NiwiZXZlbnRJZCI6MywiaWRlbnRpZnlJZCI6Mywic2VxdWVuY2VOdW1iZXIiOjZ9'
# our_cookie_list = our_cookie.replace(';',',').replace('=',':')
# our_cookie_list_json = json.dumps(our_cookie_list)
# our_cookie_dict = json.loads(json.loads(our_cookie_
# list_json))
# print(type(our_cookie_dict))
# #
# print(our_cookie_dict)
# print()

def generate_cookie_info(cookie_str):
    our_cookie_list = our_cookie.replace(' ','').split(';')
    new_dict = {}
    for info in our_cookie_list:
        print(info)
        new_dict[info.split('=')[0]] = info.split('=')[1]
    print(new_dict)
    # new_cookie = [new_dict]

    # cookie_json = json.dumps(new_cookie)
    return new_dict


if __name__ == "__main__":
    pass
    # cookie = generate_cookie_info(our_cookie)
#     # print(cookie)
#     # print(type(cookie))
#     #
#     # a = {'D_IID': '32CFDAE8-B684-3FC1-81A3-94F7BDD1CAE0', 'D_UID': '85FEA9F7-DC88-3D18-B216-FA29881BC4CD', 'D_ZID': '7C189B9D-49CF-3462-AF13-945DDB03B9A7', 'D_ZUID': '1AF99673-E77E-3A80-9624-F42DC8FE82B9', 'D_HID': '57974DC0-DCC7-3806-BCBD-72529CF3E565', 'D_SID': '103.101.177.248:6tnDK41XIhyhhVdnt1zvzuxXO3OmKDSq6VnhLuxqmco', 'wp_pid': 'b4b97584bd521b8781a7215f40e34bfb', 'initial_referrer': '', 'initial_referring_domain': '', 'device_id': 'f22fca86-ff2a-4cea-ab3a-d6b13059ae29R', '__gads': 'ID', '_ga': 'GA1.2.427249897.1556244688', '_gid': 'GA1.2.894580025.1556244696', '_pubcid': '8392935a-bb9f-4864-8dc8-f5a41d131fae', '__qca': 'P0-502956382-1556244698411', 'OX_plg': 'pm', '_411_session': 'WE45SWZvazdkYzYxQ3c5MHpFd0JqOWtaLzAyK1hmMkpWZlhUVDZtb1RKa0t6Y3dYMmRLMzRGRG5LK0VNdmRlVFo4WEFHaVJ6MDNBcmppNm9RZ1FiNjhQVFNJb1huY3BUMnBqTlBRQUx2NkFCVmhpZTRZV1ZpRG9sM0lVa2dPbFE0TW9jMHJBcUxvaVc4aFlqaFNQU2xnPT0tLW9jL1c5MVB4OFE5NmFUNmZUdXBWQWc9PQ%3D%3D--90506b732ddfabb836b9e33097507cd5cf1cb4cd', 'amplitude_id_4452f969da1962f05527ab14f5db83da_premium_api411.com': 'eyJkZXZpY2VJZCI6ImYyMmZjYTg2LWZmMmEtNGNlYS1hYjNhLWQ2YjEzMDU5YWUyOVIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTU1NjI0NDY4NTgzOSwibGFzdEV2ZW50VGltZSI6MTU1NjI0NDk0MTI1NiwiZXZlbnRJZCI6MywiaWRlbnRpZnlJZCI6Mywic2VxdWVuY2VOdW1iZXIiOjZ9'}
#     #
#     # for k,v in cookie.items():
#     #     print(k+':'+v)
#     our_cookie = {
#         "name": 'test',
#         "value": "test",
#         "name": 'test1',
#         "value": "test2",
#         "domain": '411.com',
#         # "path": '/',
#         "httpOnly": True,
#         "secure": True
#     }
#     print(our_cookie)