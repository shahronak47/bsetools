from google import google
import pdb
from bs4 import BeautifulSoup
import requests
import urllib
from selenium import webdriver


def get_bse_link(search_quote) :
    #Appending share price BSE to get a specific search result
    google_term = search_quote + " share price BSE"
    search_results = google.search(search_quote)
    for result in search_results:
        if "bseindia" in result.link:
            return result.link

def get_price_from_bse(bse_link) :
    browser = webdriver.PhantomJS()
    pdb.set_trace()
    browser.get(bse_link)
    html = browser.page_source

def get_quote(company_name) :
    bse_link = get_bse_link(company_name)
    share_price = get_price_from_bse(bse_link)

if __name__ == '__main__' :
    get_quote("Dolphin Offshore")