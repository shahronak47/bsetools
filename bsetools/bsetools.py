from google import google
from bs4 import BeautifulSoup
from selenium import webdriver

class bsetools() :

    def __init__(self):
        #Constructor for this class.
        self.board = "BSE"

    def get_bse_link(self, search_quote) :
        #Appending share price BSE to get a specific search result
        google_term = search_quote + " share price BSE"
        search_results = google.search(google_term)
        for result in search_results:
            if "bseindia" in result.link:
                return result.link, True

        #If there is a wrong search term or could not find bseindia link
        return "NA", False

    def get_price_from_bse(self, bse_link) :
        browser = webdriver.PhantomJS()
        browser.get(bse_link)
        html = browser.page_source
        soup = BeautifulSoup(html, "html.parser")
        #For values which are less than previous day are shown in red
        value = soup.find('td', class_='tbmainred')
        if value is None :
            #For values which are greater than previous day are shown in green
            value = soup.find('td', class_='tbmaingreen')

        return value.text.strip()


    def get_quote(self, company_name) :
        bse_link, flag = self.get_bse_link(company_name)
        if flag :
            share_price = self.get_price_from_bse(bse_link)
            return share_price
        else :
           return "No relevant share price found for " + company_name