from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from PIL import Image
from io import BytesIO
import time

def open_page(url):
    # self.url = 'https://www.411.com/distil_r_captcha.html?requestId=4a6870c4-c650-4434-808d-4ab1fc88a269&httpReferrer=%2Faddress%2F305-W-Rusch-St%2FThorp-WI%2F'

    browser = webdriver.Chrome(executable_path=r'C:\Users\18071\PycharmProjects\TruthFinderSpider\tools\sliding_capcha\chromedriver.exe')
    browser.get(url=url)
    wait = WebDriverWait(browser, 10)
    time.sleep(10000)


# if __name__ == "__main__":
#     url = 'https://www.baidu.com'
#     open_page(url)

from selenium.webdriver import ChromeOptions

option = ChromeOptions()
option.add_argument("--proxy-server=127.0.0.1:8080")

option.add_experimental_option('excludeSwitches', ['enable-automation'])

url = 'https://login.taobao.com/member/login.jhtml?redirectURL=https://www.taobao.com/'

browser = webdriver.Chrome(executable_path=r'C:\Users\18071\PycharmProjects\TruthFinderSpider\tools\sliding_capcha\chromedriver.exe',options=option)


browser.get(url=url)
browser.execute_script('(() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) })()')
# wait = WebDriverWait(browser, 10)
# time.sleep(10000)


