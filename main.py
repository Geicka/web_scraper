from bs4 import BeautifulSoup as bs
import requests

class web_scraper:
# initialize class
    def __init__(self):
        pass

# load webpage content
    def load_page(self):
        URL = "https://clinicaltrials.gov/ct2/show/study/NCT04710615?draw=2"
        result = requests.get(URL)
        return result
            
# convert beautifulsoup obj
    def bs_obj(self):
        # call load_page function to use result
        lp_result = self.load_page()
        soup = bs(lp_result.content, 'html.parser')
        details = soup.find_all('div', attrs={'class_', 'tr-indent2'})
        return details

# use beautifulsoup obj to scrape
    def scrape(self):
        # call bs_obj function to use details
        obj_details = self.bs_obj()
        # pass and loop through list of objs to find and output
        for index, detail in enumerate(obj_details):
            if index == 0:
                title = detail.find("h1").get_text()
                print('Title:\n', title, '\n'*2)
            elif index == 1:
                summary = detail.find_all('div', attrs={'class_', 'ct-body3 tr-indent2'})
                if summary is not None:            
                    print('Brief Summary:\n', summary[0].get_text(), '\n'*2)
                    print('Detailed Description:\n', summary[1].get_text())
                else:
                    pass
            else:
                pass        

# class call
web_scraper().scrape()