from google import google
from bs4 import BeautifulSoup
from selenium import webdriver
import collections

class bsetools() :

    def __init__(self):
        #Constructor for this class.
        self.board = "BSE"
        self.bse_website = "https://www.bseindia.com/"

    def __get_bse_link(self, search_quote) :
        #Appending share price BSE to get a specific search result
        google_term = search_quote + " share price BSE"
        search_results = google.search(google_term)
        for result in search_results:
            if "bseindia" in result.link:
                return result.link, True

        #If there is a wrong search term or could not find bseindia link
        return "NA", False

    def get_BSE_index(self):
        browser = webdriver.PhantomJS()
        browser.get(self.bse_website)
        html = browser.page_source
        soup = BeautifulSoup(html, "html.parser")
        Sensex = collections.namedtuple('Sensex', ['bse_index', 'diff'])
        Sensex.bse_index =  soup.find('div', class_='newsensexvalue').text.strip()
        Sensex.diff = soup.find('div', class_='newsensextext2').text.strip()
        #Check if index returned is float, replacing commas with empty space so that it is easy to convert into float and check
        if isinstance(float(Sensex.bse_index.replace(',', '')), float) :
            return Sensex

        return "Cannot find index now"

    def __get_price_from_bse(self, bse_link) :
        browser = webdriver.PhantomJS()
        browser.get(bse_link)
        html = browser.page_source
        soup = BeautifulSoup(html, "html.parser")
        #For values which are less than previous day are shown in red
        quote = soup.find('td', class_='tbmainred')
        if quote is None :
            #For values which are greater than previous day are shown in green
            quote = soup.find('td', class_='tbmaingreen')
        #Remove all tags and html class information and capture only value
        quote = quote.text.strip()
        diff_than_yesterday = soup.find('td', class_='tbmainsmallred')
        #Check if number which we have captured is float
        if isinstance(float(quote), float) :
            return quote, diff_than_yesterday.text.strip()

        return "Cannot find price", ""

    def get_quote(self, company_name) :
        bse_link, flag = self.__get_bse_link(company_name)
        if flag :
            share_price = self.__get_price_from_bse(bse_link)
            return share_price
        else :
            #Return relevant error message and empty bse index link in case there is no bse_link found
           return "No relevant share price found for " + company_name