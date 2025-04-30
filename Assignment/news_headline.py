import requests
from bs4 import BeautifulSoup

def fetch_headlines(n=3):
    AFR = 'https://www.afr.com/company/asx/ben'
    RawHTML = requests.get(AFR)
    parse = BeautifulSoup(RawHTML.content, 'html.parser')

    headlines = parse.find_all('h3', class_='-_73414cb90844eda9-headline')

    results = []
    for headline in headlines[:n]:
        text = headline.get_text(strip=True)
        link_tag = headline.find('a')
        if link_tag and link_tag.has_attr('href'):
            link = link_tag['href']
            if link.startswith('/'):
                link = 'https://www.afr.com' + link
            results.append((text, link))
    return results

headlines = fetch_headlines(3)

for text, link in headlines:
    print(f"{text} ({link})")