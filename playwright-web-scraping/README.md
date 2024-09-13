# Web Scraping with Playwright in Python
* https://tuts.heomi.net/web-scraping-with-playwright-in-python/

# Preparing the Python environment

We are using Python3.10
```sh
$ python3 --version
Python 3.10.14
```

Upgrade Pip to latest version
```sh
$ pip install --upgrade pip
$ pip --version
pip 24.2 from /home/tvt/.pyenv/versions/3.10.14/lib/python3.10/site-packages/pip (python 3.10)
```

Install Pipenv
```sh
$ pip install pipenv
```

Create virtual environment
```sh
$ cd playwright-web-scraping
$ pipenv --python 3.10
```

Activate the environment
```sh
$ pipenv shell
```

Check virtual environment location
```sh
$ echo $VIRTUAL_ENV
/home/tvt/.local/share/virtualenvs/playwright-web-scraping-2t7AIYan
```

# Setup Playwright

**Step 1. Install the Playwright Package**
Install the Playwright package so that it can be used in your Python code:
```sh
$ pipenv install playwright
```

**Step 2. Install Browser Drivers.**
The command below installs all available browsers (Chromium, Firefox, and WebKit) using the Playwright CLI by default:
```sh
$ playwright install
```

To install a particular browser (eg. Chromium) only, provide its name as an argument in the command:
```sh
$ playwright install chromium
```

The installed browsers will be saved into OS-specific cache folders. Therefore, we do not need to specify their location in the code. By default, they will be kept in:

* `%USERPROFILE%\\AppData\\Local\\ms-playwright` on Windows
* `~/Library/Caches/ms-playwright` on MacOS
* `~/.cache/ms-playwright` on Linux

You can see the logs with errors
```sh
playwright-web-scraping) tvt@TVTLAP:~/techspace/python/python-crawler-practices/playwright-web-scraping$ playwright install
Downloading Chromium 128.0.6613.18 (playwright build v1129) from https://playwright.azureedge.net/builds/chromium/1129/chromium-linux.zip
162.8 MiB [====================] 100% 0.0s
Chromium 128.0.6613.18 (playwright build v1129) downloaded to /home/tvt/.cache/ms-playwright/chromium-1129
Downloading FFMPEG playwright build v1009 from https://playwright.azureedge.net/builds/ffmpeg/1009/ffmpeg-linux.zip
2.6 MiB [====================] 100% 0.0s
FFMPEG playwright build v1009 downloaded to /home/tvt/.cache/ms-playwright/ffmpeg-1009
Downloading Firefox 128.0 (playwright build v1458) from https://playwright.azureedge.net/builds/firefox/1458/firefox-ubuntu-22.04.zip
85.6 MiB [====================] 100% 0.0s
Firefox 128.0 (playwright build v1458) downloaded to /home/tvt/.cache/ms-playwright/firefox-1458
Downloading Webkit 18.0 (playwright build v2051) from https://playwright.azureedge.net/builds/webkit/2051/webkit-ubuntu-22.04.zip
87.3 MiB [====================] 100% 0.0s
Webkit 18.0 (playwright build v2051) downloaded to /home/tvt/.cache/ms-playwright/webkit-2051
Playwright Host validation warning: 
╔══════════════════════════════════════════════════════╗
║ Host system is missing dependencies to run browsers. ║
║ Please install them with the following command:      ║
║                                                      ║
║     sudo playwright install-deps                     ║
║                                                      ║
║ Alternatively, use apt:                              ║
║     sudo apt-get install libatk1.0-0\                ║
║         libatk-bridge2.0-0\                          ║
║         libxkbcommon0\                               ║
║         libatspi2.0-0\                               ║
║         libxdamage1\                                 ║
║         libgbm1\                                     ║
║         libasound2                                   ║
║                                                      ║
║ <3 Playwright Team                                   ║
╚══════════════════════════════════════════════════════╝
    at validateDependenciesLinux (/home/tvt/.local/share/virtualenvs/playwright-web-scraping-2t7AIYan/lib/python3.10/site-packages/playwright/driver/package/lib/server/registry/dependencies.js:216:9)
    at process.processTicksAndRejections (node:internal/process/task_queues:95:5)
    at async Registry._validateHostRequirements (/home/tvt/.local/share/virtualenvs/playwright-web-scraping-2t7AIYan/lib/python3.10/site-packages/playwright/driver/package/lib/server/registry/index.js:575:43)
    at async Registry._validateHostRequirementsForExecutableIfNeeded (/home/tvt/.local/share/virtualenvs/playwright-web-scraping-2t7AIYan/lib/python3.10/site-packages/playwright/driver/package/lib/server/registry/index.js:673:7)
    at async Registry.validateHostRequirementsForExecutablesIfNeeded (/home/tvt/.local/share/virtualenvs/playwright-web-scraping-2t7AIYan/lib/python3.10/site-packages/playwright/driver/package/lib/server/registry/index.js:662:43)
    at async t.<anonymous> (/home/tvt/.local/share/virtualenvs/playwright-web-scraping-2t7AIYan/lib/python3.10/site-packages/playwright/driver/package/lib/cli/program.js:119:7)
```

To fix the errors, we run the commands:
```sh
playwright install-deps
```

# Extract Data

Playwright run synchronously
```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
```

Playwright can run synchronously and asynchronously. To run it asynchronously, `use async_playwright()` instead of `sync_playwright()` and add await to your code:

```python
from playwright.sync_api import async_playwright

with async_playwright() as p:
	browser = await p.chromium.launch()
```


