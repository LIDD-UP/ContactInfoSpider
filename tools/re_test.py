import re
url1 = 'https://www.411.com/distil_r_captcha.html?requestId=00ad03b0-b923-4025-aba0-a00f9da3fcb5&httpReferrer=%2Faddress%2F121-Clubhouse-Rd%2FBeech-Mountain-NC%2F'
url2 = 'https://www.411.com/address/160-Rocky-Creek-Rd/Sapphire-NC/6xVKiIatftqqO9CEvDahpJ'

a = re.search(r'requestId',url2)
print(a)


