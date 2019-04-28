
# 第一版本
# import asyncio
# from pyppeteer import launch
#
# async def main():
#     browser = await launch(headless=False)
#     page = await browser.newPage()
#     await page.goto('https://www.taobao.com')
#     await asyncio.sleep(1000)
#
# asyncio.get_event_loop().run_until_complete(main())


# 解决浏览器比内容大的问题

# import asyncio
# from pyppeteer import launch
#
# width, height = 1366, 768
#
# async def main():
#     browser = await launch(headless=False,
#                            args=[f'--window-size={width},{height}'])
#     page = await browser.newPage()
#     await page.setViewport({'width': width, 'height': height})
#     await page.goto('https://www.taobao.com')
#     await asyncio.sleep(100)
#
# asyncio.get_event_loop().run_until_complete(main())

# 解决webdriver被识别的问题
# import asyncio
# from pyppeteer import launch
#
#
# async def main():
#     browser = await launch(headless=False)
#     page = await browser.newPage()
#     await page.goto('https://login.taobao.com/member/login.jhtml?redirectURL=https://www.taobao.com/')
#     await page.evaluate(
#         '''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')
#     await asyncio.sleep(100)
#
# asyncio.get_event_loop().run_until_complete(main())



# 最终解决方案：
import asyncio
from pyppeteer import launch

width, height = 1366, 768

async def main():
    browser = await launch(headless=False,
                           devtools=True,
                           args=[f'--window-size={width},{height}'])
    page = await browser.newPage()
    await page.setViewport({'width': width, 'height': height})

    await page.goto('https://login.taobao.com/member/login.jhtml?redirectURL=https://www.taobao.com/')
    await page.evaluate(
        '''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')

    await asyncio.sleep(1000)

asyncio.get_event_loop().run_until_complete(main())



