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


Create the [app.py](./app.py) script file with the full code:

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
$ pipenv run python app.py


Job Title: Senior Community-Services Administrator  -  /jobs/__5qLx3OctM-senior-community-services-administrator/
Company: Toughjoyfax Inc
Salary:  $13,000 / year
Location:  Faroe Islands

Job Title: Principal Design Agent  -  /jobs/Ainsa9pynZg-principal-design-agent/
Company: Cheetah Group
Salary:  $19,000 / year
Location:  Liechtenstein

Job Title: Internal Hospitality Director  -  /jobs/Pi36OJrcDVc-internal-hospitality-director/
Company: Kanlam and Sons
Salary:  $147,000 / year
Location:  Singapore

Job Title: Central Director  -  /jobs/a-oQet9OWpk-central-director/
Company: Prodder LLC
Salary:  $16,000 / year
Location:  Antarctica (the territory South of 60 deg S)

Job Title: Retail Liaison  -  /jobs/2-FrYyvyYqk-retail-liaison/
Company: Oyster and Sons
Salary:  $15,000 / year
Location:  Sao Tome and Principe

Job Title: Global Manufacturing Technician  -  /jobs/jFv-wpSoi_s-global-manufacturing-technician/
Company: Wasp Inc
Salary:  $18,000 / year
Location:  Gabon

Job Title: Design Liaison  -  /jobs/xGOmJWSQc1k-design-liaison/
Company: Span LLC
Salary:  $11,000 / year
Location:  Netherlands Antilles

Job Title: Legacy Education Administrator  -  /jobs/7OX0oyl0F9g-legacy-education-administrator/
Company: Tempsoft LLC
Salary:  $11,000 / year
Location:  Slovenia

Job Title: Education Administrator  -  /jobs/cMi9kVFGEUE-education-administrator/
Company: Treeflex and Sons
Salary:  $12,000 / year
Location:  United Arab Emirates

Job Title: Farming Consultant  -  /jobs/vcT80C8lD-4-farming-consultant/
Company: Lotlux Inc
Salary:  $18,000 / year
Location:  Jordan

Job Title: Investor Coordinator  -  /jobs/HyDt0GAUzwM-investor-coordinator/
Company: Tres Zap and Sons
Salary:  $19,000 / year
Location:  United States of America

Job Title: Consulting Liaison  -  /jobs/zWfTdZRIuUw-consulting-liaison/
Company: Greenlam LLC
Salary:  $133,000 / year
Location:  Niue

Job Title: Corporate IT Administrator  -  /jobs/eJSHJ1e-6CM-corporate-it-administrator/
Company: Cardify and Sons
Salary:  $12,000 / year
Location:  Iceland

Job Title: Design Officer  -  /jobs/y_FclEnivOM-design-officer/
Company: Gnu Inc
Salary:  $91,000 / year
Location:  Uganda

Job Title: Hospitality Analyst  -  /jobs/mI8v2pEOo8E-hospitality-analyst/
Company: Llama Group
Salary:  $59,000 / year
Location:  Tuvalu

Job Title: Community-Services Facilitator  -  /jobs/brOBI7tj_v4-community-services-facilitator/
Company: Clam and Sons
Salary:  $83,000 / year
Location:  Ethiopia

Job Title: Central Consultant  -  /jobs/250H49_317E-central-consultant/
Company: Wrapsafe LLC
Salary:  $16,000 / year
Location:  Virgin Islands, U.S.

Job Title: Mining Assistant  -  /jobs/vuYqzyHEbFg-mining-assistant/
Company: Namfix LLC
Salary:  $18,000 / year
Location:  Mauritius

Job Title: Corporate Mining Architect  -  /jobs/j_zfrCBFR_E-corporate-mining-architect/
Company: Alphazap LLC
Salary:  $16,000 / year
Location:  Serbia

Job Title: Product Consultant  -  /jobs/uTQ14QEacE4-product-consultant/
Company: Flowdesk Group
Salary:  $102,000 / year
Location:  Saint Kitts and Nevis

Job Title: Hospitality Representative  -  /jobs/g5BB5Wm9MDE-hospitality-representative/
Company: Dolphin Inc
Salary:  $11,000 / year
Location:  Cook Islands

Job Title: Central Analyst  -  /jobs/U2_o2nTv6yc-central-analyst/
Company: Y Solowarm and Sons
Salary:  $126,000 / year
Location:  Kyrgyz Republic

Job Title: Internal Education Technician  -  /jobs/qRRcnWuoedU-internal-education-technician/
Company: Louse LLC
Salary:  $105,000 / year
Location:  Liberia

Job Title: Global Sales Analyst  -  /jobs/_JDDcfZlPCs-global-sales-analyst/
Company: Asoka Group
Salary:  $12,000 / year
Location:  Saudi Arabia

Job Title: Forward Manager  -  /jobs/x5l8ZuWh-ls-forward-manager/
Company: Cicada Inc
Salary:  $41,000 / year
Location:  Mauritania

