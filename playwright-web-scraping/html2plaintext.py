from urllib.request import urlopen
from bs4 import BeautifulSoup

# Reading HTML from a file
with open("emteller.html", "r+") as file:    
    html = file.read()


soup = BeautifulSoup(html, features="html.parser")

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
#text = soup.get_text(separator=' ')
text = soup.get_text(separator='\n', strip=True)

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)

print(text)