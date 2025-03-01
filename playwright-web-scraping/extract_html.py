from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    
    page = browser.new_page()
    #page.goto("https://playground.browserbear.com/jobs/")
    page.goto("https://emteller.vn/")
    
    element = page.query_selector("body")
    
    html = element.inner_html()
    
    print(f"HTML content extracted: \n{html}")
    