import requests


headers = {
# "x-d-token": "3.AR7Z2f3QNH-18D4LCtQY9TKVrZ1k-Pm9c9q6ldbnP6v9EUuJQUqbgnxxWQMoUZuhRGwBAK_Si3y3Qx8xUOL7IRVIBQpDULq5OMp-xZUZ-wX6ZWs-KBCjVq-ojeulFJFOkJsYzkLQm8DBASmiXxgTPMurId1dkbCY2AqrK4W0ZFVnrTeYKntLJ8EwgXsqaTXGwyVKFR1UfFk2T2NEpqX5V-CaaJmf8Fgxv42dCyWiUqPOC-QfNbqevu9M7idrg0WoPpxmkupc7GWFDi7pBz5TgGH8G2BuE-bBPVx8JZiNh88qBItl2He2vwosY8YVIUF3HXhAu0jK8zfq_BEJ9cxTZz0v9sbxBWaZuyTG90ixZxjT_Q==.h-C31J2N-coAAAJY",
# "x-d-token": "3.AR7Z2f3QNH-18D4LCtQY9TKVrZ1k-Pm9c9q6ldbnP6v9EUuJQUqbgnxxWQMoUZuhRGwBAK_Si3y3Qx8xUOL7IRVIBQpDULq5OMp-xZUZ-wX6ZWs-KBCjVq-ojeulFJFOkJsYzkLQm8DBASmiXxgTPMurId1dkbCY2AqrK4W0ZFVnrTeYKntLJ8EwgXsqaTXGwyVKFR1UfFk2T2NEpqX5V-CaaJmf8Fgxv42dCyWiUqPOC-QfNbqevu9M7idrg0WoPpxmkupc7GWFDi7pBz5TgGH8G2BuE-bBPVx8JZiNh88qBItl2He2vwosY8YVIUF3HXhAu0jK8zfq_BEJ9cxTZz0v9sbxBWaZuyTG90ixZxjT_Q==.pAT1D4c4nScAAAJY",
# "Host": "app.whitepages.com",
# "Connection": "Keep-Alive",
"Accept-Encoding": "gzip",
# "User-Agent": "okhttp/3.9.1"

}
# url='https://app.whitepages.com/api/v4/search?input=4324%20Page%20Pl&type=address&where=Loveland%2CCO80537&device_id=1b46d83f68dad320&client_id=aN3cN&version=339'
url = 'https://www.baidu.com'
rs = requests.get(url=url,headers=headers, verify=False)
print(rs.text)

s