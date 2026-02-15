import requests
from bs4 import BeautifulSoup

def fetch_website_contents(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup.get_text()