Job Title: Government Representative  -  /jobs/ZjvGxoJGjX4-government-representative/
Company: Sea Lion and Sons
Salary:  $132,000 / year
Location:  Romania

Job Title: Dynamic IT Administrator  -  /jobs/w9dxz2RYrqs-dynamic-it-administrator/
Company: Home Ing Inc
Salary:  $14,000 / year
Location:  Tokelau

Job Title: Community-Services Associate  -  /jobs/EsEusi2Bisw-community-services-associate/
Company: Wildebeest Group
Salary:  $65,000 / year
Location:  New Caledonia

Job Title: Product Community-Services Assistant  -  /jobs/JdlXSytj2vk-product-community-services-assistant/
Company: Zathin Inc
Salary:  $88,000 / year
Location:  El Salvador

Job Title: Marketing Designer  -  /jobs/NMiCJS3hwNE-marketing-designer/
Company: Sheep and Sons
Salary:  $94,000 / year
Location:  Trinidad and Tobago

Job Title: Investor Architect  -  /jobs/iZoUrjPgUoY-investor-architect/
Company: Horse Inc
Salary:  $14,000 / year
Location:  Saint Pierre and Miquelon

Job Title: Lead Advertising Coordinator  -  /jobs/mA6AvsNcMqo-lead-advertising-coordinator/
Company: Bee Group
Salary:  $18,000 / year
Location:  Burundi

Job Title: Education Executive  -  /jobs/fgX6YJjDUhU-education-executive/
Company: Ox Inc
Salary:  $11,000 / year
Location:  Isle of Man

Job Title: Customer Community-Services Planner  -  /jobs/4_79ata6raw-customer-community-services-planner/
Company: Serval Inc
Salary:  $54,000 / year
Location:  Antigua and Barbuda

Job Title: Lead Agent  -  /jobs/_p7pDOIK1ZY-lead-agent/
Company: Elk and Sons
Salary:  $17,000 / year
Location:  Jordan

Job Title: Construction Designer  -  /jobs/C2qPq5LtS5c-construction-designer/
Company: Matsoft Group
Salary:  $19,000 / year
Location:  Martinique

Job Title: District Community-Services Developer  -  /jobs/-Cmw4sxh1k8-district-community-services-developer/
Company: Chimpanzee Inc
Salary:  $32,000 / year
Location:  Indonesia

Job Title: National Agent  -  /jobs/TyVf0SbtbG0-national-agent/
Company: Stronghold and Sons
Salary:  $103,000 / year
Location:  Albania

Job Title: District Administrator  -  /jobs/TzT22HsHfis-district-administrator/
Company: Sheep LLC
Salary:  $10,000 / year
Location:  Cocos (Keeling) Islands

Job Title: International Facilitator  -  /jobs/RFSM2s00rIM-international-facilitator/
Company: Cicada Group
Salary:  $10,000 / year
Location:  Turkey

Job Title: Senior Banking Associate  -  /jobs/RApb9prKuu0-senior-banking-associate/
Company: Butterfly Inc
Salary:  $136,000 / year
Location:  Sudan

Job Title: Accounting Executive  -  /jobs/6nyPYHpSMlM-accounting-executive/
Company: Y Solowarm and Sons
Salary:  $120,000 / year
Location:  Ecuador

Job Title: Legacy Director  -  /jobs/vvjlhAvu2CA-legacy-director/
Company: Zebra and Sons
Salary:  $136,000 / year
Location:  France

Job Title: Legal Director  -  /jobs/YxTjpTWDXWU-legal-director/
Company: Minnow and Sons
Salary:  $49,000 / year
Location:  French Southern Territories

Job Title: Forward Consultant  -  /jobs/Wwd54aeW7Jg-forward-consultant/
Company: Ferret and Sons
Salary:  $116,000 / year
Location:  Estonia

Job Title: Corporate Accounting Specialist  -  /jobs/ROTIL_bvrtU-corporate-accounting-specialist/
Company: Wombat Inc
Salary:  $14,000 / year
Location:  Czech Republic

Job Title: Senior Marketing Administrator  -  /jobs/qDiRNlk7Hvk-senior-marketing-administrator/
Company: Butterfly and Sons
Salary:  $18,000 / year
Location:  Northern Mariana Islands

Job Title: Accounting Engineer  -  /jobs/ooWYMEfr3z4-accounting-engineer/
Company: Herring Group
Salary:  $16,000 / year
Location:  Saint Martin

Job Title: Real-Estate Director  -  /jobs/6LKA62ROYdI-real-estate-director/
Company: Antelope LLC
Salary:  $60,000 / year
Location:  Central African Republic

Job Title: Government Manager  -  /jobs/w_0TdloV5VU-government-manager/
Company: Dog and Sons
Salary:  $119,000 / year
Location:  Colombia

