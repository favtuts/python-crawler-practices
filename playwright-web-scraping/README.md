# Web Scraping with Playwright in Python


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


# Extract SPA Web content

Waiting for the content to load
```python
await page.waitForSelector('#content');
await page.waitForSelector('#root');
await page.waitForSelector('body');
```


# References
* https://stackoverflow.com/questions/69980581/get-entire-playwright-page-in-html-and-text
* https://www.roborabbit.com/blog/web-scraping-with-playwright-in-python/
* https://blog.apify.com/scraping-single-page-applications-with-playwright/
* https://crawlee.dev/docs/examples/playwright-crawler