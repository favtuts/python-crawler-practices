from playwright.async_api import async_playwright
import asyncio
#create an async run function
async def run():
    async with async_playwright() as playwright:
        #launch a browser
        browser = await playwright.chromium.launch(headless=True, timeout=180 * 1000)
                
        
        #create a new page                
        ua = (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/69.0.3497.100 Safari/537.36"
        )
        page = await browser.new_page(user_agent=ua)
        
        #go to the site        
        url = (
            "https://emteller.vn/"
        )              
                
        await page.goto(url)        
        await page.wait_for_timeout(5000)
        await page.keyboard.press('PageDown')
        await page.wait_for_timeout(2000)        
             
        """
        #await page.goto(url, wait_until="domcontentloaded", timeout=180 * 1000)
        await page.goto(url)
        await page.wait_for_load_state(state="domcontentloaded")        
        await page.keyboard.press('PageDown')
        """

        #waiting for content to load
        #for a specific selector to appear on the page        
        #await page.wait_for_selector('#root');
        await page.wait_for_selector('body');
        
                
        fullHtml = await page.content()
        print(f'Full HTML Content:\n{fullHtml}')
        print(f'***************************')
        bodyHtml = await page.inner_text('body')
        print(f'Body Content:\n{bodyHtml}')            
        
        #close the browser
        await browser.close()
        
        # save html to file
        with open('emteller.html', 'w', encoding='utf-8') as f:
            f.write(fullHtml)

#async main function
async def main():
    await run()

#run the main function using asyncio
asyncio.run(main())