import requests
from bs4 import BeautifulSoup

# This function retrieves the latest headlines about Bendigo from the AFR website
def fetch_headlines(n=3):
    AFR = 'https://www.afr.com/company/asx/ben'  # URL to the company's news section on the AFR
    RawHTML = requests.get(AFR)  # Send an HTTP GET request to the webpage
    parse = BeautifulSoup(RawHTML.content, 'html.parser')  # Parse the HTML content of the page

    # Find all <h3> elements with the specified class that likely contain news headlines
    headlines = parse.find_all('h3', class_='-_73414cb90844eda9-headline')

    results = []  # Initialize an empty list to store headline text and links

    # Iterate through the top n headlines
    for headline in headlines[:n]:
        text = headline.get_text(strip=True)  # Extract the headline text and remove leading/trailing spaces
        link_tag = headline.find('a')  # Look for a link inside the <h3> tag

        # Check if a link is found and has an h reference attribute
        if link_tag and link_tag.has_attr('href'):
            link = link_tag['href']  # Extract the link URL
            if link.startswith('/'):  # If it's a relative path, convert to full URL
                link = 'https://www.afr.com' + link
            results.append((text, link))  # Save the text and full link as a tuple

    return results  # Return the list of (headline, link) pairs

# Call the function to get the top 3 headlines
headlines = fetch_headlines(3)

# Print each headline along with its clickable URL
for text, link in headlines:
    print(f"{text} ({link})")