Job Title: Principal Farming Associate  -  /jobs/90deU2EWg3Y-principal-farming-associate/
Company: Zaam Dox LLC
Salary:  $118,000 / year
Location:  Mali

Job Title: Accounting Developer  -  /jobs/G4NBnofFz1Y-accounting-developer/
Company: Transcof Group
Salary:  $112,000 / year
Location:  Saint Helena

Job Title: Chief Banking Architect  -  /jobs/kC0z-1Vl9Ms-chief-banking-architect/
Company: Squirrel and Sons
Salary:  $136,000 / year
Location:  Madagascar

Job Title: Hospitality Architect  -  /jobs/1Gj25N5b76k-hospitality-architect/
Company: Fix San and Sons
Salary:  $93,000 / year
Location:  Mauritania

Job Title: Advertising Designer  -  /jobs/mKAcpXLAokU-advertising-designer/
Company: Hyena LLC
Salary:  $85,000 / year
Location:  Malawi

Job Title: Customer Legal Supervisor  -  /jobs/nUdAH1oHxv4-customer-legal-supervisor/
Company: Badger Inc
Salary:  $102,000 / year
Location:  Jersey

Job Title: Central IT Liaison  -  /jobs/aajw22TLacc-central-it-liaison/
Company: Moose LLC
Salary:  $19,000 / year
Location:  Mali

Job Title: Administration Architect  -  /jobs/hwrAWsbzO4E-administration-architect/
Company: Sheep Inc
Salary:  $68,000 / year
Location:  Germany

Job Title: Regional Coordinator  -  /jobs/Frb3ANFeSKo-regional-coordinator/
Company: Holdlamis and Sons
Salary:  $132,000 / year
Location:  Croatia

Job Title: Marketing Representative  -  /jobs/Ok3EKAX-ktY-marketing-representative/
Company: Lizard LLC
Salary:  $72,000 / year
Location:  Macedonia

Job Title: Dynamic Agent  -  /jobs/kqer54AJ5RU-dynamic-agent/
Company: Grasshopper Group
Salary:  $13,000 / year
Location:  Equatorial Guinea

Job Title: Human Design Producer  -  /jobs/zGy3LSZN2vQ-human-design-producer/
Company: Coyote Inc
Salary:  $18,000 / year
Location:  Guyana

Job Title: Consulting Executive  -  /jobs/GBjpfhn-d4g-consulting-executive/
Company: Gembucket Inc
Salary:  $17,000 / year
Location:  Brunei Darussalam

Job Title: Education Analyst  -  /jobs/C17zozFlppA-education-analyst/
Company: Tempsoft Inc
Salary:  $44,000 / year
Location:  Cote d'Ivoire

Job Title: Central Director  -  /jobs/XnAPuoPVFpU-central-director/
Company: Zaam Dox Group
Salary:  $10,000 / year
Location:  Turkey

Job Title: Accounting Associate  -  /jobs/8fKKlOp7mbs-accounting-associate/
Company: Fish Inc
Salary:  $82,000 / year
Location:  Tajikistan

Job Title: Central Assistant  -  /jobs/v6dbuc8OaQE-central-assistant/
Company: Temp LLC
Salary:  $78,000 / year
Location:  Martinique

Job Title: Manufacturing Administrator  -  /jobs/FWxWBlJ2DPk-manufacturing-administrator/
Company: Beaver LLC
Salary:  $14,000 / year
Location:  Syrian Arab Republic

Job Title: Regional Marketing Associate  -  /jobs/y7YxdpLuAwo-regional-marketing-associate/
Company: Beetle Group
Salary:  $15,000 / year
Location:  Tokelau

Job Title: Consulting Administrator  -  /jobs/6EWEZ7EZScU-consulting-administrator/
Company: Wombat and Sons
Salary:  $19,000 / year
Location:  Hong Kong

Job Title: Administration Associate  -  /jobs/emR9Xshk6VY-administration-associate/
Company: Greenlam Inc
Salary:  $89,000 / year
Location:  Tonga

Job Title: Marketing Orchestrator  -  /jobs/eVm34eEgNFE-marketing-orchestrator/
Company: Gembucket Group
Salary:  $11,000 / year
Location:  Sri Lanka

Job Title: Marketing Analyst  -  /jobs/JvwuIaNk_YA-marketing-analyst/
Company: Tresom Group
Salary:  $149,000 / year
Location:  Argentina

Job Title: Retail Planner  -  /jobs/7XdH4f-AtLM-retail-planner/
Company: Rank and Sons
Salary:  $15,000 / year
Location:  Mauritius

Job Title: Banking Orchestrator  -  /jobs/BrBYJ8s8wuQ-banking-orchestrator/
Company: Greenlam Group
Salary:  $141,000 / year
Location:  Pitcairn Islands

Job Title: Community-Services Facilitator  -  /jobs/tyeSulkhoW8-community-services-facilitator/
Company: Job Group
Salary:  $15,000 / year
Location:  Lesotho

