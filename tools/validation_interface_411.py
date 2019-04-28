import requests
headers = {
'authority': 'www.411.com',
'method': 'GET',
'path': '/address/1117-Karluk-St-Apt-2/Anchorage-AK',
'scheme': 'https',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'zh-CN,zh;q=0.9',
'cache-control': 'no-cache',
'cookie': 'D_IID=60EFD30F-FEBC-3367-95BA-CAE6387DEAA4; D_UID=EEE60161-24BA-3A3D-AC13-1AAEE0433529; D_ZID=D4F8BEDB-63FD-3F9F-9943-C9307BAED189; D_ZUID=EFA7A7E3-D90D-3E00-92FC-17C06D254236; D_HID=C5A52DB9-4D71-3C51-86D9-670A8E314E0F; D_SID=104.192.81.202:kpLT9NOpZk2Gcs3Uglunf+/GwcSyZkLbqOMiaWUvIQU; wp_pid=c87829612f2748996c9468c7a1aa116a; initial_referrer=http%3A%2F%2F411.com%2F; initial_referring_domain=411.com; device_id=9b443a0a-ed3c-4f31-a41e-96bb884b5028R; _ga=GA1.2.819839102.1555392578; _gid=GA1.2.349130287.1555392578; __gads=ID=95798f01b2b9fe27:T=1555392579:S=ALNI_MbX3AQzLdMY1RJHokgOjbBkWjLDOA; __qca=P0-2031199324-1555392578816; OX_plg=pm; ewp=68; wp_endemic_provider=E; eb=68; weekly_count=%5B%7B%22searched_date%22%3A%2220190415%22%2C%22value%22%3A4%7D%2C%7B%22searched_date%22%3A%2220190416%22%2C%22value%22%3A1%7D%5D; _411_session=WEVhbUlGOWVWZ051NWwxOWovQzJiT0NKNTd6ZnJ2K2tIZldHT0dpb0l3MUw5TEpyZjJOMUx5by9teEVoRVhEVGgwZGx2Ym1TY2JudlVNeElIM2hlR0J4dFQwSUVpZzNwMnMraW9hQVJVdDFMcFc0N2RWdVltT2dSWkt3NHRWbVVVMzBrRzZNcmhXU25MVVV1WFRYWHlRPT0tLTN4cExlcEtHSjlib3A0cllFaTNxZlE9PQ%3D%3D--34ca5f22ce17668e0f9c88672cc3ea90ea166230; amplitude_id_4452f969da1962f05527ab14f5db83da_premium_api411.com=eyJkZXZpY2VJZCI6IjliNDQzYTBhLWVkM2MtNGYzMS1hNDFlLTk2YmI4ODRiNTAyOFIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTU1NTQwMDk5MDM5NCwibGFzdEV2ZW50VGltZSI6MTU1NTQwNDAyNDIzMiwiZXZlbnRJZCI6NDUsImlkZW50aWZ5SWQiOjQ1LCJzZXF1ZW5jZU51bWJlciI6OTB9',
'pragma': 'no-cache',
'referer': 'https://www.411.com/address/1117-Karluk-St/Anchorage-AK',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
}


req = requests.get(url ='https://www.411.com/address/1117-Karluk-St-Apt-2/Anchorage-AK/',headers=headers )
with open('411.html','w') as f:
    f.write(req.text)