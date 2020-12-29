"""Parser and Formatter for OSG recipes."""
import bs4
import requests

class OhSheGlows():
    website = "OhSheGlows"
    general_url = "ohsheglows.com"
    prefix = "osg"
    def __init__(self, url_link):
        self.url_link = url_link
        self.document = requests.get(url_link)
        self.soup = bs4.BeautifulSoup(self.document.text, features="html.parser")

    def get_food_image(self):
        photo = self.soup.find_all(attrs={"class": "post_box"})[0].find('img').attrs['src']
        return photo

    def get_title(self):
        return [x.text for x in self.soup.find_all(attrs={"class": "entry-title"})][0]

    def get_ingredients(self):
        ing_ul = self.soup.find_all(attrs={"class": "ingredients"})
        ing_li = []
        for ul in ing_ul:
            li = ul.find_all("li")
            ing_li += *li
        return [x.text for x in ing_li]

    def get_steps(self):
        return [x.text for x in self.soup.find_all(attrs={"id": "instructions"})]
