import asyncio
from pyppeteer import launch

width, height = 1366, 768

async def main():
    browser = await launch(headless=False,
                           devtools=True,
                           args=[f'--window-size={width},{height}'])
    page = await browser.newPage()
    await page.setViewport({'width': width, 'height': height})

    await page.goto('https://www.411.com/distil_r_captcha.html?requestId=35a8b220-d6de-42b5-a988-dfa0c853ff82&httpReferrer=%2Faddress%2F139-Sunnyside-Dr%2FBoone-NC%2F',timeout=10000000)
    await page.evaluate(
        '''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')

    await asyncio.sleep(1000)

asyncio.get_event_loop().run_until_complete(main())