Job Title: Government Executive  -  /jobs/yUlrEA6yWLA-government-executive/
Company: Prodder and Sons
Salary:  $10,000 / year
Location:  Comoros

Job Title: Community-Services Facilitator  -  /jobs/80MZHJ24tYs-community-services-facilitator/
Company: Dinosaur Inc
Salary:  $85,000 / year
Location:  Djibouti

Job Title: Design Strategist  -  /jobs/c3UatcBE1QM-design-strategist/
Company: Bytecard LLC
Salary:  $11,000 / year
Location:  Argentina

Job Title: Global Producer  -  /jobs/gHh_LHek0io-global-producer/
Company: Bytecard LLC
Salary:  $135,000 / year
Location:  Cayman Islands

Job Title: Government Architect  -  /jobs/DXdwUbqp97c-government-architect/
Company: Stronghold Inc
Salary:  $11,000 / year
Location:  Bhutan

Job Title: International Education Producer  -  /jobs/XOHGLv7flpU-international-education-producer/
Company: Job Group
Salary:  $96,000 / year
Location:  Cameroon

Job Title: Retail Executive  -  /jobs/Z3dpvHcYkJM-retail-executive/
Company: Flexidy Group
Salary:  $10,000 / year
Location:  Moldova

Job Title: Chief Manager  -  /jobs/j7TMjxGuyv4-chief-manager/
Company: Zathin Inc
Salary:  $17,000 / year
Location:  Lithuania

Job Title: Direct Liaison  -  /jobs/dFx4KjDp43g-direct-liaison/
Company: Andalax Inc
Salary:  $16,000 / year
Location:  Mozambique

Job Title: Healthcare Executive  -  /jobs/p_nxHyf5gvI-healthcare-executive/
Company: Trout and Sons
Salary:  $17,000 / year
Location:  French Polynesia

Job Title: Corporate Design Designer  -  /jobs/77l8XDwJhbs-corporate-design-designer/
Company: Sonair LLC
Salary:  $18,000 / year
Location:  Ghana

Job Title: National Retail Consultant  -  /jobs/hOu3xRV9sAI-national-retail-consultant/
Company: Jellyfish Inc
Salary:  $77,000 / year
Location:  Colombia

Job Title: Hospitality Architect  -  /jobs/sJqcU1SdDUk-hospitality-architect/
Company: Grasshopper and Sons
Salary:  $71,000 / year
Location:  Zimbabwe

Job Title: Corporate Technology Consultant  -  /jobs/kwRxVo6Sr5I-corporate-technology-consultant/
Company: Fish Group
Salary:  $18,000 / year
Location:  Liechtenstein

Job Title: Dynamic Education Technician  -  /jobs/CcuTAiYndDk-dynamic-education-technician/
Company: Mat Lam Tam and Sons
Salary:  $15,000 / year
Location:  Iceland

Job Title: Internal Accounting Consultant  -  /jobs/l7wkvVpaeSg-internal-accounting-consultant/
Company: Bigtax Inc
Salary:  $15,000 / year
Location:  Vietnam

Job Title: Internal Real-Estate Administrator  -  /jobs/e0SiwZ21kec-internal-real-estate-administrator/
Company: Skunk Inc
Salary:  $76,000 / year
Location:  Iraq

Job Title: Technology Representative  -  /jobs/mU6Qg9OEJJY-technology-representative/
Company: Raven Inc
Salary:  $137,000 / year
Location:  Saint Vincent and the Grenadines

Job Title: Dynamic Mining Designer  -  /jobs/7A_7bWBqxvw-dynamic-mining-designer/
Company: Serval LLC
Salary:  $12,000 / year
Location:  Macedonia

Job Title: Forward Construction Director  -  /jobs/3_sC91qo81c-forward-construction-director/
Company: Bamity Group
Salary:  $95,000 / year
Location:  Portugal

Job Title: Healthcare Technician  -  /jobs/KNYQZeTRuOc-healthcare-technician/
Company: Regrant and Sons
Salary:  $38,000 / year
Location:  Albania

Job Title: Direct Banking Facilitator  -  /jobs/3xNuBkBjTbU-direct-banking-facilitator/
Company: Tresom LLC
Salary:  $16,000 / year
Location:  Portugal

Job Title: Human Healthcare Analyst  -  /jobs/HvP7aENB7ro-human-healthcare-analyst/
Company: Otcom Inc
Salary:  $103,000 / year
Location:  Azerbaijan

Job Title: Regional Legal Executive  -  /jobs/BsiICmiDX2w-regional-legal-executive/
Company: Hyena and Sons
Salary:  $121,000 / year
Location:  Madagascar

