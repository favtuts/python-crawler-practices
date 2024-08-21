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

Step 1. Install the Playwright Package
```sh
$ pipenv install playwright
```