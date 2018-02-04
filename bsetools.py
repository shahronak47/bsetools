from google import google
import pdb
from bs4 import BeautifulSoup
import requests
import urllib
from selenium import webdriver


def get_bse_link(search_quote) :
    #Appending share price BSE to get a specific search result
    google_term = search_quote + " share price BSE"
    search_results = google.search(google_term)
    for result in search_results:
        if "bseindia" in result.link:
            return result.link

def get_price_from_bse(bse_link) :
    browser = webdriver.PhantomJS()
    browser.get(bse_link)
    html = browser.page_source
    soup = BeautifulSoup(html)
    #For values which are less than previous day are shown in red
    value = soup.find('td', class_='tbmainred')
    if value is None :
        #For values which are less than previous day are shown in green
        value = soup.find('td', class_='tbmaingreen')

    return value.text.strip()


def get_quote(company_name) :
    bse_link = get_bse_link(company_name)
    share_price = get_price_from_bse(bse_link)
    print(share_price)

if __name__ == '__main__' :
    get_quote("Tech Mahindra")