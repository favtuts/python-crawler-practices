from playwright.async_api import async_playwright
import asyncio
#create an async run function
async def run():
    async with async_playwright() as playwright:
        #launch a browser
        browser = await playwright.chromium.launch(headless=True)
        #create a new page
        page = await browser.new_page()
        #go to the site
        await page.goto("https://quotes.toscrape.com")
        #await page.goto("https://emteller.vn/")
        #get full html of the page
        fullHtml = await page.content()
        print(f'Full HTML Content:\n{fullHtml}')
        print(f'***************************')
        bodyHtml = await page.inner_html('body')
        print(f'Body Content:\n{bodyHtml}')
        
        #close the browser
        await browser.close()

#async main function
async def main():
    await run()

#run the main function using asyncio
asyncio.run(main())