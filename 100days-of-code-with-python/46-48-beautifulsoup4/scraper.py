"""
Create by Killer at 2019-05-17 15:04
"""

import requests
import bs4

# URL for want to scrape
URL = 'https://pybit.es/pages/projects.html'

def pull_site():
    raw_site_page = requests.get(URL)
    raw_site_page.raise_for_status()
    return raw_site_page


def scrape(site):
    header_list = []

    # Create BeautifulSoup object
    soup = bs4.BeautifulSoup(site.text, 'lxml')
    html_header_list = soup.select('.projectHeader')

    for headers in html_header_list:
        header_list.append(headers.getText())
    for headers in header_list:
        print(headers)

if __name__ == '__main__':
    site = pull_site()
    scrape(site)