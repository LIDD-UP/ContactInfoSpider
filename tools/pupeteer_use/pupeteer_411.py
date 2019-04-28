import asyncio
from pyppeteer import launch
import json

width, height = 1366, 768

coo='D_IID=32CFDAE8-B684-3FC1-81A3-94F7BDD1CAE0; D_UID=85FEA9F7-DC88-3D18-B216-FA29881BC4CD; D_ZID=7C189B9D-49CF-3462-AF13-945DDB03B9A7; D_ZUID=1AF99673-E77E-3A80-9624-F42DC8FE82B9; D_HID=57974DC0-DCC7-3806-BCBD-72529CF3E565; D_SID=103.101.177.248:6tnDK41XIhyhhVdnt1zvzuxXO3OmKDSq6VnhLuxqmco; wp_pid=b4b97584bd521b8781a7215f40e34bfb; initial_referrer=; initial_referring_domain=; device_id=f22fca86-ff2a-4cea-ab3a-d6b13059ae29R; __gads=ID=1917b5b8836ae2f2:T=1556244688:S=ALNI_MakZmZZKsU2qLT3CeCSaXs8yvQjyg; _ga=GA1.2.427249897.1556244688; _gid=GA1.2.894580025.1556244696; _pubcid=8392935a-bb9f-4864-8dc8-f5a41d131fae; __qca=P0-502956382-1556244698411; OX_plg=pm; _411_session=WE45SWZvazdkYzYxQ3c5MHpFd0JqOWtaLzAyK1hmMkpWZlhUVDZtb1RKa0t6Y3dYMmRLMzRGRG5LK0VNdmRlVFo4WEFHaVJ6MDNBcmppNm9RZ1FiNjhQVFNJb1huY3BUMnBqTlBRQUx2NkFCVmhpZTRZV1ZpRG9sM0lVa2dPbFE0TW9jMHJBcUxvaVc4aFlqaFNQU2xnPT0tLW9jL1c5MVB4OFE5NmFUNmZUdXBWQWc9PQ%3D%3D--90506b732ddfabb836b9e33097507cd5cf1cb4cd; amplitude_id_4452f969da1962f05527ab14f5db83da_premium_api411.com=eyJkZXZpY2VJZCI6ImYyMmZjYTg2LWZmMmEtNGNlYS1hYjNhLWQ2YjEzMDU5YWUyOVIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTU1NjI0NDY4NTgzOSwibGFzdEV2ZW50VGltZSI6MTU1NjI0NDk0MTI1NiwiZXZlbnRJZCI6MywiaWRlbnRpZnlJZCI6Mywic2VxdWVuY2VOdW1iZXIiOjZ9'

# def generate_cookie_info(cookie_str):
#     our_cookie_list = cookie_str.replace(' ', '').split(';')
#     new_dict = {}
#     for info in our_cookie_list:
#         print(info)
#         new_dict[info.split('=')[0]] = info.split('=')[1]
#     print(new_dict)
#     # new_cookie = [new_dict]
#
#     # cookie_json = json.dumps(new_cookie)
#     return new_dict


# our_cookie_dict = generate_cookie_info(coo)


# def format_cookie(k,v):
# our_cookie = {
#     "name":'cookie',
#     "value":"{value}".format(value=coo),
#     "domain": '411.com',
#     "httpOnly": True,
#     "secure": True
# }
# return our_cookie


async def main():
    browser = await launch(headless=False,
                           devtools=True,
                           args=[f'--window-size={width},{height}','--disable-infobars',
                                 # '--proxy-server=127.0.0.1:8080'

                                 ],
                           userDataDir="./data",
                           )
    page = await browser.newPage()
    await page.setViewport({'width': width, 'height': height})
    # async for k,v in our_cookie_dict:
    #     our_cookie = await format_cookie(k,v)
    # await page.setCookie(our_cookie)
    await page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36')


    await page.goto('https://www.411.com/distil_r_captcha.html?requestId=2e3060d5-176f-4508-95d2-b18267b698d4&httpReferrer=%2Faddress%2F225-Stone-Hill-Dr%2FPenrose-NC%2F',timeout=1000000)
    # await page.goto('https://www.411.com/address/3627-N-19th-St/Philadelphia-PA/', timeout=1000000)
    # await page.evaluate(
    #     '''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')

    await asyncio.sleep(1000)

asyncio.get_event_loop().run_until_complete(main())




