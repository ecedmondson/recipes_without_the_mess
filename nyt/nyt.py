"""Parser and Formatter for NYT ecipes."""
import bs4
import requests

class NYT():
    website = "New York Times Cooking"
    general_url = "cooking.newyorktimes.com"
    prefix = "nyt"
    def __init__(self, url_link):
        self.url_link = url_link
        self.document = requests.get(url_link)
        self.soup = bs4.BeautifulSoup(self.document.text, features="html.parser")

    def get_food_image(self):
        photo = self.soup.find(attrs={"class": "media-container"}).find("img").attrs['src']
        return photo

    def get_title(self):
        return [x.text for x in self.soup.find_all(attrs={"class": "recipe-title"})][0]

    def get_ingredients(self):
        return [x.text for x in self.soup.find_all(attrs={"class": "recipe-ingredients-wrap"})]

    def get_steps(self):
        return [x.text for x in self.soup.find_all(attrs={"class": "recipe-steps-wrap"})]
