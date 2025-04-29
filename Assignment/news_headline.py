import requests
from bs4 import BeautifulSoup

# Reading in AFR URL for Bendigo Website
AFR = 'https://www.afr.com/company/asx/ben'
RawHTML = requests.get(AFR)

# Parse the raw HTML using BeautifulSoup
parse = BeautifulSoup(RawHTML.content, 'html.parser')

# Find recent AFR headlines by filtering to publication-specific format
headlines = parse.find_all('h3', class_='-_73414cb90844eda9-headline')

# Pull and print the most recent 10 headlines
for headline in headlines[:10]:
    print(headline.get_text(strip=True))