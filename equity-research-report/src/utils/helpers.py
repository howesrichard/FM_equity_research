def read_commentary(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def scrape_image(url):
    import requests
    from bs4 import BeautifulSoup

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    images = soup.find_all('img')
    
    return [img['src'] for img in images if 'src' in img.attrs]