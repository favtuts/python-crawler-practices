from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    
    page = browser.new_page()
    page.goto("https://playground.browserbear.com/jobs/")
                  
    job_card = page.locator("article").all()
    
    for card in job_card:
      
        job_element = card.locator("a")
        job_title = job_element.inner_html()
        link = job_element.get_attribute("href")  
        
        company = card.locator(".company").inner_html()
        location = card.locator(".location").inner_html()
        salary = card.locator(".salary").inner_html()
        
        print("Job Title:", job_title, " - ", link)
        print("Company:", company)
        print("Salary: ", salary)
        print("Location: ", location)
        print()
                
    browser.close()