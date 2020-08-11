"""Parser and Formatter for Bon Appetit recipes."""
import bs4
import requests

class BonAppetit():
    website = "BonAppetit"
    general_url = "bonappetit.com"
    prefix = "ba"
    def __init__(self, url_link):
        self.url_link = url_link
        self.document = requests.get(url_link)
        self.soup = bs4.BeautifulSoup(self.document.text, features="html.parser")

    def get_food_image(self):
        photo = self.soup.find_all(attrs={"class": "ba-picture--fit"})[0].attrs['srcset'].split(" ")
        return photo[0]

    def get_title(self):
        return [x.text for x in self.soup.find_all(attrs={"itemprop": "name"})][0]

    def get_ingredients(self):
        return [x.text for x in self.soup.find_all(attrs={"class": "ingredient"})]

    def get_steps(self):
        return [x.text for x in self.soup.find_all(attrs={"class": "step"})]

