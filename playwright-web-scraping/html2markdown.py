from urllib.parse import urljoin
import html2text
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


# Reading HTML from a file
with open("emteller.html", "r+") as file:    
    html = file.read()


# Make absolute links
soup = BeautifulSoup(html, features="html.parser")
url = 'https://emteller.vn/'
MakeAbsoluteLinks(url, soup)

html = soup.prettify()

text_maker = html2text.HTML2Text()
text_maker.ignore_links = True
markdown_text = text_maker.handle(html)
print(markdown_text)

# save markdown to file
with open('emteller.md', 'w', encoding='utf-8') as f:
    f.write(markdown_text)
