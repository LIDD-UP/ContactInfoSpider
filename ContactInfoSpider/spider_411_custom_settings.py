spider_411_custom_settings = {
        "ITEM_PIPELINES": {
            # 'TruthFinderSpider.pipelines.TruthFinderContactInfoPipeline': 301,
            'TruthFinderSpider.pipelines.TruthFinderContactInfoMysqlPipeline': 302,


        },
        "DOWNLOADER_MIDDLEWARES": {
            # 'TruthFinderSpider.middlewares.RandomUserAgentMiddleware':1,
            # 'TruthFinderSpider.middlewares.RandomUserAgentFakeMiddleware':1,
            'TruthFinderSpider.middlewares.Spider411TimeToStopMiddleware':545,

        },
        "SPIDER_MIDDLEWARES": {
            # 'TruthFinderSpider.middlewares.TruthfinderspiderCloseSpiderMiddleware':550,
        },

        "DEFAULT_REQUEST_HEADERS": {
            'authority': 'www.411.com',
            'method': 'GET',
            # 'path': '/address/1117-Karluk-St-Apt-2/Anchorage-AK',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'no-cache',
            'cookie': 'D_IID=60EFD30F-FEBC-3367-95BA-CAE6387DEAA4; D_UID=EEE60161-24BA-3A3D-AC13-1AAEE0433529; D_ZID=D4F8BEDB-63FD-3F9F-9943-C9307BAED189; D_ZUID=EFA7A7E3-D90D-3E00-92FC-17C06D254236; D_HID=C5A52DB9-4D71-3C51-86D9-670A8E314E0F; D_SID=104.192.81.202:kpLT9NOpZk2Gcs3Uglunf+/GwcSyZkLbqOMiaWUvIQU; wp_pid=048e1cf64b4fff290fb7e801916bdfdf; _411_session=bGUzL3pJTDU0aW9xS3FuVEZXRitPblNZT0poSjJvV2Z6SnJTRXhNMmU4Wnk0U1h1NGxJTmlZblFUWDlJRjRRM0YrczBJTzdGMHVLYk9xbk5LQjJ1Q2NJWkFoNTNScWp1cDBEcUtJWTBqczFrczV2ZHIyWnhXSklSUHVzNDZJZWVEcTM1UWxXdFltUElwNm5GSkRTZ3NBPT0tLWdQSEFMRFliL29DWjVFSkZtV2w0S2c9PQ%3D%3D--86a928203acba562a4411b40b9a327d0a457b85e; initial_referrer=; initial_referring_domain=; device_id=d544913c-76db-4e78-b181-f7e5f63304d7R; amplitude_id_4452f969da1962f05527ab14f5db83da_premium_api411.com=eyJkZXZpY2VJZCI6ImQ1NDQ5MTNjLTc2ZGItNGU3OC1iMTgxLWY3ZTVmNjMzMDRkN1IiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTU1NjQzMjcxMDU2NSwibGFzdEV2ZW50VGltZSI6MTU1NjQzMjcxMTAxOCwiZXZlbnRJZCI6MSwiaWRlbnRpZnlJZCI6MSwic2VxdWVuY2VOdW1iZXIiOjJ9; _ga=GA1.2.1402559380.1556432712; _gid=GA1.2.618129759.1556432712; _gat=1; __gads=ID=afc3222e3479b004:T=1556432712:S=ALNI_MZFc4yTP7qjgV9y5FKzxfv9DYWqkw; __qca=P0-682910557-1556432712986; OX_plg=pm',

            'pragma': 'no-cache',
            # 'referer': 'https://www.411.com/address/1117-Karluk-St/Anchorage-AK',
            'upgrade-insecure-requests': '1',
            # 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
            'user-agent':'Mozilla/5.0 (X11; CrOS i686 13.587.48) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.43 Safari/535.1',
        },
        "COOKIES_ENABLED": False,
        # "REDIRECT_ENABLED": False,
        # "REFERER_ENABLED": False,
        # "RETRY_ENABLED": False,
        "CONCURRENT_REQUESTS":  1,
        "HTTPERROR_ALLOWED_CODES": [403,404,405,416],


        "REACTOR_THREADPOOL_MAXSIZE": 100,
        "CONCURRENT_REQUESTS_PER_DOMAIN": 1,

        # "LOG_FILE": "realtor_log.txt",
        # "LOG_LEVEL": 'ERROR',

    }




