import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, 'html.parser')

# NYT headlines are typically in <h2> or <h3> tags
for tag in soup.find_all(['h2', 'h3']):
    title = tag.get_text().strip()
    if title:
        print(title)