playwright-web-scrapingtvt@TVTLAP:~/techspace/python/python-crawler-practices/playwright-web-scraping$ pipenv run python app.py
Courtesy Notice: Pipenv found itself running within a virtual environment, so it will automatically use that environment, instead of creating its own for any project. You can set PIPENV_IGNORE_VIRTUALENVS=1 to force pipenv to ignore that environment and create its own instead. You can set PIPENV_VERBOSITY=-1 to suppress this warning.
Job Title: Senior Community-Services Administrator  -  /jobs/__5qLx3OctM-senior-community-services-administrator/
Company: Toughjoyfax Inc
Salary:  $13,000 / year
Location:  Faroe Islands

Job Title: Principal Design Agent  -  /jobs/Ainsa9pynZg-principal-design-agent/
Company: Cheetah Group
Salary:  $19,000 / year
Location:  Liechtenstein

Job Title: Internal Hospitality Director  -  /jobs/Pi36OJrcDVc-internal-hospitality-director/
Company: Kanlam and Sons
Salary:  $147,000 / year
Location:  Singapore

Job Title: Central Director  -  /jobs/a-oQet9OWpk-central-director/
Company: Prodder LLC
Salary:  $16,000 / year
Location:  Antarctica (the territory South of 60 deg S)

Job Title: Retail Liaison  -  /jobs/2-FrYyvyYqk-retail-liaison/
Company: Oyster and Sons
Salary:  $15,000 / year
Location:  Sao Tome and Principe

Job Title: Global Manufacturing Technician  -  /jobs/jFv-wpSoi_s-global-manufacturing-technician/
Company: Wasp Inc
Salary:  $18,000 / year
Location:  Gabon

Job Title: Design Liaison  -  /jobs/xGOmJWSQc1k-design-liaison/
Company: Span LLC
Salary:  $11,000 / year
Location:  Netherlands Antilles

Job Title: Legacy Education Administrator  -  /jobs/7OX0oyl0F9g-legacy-education-administrator/
Company: Tempsoft LLC
Salary:  $11,000 / year
Location:  Slovenia

Job Title: Education Administrator  -  /jobs/cMi9kVFGEUE-education-administrator/
Company: Treeflex and Sons
Salary:  $12,000 / year
Location:  United Arab Emirates

Job Title: Farming Consultant  -  /jobs/vcT80C8lD-4-farming-consultant/
Company: Lotlux Inc
Salary:  $18,000 / year
Location:  Jordan

Job Title: Investor Coordinator  -  /jobs/HyDt0GAUzwM-investor-coordinator/
Company: Tres Zap and Sons
Salary:  $19,000 / year
Location:  United States of America

Job Title: Consulting Liaison  -  /jobs/zWfTdZRIuUw-consulting-liaison/
Company: Greenlam LLC
Salary:  $133,000 / year
Location:  Niue

Job Title: Corporate IT Administrator  -  /jobs/eJSHJ1e-6CM-corporate-it-administrator/
Company: Cardify and Sons
Salary:  $12,000 / year
Location:  Iceland

Job Title: Design Officer  -  /jobs/y_FclEnivOM-design-officer/
Company: Gnu Inc
Salary:  $91,000 / year
Location:  Uganda

Job Title: Hospitality Analyst  -  /jobs/mI8v2pEOo8E-hospitality-analyst/
Company: Llama Group
Salary:  $59,000 / year
Location:  Tuvalu

Job Title: Community-Services Facilitator  -  /jobs/brOBI7tj_v4-community-services-facilitator/
Company: Clam and Sons
Salary:  $83,000 / year
Location:  Ethiopia

Job Title: Central Consultant  -  /jobs/250H49_317E-central-consultant/
Company: Wrapsafe LLC
Salary:  $16,000 / year
Location:  Virgin Islands, U.S.

Job Title: Mining Assistant  -  /jobs/vuYqzyHEbFg-mining-assistant/
Company: Namfix LLC
Salary:  $18,000 / year
Location:  Mauritius

Job Title: Corporate Mining Architect  -  /jobs/j_zfrCBFR_E-corporate-mining-architect/
Company: Alphazap LLC
Salary:  $16,000 / year
Location:  Serbia

Job Title: Product Consultant  -  /jobs/uTQ14QEacE4-product-consultant/
Company: Flowdesk Group
Salary:  $102,000 / year
Location:  Saint Kitts and Nevis

Job Title: Hospitality Representative  -  /jobs/g5BB5Wm9MDE-hospitality-representative/
Company: Dolphin Inc
Salary:  $11,000 / year
Location:  Cook Islands

Job Title: Central Analyst  -  /jobs/U2_o2nTv6yc-central-analyst/
Company: Y Solowarm and Sons
Salary:  $126,000 / year
Location:  Kyrgyz Republic

Job Title: Internal Education Technician  -  /jobs/qRRcnWuoedU-internal-education-technician/
Company: Louse LLC
Salary:  $105,000 / year
Location:  Liberia

Job Title: Global Sales Analyst  -  /jobs/_JDDcfZlPCs-global-sales-analyst/
Company: Asoka Group
Salary:  $12,000 / year
Location:  Saudi Arabia