Create the [extract_jobs.py](./extract_jobs.py) script file with the full code:

```python
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
```

Run the script
```sh
$ pipenv run python extract_jobs.py


Job Title: Senior Community-Services Administrator  -  /jobs/__5qLx3OctM-senior-community-services-administrator/
Company: Toughjoyfax Inc
Salary:  $13,000 / year
Location:  Faroe Islands

.....

Job Title: Human Healthcare Analyst  -  /jobs/HvP7aENB7ro-human-healthcare-analyst/
Company: Otcom Inc
Salary:  $103,000 / year
Location:  Azerbaijan

Job Title: Regional Legal Executive  -  /jobs/BsiICmiDX2w-regional-legal-executive/
Company: Hyena and Sons
Salary:  $121,000 / year
Location:  Madagascar
```



# Get full HTML content

We can query the elemant by selector = "body" to get full HTML content body
```sh
$ pipenv run python extract_html.py
```

# Scrape More Data

When you click on a [job on the board](https://playground.roborabbit.com/jobs/), you will be redirected to [Job Detail page](https://playground.roborabbit.com/jobs/G4NBnofFz1Y-accounting-developer/). In the detail job page we can see more data like number of applicants.

To scrape these details, you can click on the links using `click()` and find the target elements using similar methods. Then, use `page.go_back()` to go back to the main page and continue with the next job in the list.

```python
...
for card in job_card:
      
        job_element = card.locator("a") 
				...   
        job_element.click() # go to the link
        applicant = page.locator(".applicants").inner_html()
        page.go_back()
        
        company = card.locator(".company").inner_html()
        location = card.locator(".location").inner_html()
        salary = card.locator(".salary").inner_html()
        
        # Print the extracted text and link
        print("Job Title:", job_title, " - ", link)
        print("Company:", company)
        print("Salary: ", salary)
        print("Location: ", location)
        print("Applicants: ", applicant)
        print()
...
```


# Extract SPA Web content

Waiting for the content to load
```python
await page.waitForSelector('#content');
await page.waitForSelector('#root');
await page.waitForSelector('body');
```

You may need to provide UserAgent and wail util the `domcontentloaded`, example:
```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    # user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
    ua = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/69.0.3497.100 Safari/537.36"
    )
    url = (
        "https://www.apple.com/br/shop/product/MV7N2BE/A/airpods-com-estojo-de-recarga"
    )
    page = browser.new_page(user_agent=ua)
    page.goto(url, wait_until="domcontentloaded")
    sel = "span.as-price-installments:last-child"
    text = (
        page.wait_for_selector(sel)
        .text_content()
        .replace("à vista (10% de desconto)", "")
        .strip()
    )
    print(text)  # => R$ 1.399,50
    browser.close()
```

Run the code SPA script:
```bash
pipenv run python extract_spa.py
```


# Extract text from HTML

After you extract HTML content using Playwright, you may want to extract the text only from HTML codes.


## Using BeautifulSoup

You just have to install BeautifulSoup before 
```sh
pipenv install beautifulsoup4
```

Then use the piece of code for extracting text without getting javascript or not wanted things
```python
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"
html = urlopen(url).read()
soup = BeautifulSoup(html, features="html.parser")

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)

print(text)
```

## Using html2text Library

The [html2text](https://pypi.org/project/html2text/) Turn HTML into equivalent Markdown-structured text.
```sh
pipenv install html2text
```

Here is an example:
```python
import html2text
html_data = "<p>Check out my [blog](http://example.com)!</p>"
text_maker = html2text.HTML2Text()
text_maker.ignore_links = True
plain_text = text_maker.handle(html_data)
print(plain_text)
```

# Make Absolute links in HTML 

Relative links can be found in the following HTML tags:a, link, img

```python
from urllib.parse import urljoin
from bs4 import BeautifulSoup

def MakeAbsoluteLinks(url, soup):
    '''
        Convert all links in BS object to absolute
        url - base url (downloaded)
        soup - soup object
    '''
    # Find all a tags
    for a in soup.findAll('a'):
        # if this tag have href property
        if a.get('href'):
            # Make link in absolute format
            a['href'] = urljoin(url, a['href'])
    # Find all link tags
    for link in soup.findAll('link'):
        # if this tag have href property
        if link.get('href'):
            # Make link in absolute format
            link['href'] = urljoin(url, link['href'])
    # Find all img tags
    for img in soup.findAll('img'):
        # if this tag have src property
        if img.get('src'):
            # Make link in absolute format
            img['src'] = urljoin(url, img['src'])

# Process HTML data into soup structure
soup = BeautifulSoup(response.content, 'lxml')
# Convert relative links into absolute if any
MakeAbsoluteLinks(url, soup)

print(soup.prettify())
```


# References
* https://stackoverflow.com/questions/69980581/get-entire-playwright-page-in-html-and-text
* https://www.roborabbit.com/blog/web-scraping-with-playwright-in-python/
* https://blog.apify.com/scraping-single-page-applications-with-playwright/
* https://crawlee.dev/docs/examples/playwright-crawler
* https://stackoverflow.com/questions/328356/extracting-text-from-html-file-using-python
* https://stackoverflow.com/questions/76122020/playwright-does-not-render-js-scripts-and-hence-the-html-is-not-fully-loaded
* https://stackoverflow.com/questions/71874282/ubuntu-python-playright-headless-true-get-wrong-page
* http://mycoding.uk/a/python__how_to_make_absolute_links_in_beautifulsoup.html