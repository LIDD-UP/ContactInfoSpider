import requests
import pandas as pd
import re
import json
headers = {
'authority': 'www.truthfinder.com',
'method': 'GET',
# 'path': '/address/1117-karluk-street/anchorage/ak/99501/',
'scheme': 'https',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'zh-CN,zh;q=0.9',
'cache-control': 'no-cache',
# 'cookie': '__cfduid=dd8fde4a3b8cf83c11ce01c109122f3d91555392252; PHPSESSID=kdk3qtqmo6pk7rprn11ph92vb3; _gcl_au=1.1.218817212.1555392254; _ga=GA1.2.257191145.1555392254; _gid=GA1.2.1206418053.1555392254; spid=DA577A99-D14E-4DB3-ACAE-437F030DDE46; sp_apnxid=7836183178481518710; _fbp=fb.1.1555392397836.545440278; __ssid=9898f423feddf47379a2dbfa1b07316; warningModalPopped=true; __uzma=a1fff3b6-eda0-4ac2-bc90-1bec55fd6686; __uzmb=1555393952; qualityScore=97.14999999999999; sp_ssid=1555396850130; AMP_TOKEN=%24NOT_FOUND; language=en_US; session-set=true; amazon-pay-abtesting-new-widgets=true; amazon-pay-connectedAuth=connectedAuth_general; amazon-pay-abtesting-apa-migration=true; guidelinesModalPopped=true; __uzmc=817931622160; uzdbm_a=e6418a42-9f82-c2a7-1cda-7c772cc17e3a; __uzmd=1555397164; sp_sync_ssid=1555398156573',
'pragma': 'no-cache',
'referer': 'https://www.truthfinder.com/address-lookup/',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
}

# url1 = 'https://www.truthfinder.com/address/l38-b10-laurel-st/anchorage/ak/99515/'
# url2 = 'https://www.truthfinder.com/address/1117-karluk-street/anchorage/ak/99501/'
# req = requests.get(url =url2,headers=headers )
# with open('truthfinder.html','w') as f:
#     f.write(req.text)


data = pd.read_html('./truthfinder.html')
# print(data[0].columns)
# print(len(data))
# print(data)

# print(data[0].values[0:1,:])
# print(len(data[0].values[1,:]))
list_data = data[0].values

response_url = 'https://www.truthfinder.com/address/1117-karluk-street/anchorage/ak/99501/'





# for i in range(10):
#     name = list_data[i,0] .split('Possible Aliases:')[0]
#     age = list_data[i,1]
#     address = re.findall(r'address/(.*)',response_url)[0].replace('-',' ').replace('/',',').rstrip(',')
#     phone = ''
#
#     print(address)


def data_analysis(data,response_url):
    for i in range(len(data)):
        name = data[i, 0].split('Possible Aliases:')[0]
        age = data[i, 1]
        print('type:',type(age))
        if pd.isna(age):
            print('............................')
            age = 0
        if age =='nan':
            print('............................')
            age = 0
        address = re.findall(r'address/(.*)', response_url)[0].replace('-', ' ').replace('/', ',').rstrip(',')
        phone = ''
        # print(address)

        json_result = '{"masterContactId":%s, "name":"%s", "age": %s, "address": "%s", ' \
                      '"phone":"%s"}' % (111, name, age, address, phone)

        print(json_result)

        json_result_dict = json.loads(json_result)
        print(json_result_dict)



data_analysis(list_data,response_url)