Job Title: Forward Manager  -  /jobs/x5l8ZuWh-ls-forward-manager/
Company: Cicada Inc
Salary:  $41,000 / year
Location:  Mauritania

Job Title: Government Representative  -  /jobs/ZjvGxoJGjX4-government-representative/
Company: Sea Lion and Sons
Salary:  $132,000 / year
Location:  Romania

Job Title: Dynamic IT Administrator  -  /jobs/w9dxz2RYrqs-dynamic-it-administrator/
Company: Home Ing Inc
Salary:  $14,000 / year
Location:  Tokelau

Job Title: Community-Services Associate  -  /jobs/EsEusi2Bisw-community-services-associate/
Company: Wildebeest Group
Salary:  $65,000 / year
Location:  New Caledonia

Job Title: Product Community-Services Assistant  -  /jobs/JdlXSytj2vk-product-community-services-assistant/
Company: Zathin Inc
Salary:  $88,000 / year
Location:  El Salvador

Job Title: Marketing Designer  -  /jobs/NMiCJS3hwNE-marketing-designer/
Company: Sheep and Sons
Salary:  $94,000 / year
Location:  Trinidad and Tobago

Job Title: Investor Architect  -  /jobs/iZoUrjPgUoY-investor-architect/
Company: Horse Inc
Salary:  $14,000 / year
Location:  Saint Pierre and Miquelon

Job Title: Lead Advertising Coordinator  -  /jobs/mA6AvsNcMqo-lead-advertising-coordinator/
Company: Bee Group
Salary:  $18,000 / year
Location:  Burundi

Job Title: Education Executive  -  /jobs/fgX6YJjDUhU-education-executive/
Company: Ox Inc
Salary:  $11,000 / year
Location:  Isle of Man

Job Title: Customer Community-Services Planner  -  /jobs/4_79ata6raw-customer-community-services-planner/
Company: Serval Inc
Salary:  $54,000 / year
Location:  Antigua and Barbuda

Job Title: Lead Agent  -  /jobs/_p7pDOIK1ZY-lead-agent/
Company: Elk and Sons
Salary:  $17,000 / year
Location:  Jordan

Job Title: Construction Designer  -  /jobs/C2qPq5LtS5c-construction-designer/
Company: Matsoft Group
Salary:  $19,000 / year
Location:  Martinique

Job Title: District Community-Services Developer  -  /jobs/-Cmw4sxh1k8-district-community-services-developer/
Company: Chimpanzee Inc
Salary:  $32,000 / year
Location:  Indonesia

Job Title: National Agent  -  /jobs/TyVf0SbtbG0-national-agent/
Company: Stronghold and Sons
Salary:  $103,000 / year
Location:  Albania

Job Title: District Administrator  -  /jobs/TzT22HsHfis-district-administrator/
Company: Sheep LLC
Salary:  $10,000 / year
Location:  Cocos (Keeling) Islands

Job Title: International Facilitator  -  /jobs/RFSM2s00rIM-international-facilitator/
Company: Cicada Group
Salary:  $10,000 / year
Location:  Turkey

Job Title: Senior Banking Associate  -  /jobs/RApb9prKuu0-senior-banking-associate/
Company: Butterfly Inc
Salary:  $136,000 / year
Location:  Sudan

Job Title: Accounting Executive  -  /jobs/6nyPYHpSMlM-accounting-executive/
Company: Y Solowarm and Sons
Salary:  $120,000 / year
Location:  Ecuador

Job Title: Legacy Director  -  /jobs/vvjlhAvu2CA-legacy-director/
Company: Zebra and Sons
Salary:  $136,000 / year
Location:  France

Job Title: Legal Director  -  /jobs/YxTjpTWDXWU-legal-director/
Company: Minnow and Sons
Salary:  $49,000 / year
Location:  French Southern Territories

Job Title: Forward Consultant  -  /jobs/Wwd54aeW7Jg-forward-consultant/
Company: Ferret and Sons
Salary:  $116,000 / year
Location:  Estonia

Job Title: Corporate Accounting Specialist  -  /jobs/ROTIL_bvrtU-corporate-accounting-specialist/
Company: Wombat Inc
Salary:  $14,000 / year
Location:  Czech Republic

Job Title: Senior Marketing Administrator  -  /jobs/qDiRNlk7Hvk-senior-marketing-administrator/
Company: Butterfly and Sons
Salary:  $18,000 / year
Location:  Northern Mariana Islands

Job Title: Accounting Engineer  -  /jobs/ooWYMEfr3z4-accounting-engineer/
Company: Herring Group
Salary:  $16,000 / year
Location:  Saint Martin

Job Title: Real-Estate Director  -  /jobs/6LKA62ROYdI-real-estate-director/
Company: Antelope LLC
Salary:  $60,000 / year
Location:  Central African Republic

