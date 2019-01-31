from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

def get_one_page(url):
    # Grab the page
    client = urlopen(url)
    page_html = client.read()
    client.close()
    # Does html parsing
    page = soup(page_html, 'html.parser')
    return page

def calculate_loops(entries_per_page, entries):
    if not isinstance(entries_per_page, int):
        try:
            entries_per_page = int(entries_per_page)
        except Exception as e:
            print(str(e))
            raise
    if not isinstance(entries, int):
        try:
            entries = int(entries)
        except Exception as e:
            print(str(e))
            raise

    return int(entries / entries_per_page) + 1