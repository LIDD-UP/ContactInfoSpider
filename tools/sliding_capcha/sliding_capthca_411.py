from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains,ChromeOptions
from PIL import Image
from io import BytesIO
import re

import time

BORDER = 6


class CrackGeetest():
    def __init__(self,url):
        # self.url = 'https://www.411.com/distil_r_captcha.html?requestId=4a6870c4-c650-4434-808d-4ab1fc88a269&httpReferrer=%2Faddress%2F305-W-Rusch-St%2FThorp-WI%2F'
        self.url = url
        option = ChromeOptions()
        option.add_experimental_option('excludeSwitches', ['enable-automation'])
        option.add_argument('--user-data-dir=./chrome_data')
        self.browser = webdriver.Chrome(executable_path=r'C:\Users\18071\PycharmProjects\TruthFinderSpider\tools\sliding_capcha\chromedriver.exe',options=option)
        self.wait = WebDriverWait(self.browser, 10)

    def open(self):
        '''
        打开网页
        :return None
        '''
        self.browser.get(self.url)

    def close(self):
        '''
        关闭网页
        :return None
        '''
        self.browser.close()
        self.browser.quit()

    def change_to_slide(self):
        '''
        切换为滑动认证
        :return 滑动选项对象
        '''
        huadong = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.products-content ul > li:nth-child(2)'))
        )
        return huadong

    def get_geetest_button(self):
        '''
        获取初始认证按钮
        :return 按钮对象
        '''
        button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.geetest_radar_tip'))
        )
        return button

    def wait_pic(self):
        '''
        等待验证图片加载完成
        :return None
        '''
        self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.geetest_wrap'))
        )

    def get_screenshot(self):
        """
        获取网页截图
        :return: 截图对象
        """
        screenshot = self.browser.get_screenshot_as_png()
        screenshot = Image.open(BytesIO(screenshot))
        return screenshot

    def get_position(self):
        '''
        获取验证码位置
        :return: 位置元组
        '''
        img = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'geetest_canvas_img')))
        time.sleep(2)
        location = img.location
        size = img.size
        top, bottom = location['y'], location['y'] + size['height']
        left, right = location['x'], location['x'] + size['width']
        return (top, bottom, left, right)

    def get_slider(self):
        '''
        获取滑块
        :return: 滑块对象
        '''
        slider = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'geetest_slider_button')))
        return slider

    def get_geetest_image(self, name='captcha.png'):
        '''
        获取验证码图片
        :return: 图片对象
        '''
        top, bottom, left, right = self.get_position()
        print('验证码位置', top, bottom, left, right)
        screenshot = self.get_screenshot()
        captcha = screenshot.crop((left, top, right, bottom))
        captcha.save(name)
        return captcha

    def delete_style(self):
        '''
        执行js脚本，获取无滑块图
        :return None
        '''
        js = 'document.querySelectorAll("canvas")[2].style=""'
        self.browser.execute_script(js)

    def is_pixel_equal(self, img1, img2, x, y):
        '''
        判断两个像素是否相同
        :param img1: 不带缺口图片
        :param img2: 带缺口图
        :param x: 位置x
        :param y: 位置y
        :return: 像素是否相同
        '''
        # 取两个图片的像素点
        pix1 = img1.load()[x, y]
        pix2 = img2.load()[x, y]
        threshold = 15
        if abs(pix1[0] - pix2[0]) < threshold \
                and abs(pix1[1] - pix2[1]) < threshold \
                and abs(pix1[2] - pix2[2]) < threshold:
            return True
        else:
            return False

    def get_gap(self, img1, img2):
        '''
        获取缺口偏移量
        :param img1: 不带缺口图片
        :param img2: 带缺口图
        :return 缺口位置
        '''
        left = 63 # 60这个值出现了问题，就是太小了，算出来的不同就是60位置位置，（因为验证码有一个突出的地方刚好是60这个点，但是太大了也不行，如果缺口和图像很近的情况
        for i in range(left, img1.size[0]):
            for j in range(img1.size[1]):
                if not self.is_pixel_equal(img1, img2, i, j):
                    left = i
                    return left
        return left

    def get_track(self, distance):
        '''
        根据偏移量获取移动轨迹
        :param distance: 偏移量
        :return: 移动轨迹
        '''
        # 移动轨迹
        track = []
        # 当前位移
        current = 0
        # 减速阈值
        mid = distance * 3 / 5
        # 计算间隔
        t = 0.2
        # 初速度
        v = 0
        # 滑超过过一段距离
        distance += 15
        while current < distance:
            if current < mid:
                # 加速度为正
                a = 1
            else:
                # 加速度为负
                a = -0.5
            # 初速度 v0
            v0 = v
            # 当前速度 v
            v = v0 + a * t
            # 移动距离 move-->x
            move = v0 * t + 1 / 2 * a * t * t
            # 当前位移
            current += move
            # 加入轨迹
            track.append(round(move))
        return track

    def shake_mouse(self):
        '''
        模拟人手释放鼠标时的抖动
        :return: None
        '''
        ActionChains(self.browser).move_by_offset(xoffset=-3, yoffset=0).perform()
        ActionChains(self.browser).move_by_offset(xoffset=3, yoffset=0).perform()

    def move_to_gap(self, slider, tracks):
        '''
        拖动滑块到缺口处
        :param slider: 滑块
        :param tracks: 轨迹
        :return
        '''
        back_tracks = [-1, -1, -2, -2, -3, -2, -2, -1, -1]
        ActionChains(self.browser).click_and_hold(slider).perform()
        # 正向
        print("正向移动{}".format(sum(tracks)))
        for x in tracks:
            ActionChains(self.browser).move_by_offset(xoffset=x, yoffset=0).perform()
        time.sleep(0.5)
        # 逆向
        print("逆向移动{}".format(sum(back_tracks)))
        print('总的移动距离{}'.format(sum(back_tracks)+sum(tracks)))
        for x in back_tracks:
            ActionChains(self.browser).move_by_offset(xoffset=x, yoffset=0).perform()
        # 模拟抖动
        self.shake_mouse()
        time.sleep(0.5)
        ActionChains(self.browser).release().perform()

    def crack(self):

        # 打开网页
        self.open()
        # 转换验证方式，点击认证按钮
        # s_button = self.change_to_slide()
        time.sleep(1)
        # s_button.click()
        g_button = self.get_geetest_button()
        g_button.click()
        # 确认图片加载完成
        self.wait_pic()
        # 获取滑块
        slider = self.get_slider()
        # 获取带缺口的验证码图片
        image1 = self.get_geetest_image('captcha1.png')
        self.delete_style()
        image2 = self.get_geetest_image('captcha2.png')
        gap = self.get_gap(image1, image2)
        print('缺口位置', gap)
        gap -= BORDER
        print('缺口位置', gap)
        track = self.get_track(gap)

        self.move_to_gap(slider, track)
        print('判断是否验证成功')
        # EC.text_to_be_present_in_element((By.CLASS_NAME, 'geetest_success_radar_tip_content'))
        time.sleep(10) # 等待页面跳转
        current_url = self.browser.current_url
        print(current_url)
        is_success_flag = re.search(r'requestId', current_url)

        if is_success_flag is None:
            print('识别成功')
            time.sleep(5)
        if is_success_flag is not None:
            self.crack()
            time.sleep(5)
        # success = self.wait.until(
        #     EC.text_to_be_present_in_element((By.CLASS_NAME, 'geetest_success_radar_tip_content'), '验证成功')# 这行代码有异常，有时候能够捕获到这个值，有时候不能，可能原因就是这个值存在时间不长，可能在页面跳转之后就无法捕获了，所以应该判断，跳转之后的页面。
        # )

        # self.close()


if __name__ == '__main__':
    url = "https://www.411.com/distil_r_captcha.html?requestId=00ad03b0-b923-4025-aba0-a00f9da3fcb5&httpReferrer=%2Faddress%2F121-Clubhouse-Rd%2FBeech-Mountain-NC%2F"
    crack = CrackGeetest(url=url)
    crack.crack()
    # image1 = Image.open('./captcha1.png')
    # image2 = Image.open('./captcha2.png')
    #
    # gap = crack.get_gap(image1, image2)
    # print(gap)

    # 在验证中出现的情况，
    # 1：出现怪兽吃掉拼图，
    #2：出现缺口和拼图很近，left偏移量太大了，
    # 3：返回的距离不够。 可以通过调整border值，出现的次数较多


    # 之前是没有加border的情况，现在加boreder并且设置成为5；这种情况下差距太大的影响不是很大
    # 如果差距大于3，匹配就不能成功，只能在1-2的偏移量的时候才能成功
    # 有时候会出现偏移量的滑动很接近，但是会出现小怪兽的情况，所以说最好出现1，2的误差才行，
    # 设置成为5的情况很多时候会出现差距太大，很容易出现3，和出现刚好重合的情况，所以最好设置成为