Job Title: Government Manager  -  /jobs/w_0TdloV5VU-government-manager/
Company: Dog and Sons
Salary:  $119,000 / year
Location:  Colombia

Job Title: Principal Farming Associate  -  /jobs/90deU2EWg3Y-principal-farming-associate/
Company: Zaam Dox LLC
Salary:  $118,000 / year
Location:  Mali

Job Title: Accounting Developer  -  /jobs/G4NBnofFz1Y-accounting-developer/
Company: Transcof Group
Salary:  $112,000 / year
Location:  Saint Helena

Job Title: Chief Banking Architect  -  /jobs/kC0z-1Vl9Ms-chief-banking-architect/
Company: Squirrel and Sons
Salary:  $136,000 / year
Location:  Madagascar

Job Title: Hospitality Architect  -  /jobs/1Gj25N5b76k-hospitality-architect/
Company: Fix San and Sons
Salary:  $93,000 / year
Location:  Mauritania

Job Title: Advertising Designer  -  /jobs/mKAcpXLAokU-advertising-designer/
Company: Hyena LLC
Salary:  $85,000 / year
Location:  Malawi

Job Title: Customer Legal Supervisor  -  /jobs/nUdAH1oHxv4-customer-legal-supervisor/
Company: Badger Inc
Salary:  $102,000 / year
Location:  Jersey

Job Title: Central IT Liaison  -  /jobs/aajw22TLacc-central-it-liaison/
Company: Moose LLC
Salary:  $19,000 / year
Location:  Mali

Job Title: Administration Architect  -  /jobs/hwrAWsbzO4E-administration-architect/
Company: Sheep Inc
Salary:  $68,000 / year
Location:  Germany

Job Title: Regional Coordinator  -  /jobs/Frb3ANFeSKo-regional-coordinator/
Company: Holdlamis and Sons
Salary:  $132,000 / year
Location:  Croatia

Job Title: Marketing Representative  -  /jobs/Ok3EKAX-ktY-marketing-representative/
Company: Lizard LLC
Salary:  $72,000 / year
Location:  Macedonia

Job Title: Dynamic Agent  -  /jobs/kqer54AJ5RU-dynamic-agent/
Company: Grasshopper Group
Salary:  $13,000 / year
Location:  Equatorial Guinea

Job Title: Human Design Producer  -  /jobs/zGy3LSZN2vQ-human-design-producer/
Company: Coyote Inc
Salary:  $18,000 / year
Location:  Guyana

Job Title: Consulting Executive  -  /jobs/GBjpfhn-d4g-consulting-executive/
Company: Gembucket Inc
Salary:  $17,000 / year
Location:  Brunei Darussalam

Job Title: Education Analyst  -  /jobs/C17zozFlppA-education-analyst/
Company: Tempsoft Inc
Salary:  $44,000 / year
Location:  Cote d'Ivoire

Job Title: Central Director  -  /jobs/XnAPuoPVFpU-central-director/
Company: Zaam Dox Group
Salary:  $10,000 / year
Location:  Turkey

Job Title: Accounting Associate  -  /jobs/8fKKlOp7mbs-accounting-associate/
Company: Fish Inc
Salary:  $82,000 / year
Location:  Tajikistan

Job Title: Central Assistant  -  /jobs/v6dbuc8OaQE-central-assistant/
Company: Temp LLC
Salary:  $78,000 / year
Location:  Martinique

Job Title: Manufacturing Administrator  -  /jobs/FWxWBlJ2DPk-manufacturing-administrator/
Company: Beaver LLC
Salary:  $14,000 / year
Location:  Syrian Arab Republic

Job Title: Regional Marketing Associate  -  /jobs/y7YxdpLuAwo-regional-marketing-associate/
Company: Beetle Group
Salary:  $15,000 / year
Location:  Tokelau

Job Title: Consulting Administrator  -  /jobs/6EWEZ7EZScU-consulting-administrator/
Company: Wombat and Sons
Salary:  $19,000 / year
Location:  Hong Kong

Job Title: Administration Associate  -  /jobs/emR9Xshk6VY-administration-associate/
Company: Greenlam Inc
Salary:  $89,000 / year
Location:  Tonga

Job Title: Marketing Orchestrator  -  /jobs/eVm34eEgNFE-marketing-orchestrator/
Company: Gembucket Group
Salary:  $11,000 / year
Location:  Sri Lanka

Job Title: Marketing Analyst  -  /jobs/JvwuIaNk_YA-marketing-analyst/
Company: Tresom Group
Salary:  $149,000 / year
Location:  Argentina

Job Title: Retail Planner  -  /jobs/7XdH4f-AtLM-retail-planner/
Company: Rank and Sons
Salary:  $15,000 / year
Location:  Mauritius

Job Title: Banking Orchestrator  -  /jobs/BrBYJ8s8wuQ-banking-orchestrator/
Company: Greenlam Group
Salary:  $141,000 / year
Location:  Pitcairn Islands

