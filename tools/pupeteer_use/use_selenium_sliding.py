# --user-data-dir


from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from PIL import Image
from io import BytesIO
import time
from selenium.webdriver import ChromeOptions
option = ChromeOptions()

def open_page(url):
    # self.url = 'https://www.411.com/distil_r_captcha.html?requestId=4a6870c4-c650-4434-808d-4ab1fc88a269&httpReferrer=%2Faddress%2F305-W-Rusch-St%2FThorp-WI%2F'

    option = ChromeOptions()
    # option.add_argument('--user-data-dir=C:\\Users\\18071\\AppData\\Local\\Google\\Chrome\\User Data\\Default')
    option.add_argument('--user-data-dir=./chrome_data')
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    browser = webdriver.Chrome(executable_path=r'C:\Users\18071\PycharmProjects\TruthFinderSpider\tools\sliding_capcha\chromedriver.exe',options=option)
    # browser.execute_script('(() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) })()')
    browser.get(url=url)
    wait = WebDriverWait(browser, 10)
    time.sleep(10000)



if __name__ =="__main__":
    # url1 = 'https://www.411.com/address/360-Club-Dr/Sapphire-NC/'
    url2 = 'https://www.411.com/distil_r_captcha.html?requestId=71e50caa-7adb-47d8-9f44-6bf641abb6d6&httpReferrer=%2Faddress%2F3124-Buffalo-Nvno%2FZionville-NC%2F'
    open_page(url=url2)
