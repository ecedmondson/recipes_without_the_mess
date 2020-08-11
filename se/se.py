"""Parser and Formatter for Bon Appetit recipes."""
import bs4
import requests
import sys
from http.client import HTTPConnection # py3
import logging

HTTPConnection.debuglevel = 1
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

class SeriousEats():
    website = "SeriousEats"
    general_url = "seriouseats.com"
    prefix = "se"
    def __init__(self, url_link):
        self.url_link = url_link
        print(self.url_link)
        print(url_link)	
        self.document = requests.get(url_link, headers={"Accept": "*/*"}, verify=False)
        self.soup = bs4.BeautifulSoup(self.document.text, features="html.parser")

    def get_food_image(self):
        return self.soup.find(attrs={"class": "recipe-main-photo thumb-large"})       

    def get_title(self):
        return [x.text for x in self.soup.find_all(attrs={"itemprop": "name"})][0]

    def get_ingredients(self):
        return [x.text for x in self.soup.find_all(attrs={"class": "ingredient"})]

    def get_steps(self):
        return [x.text for x in self.soup.find_all(attrs={"class": "step"})]

s = SeriousEats("https://www.seriouseats.com/recipes/2019/10/french-onion-soup-tarte-tatin.html")
i = s.get_food_image()
print(i)