Job Title: Community-Services Facilitator  -  /jobs/tyeSulkhoW8-community-services-facilitator/
Company: Job Group
Salary:  $15,000 / year
Location:  Lesotho

Job Title: Government Executive  -  /jobs/yUlrEA6yWLA-government-executive/
Company: Prodder and Sons
Salary:  $10,000 / year
Location:  Comoros

Job Title: Community-Services Facilitator  -  /jobs/80MZHJ24tYs-community-services-facilitator/
Company: Dinosaur Inc
Salary:  $85,000 / year
Location:  Djibouti

Job Title: Design Strategist  -  /jobs/c3UatcBE1QM-design-strategist/
Company: Bytecard LLC
Salary:  $11,000 / year
Location:  Argentina

Job Title: Global Producer  -  /jobs/gHh_LHek0io-global-producer/
Company: Bytecard LLC
Salary:  $135,000 / year
Location:  Cayman Islands

Job Title: Government Architect  -  /jobs/DXdwUbqp97c-government-architect/
Company: Stronghold Inc
Salary:  $11,000 / year
Location:  Bhutan

Job Title: International Education Producer  -  /jobs/XOHGLv7flpU-international-education-producer/
Company: Job Group
Salary:  $96,000 / year
Location:  Cameroon

Job Title: Retail Executive  -  /jobs/Z3dpvHcYkJM-retail-executive/
Company: Flexidy Group
Salary:  $10,000 / year
Location:  Moldova

Job Title: Chief Manager  -  /jobs/j7TMjxGuyv4-chief-manager/
Company: Zathin Inc
Salary:  $17,000 / year
Location:  Lithuania

Job Title: Direct Liaison  -  /jobs/dFx4KjDp43g-direct-liaison/
Company: Andalax Inc
Salary:  $16,000 / year
Location:  Mozambique

Job Title: Healthcare Executive  -  /jobs/p_nxHyf5gvI-healthcare-executive/
Company: Trout and Sons
Salary:  $17,000 / year
Location:  French Polynesia

Job Title: Corporate Design Designer  -  /jobs/77l8XDwJhbs-corporate-design-designer/
Company: Sonair LLC
Salary:  $18,000 / year
Location:  Ghana

Job Title: National Retail Consultant  -  /jobs/hOu3xRV9sAI-national-retail-consultant/
Company: Jellyfish Inc
Salary:  $77,000 / year
Location:  Colombia

Job Title: Hospitality Architect  -  /jobs/sJqcU1SdDUk-hospitality-architect/
Company: Grasshopper and Sons
Salary:  $71,000 / year
Location:  Zimbabwe

Job Title: Corporate Technology Consultant  -  /jobs/kwRxVo6Sr5I-corporate-technology-consultant/
Company: Fish Group
Salary:  $18,000 / year
Location:  Liechtenstein

Job Title: Dynamic Education Technician  -  /jobs/CcuTAiYndDk-dynamic-education-technician/
Company: Mat Lam Tam and Sons
Salary:  $15,000 / year
Location:  Iceland

Job Title: Internal Accounting Consultant  -  /jobs/l7wkvVpaeSg-internal-accounting-consultant/
Company: Bigtax Inc
Salary:  $15,000 / year
Location:  Vietnam

Job Title: Internal Real-Estate Administrator  -  /jobs/e0SiwZ21kec-internal-real-estate-administrator/
Company: Skunk Inc
Salary:  $76,000 / year
Location:  Iraq

Job Title: Technology Representative  -  /jobs/mU6Qg9OEJJY-technology-representative/
Company: Raven Inc
Salary:  $137,000 / year
Location:  Saint Vincent and the Grenadines

Job Title: Dynamic Mining Designer  -  /jobs/7A_7bWBqxvw-dynamic-mining-designer/
Company: Serval LLC
Salary:  $12,000 / year
Location:  Macedonia

Job Title: Forward Construction Director  -  /jobs/3_sC91qo81c-forward-construction-director/
Company: Bamity Group
Salary:  $95,000 / year
Location:  Portugal

Job Title: Healthcare Technician  -  /jobs/KNYQZeTRuOc-healthcare-technician/
Company: Regrant and Sons
Salary:  $38,000 / year
Location:  Albania

Job Title: Direct Banking Facilitator  -  /jobs/3xNuBkBjTbU-direct-banking-facilitator/
Company: Tresom LLC
Salary:  $16,000 / year
Location:  Portugal

Job Title: Human Healthcare Analyst  -  /jobs/HvP7aENB7ro-human-healthcare-analyst/
Company: Otcom Inc
Salary:  $103,000 / year
Location:  Azerbaijan

Job Title: Regional Legal Executive  -  /jobs/BsiICmiDX2w-regional-legal-executive/
Company: Hyena and Sons
Salary:  $121,000 / year
Location:  Madagascar
```