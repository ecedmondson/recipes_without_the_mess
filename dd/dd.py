"""Parser and Formatter for Food52 recipes."""
import bs4
import requests

class DimitrasDishes():
    website = "DimitrasDishes"
    general_url = "www.dimitrasdishes.com"
    prefix = "dd"
    def __init__(self, url_link):
        self.url_link = url_link
        self.document = requests.get(url_link)
        self.soup = bs4.BeautifulSoup(self.document.text, features="html.parser")

    def get_food_image(self):
        return self.soup.find(attrs={"class": "entry-content"}).find("img").attrs["src"]

    def get_title(self):
        return self.soup.find(attrs={"class": "entry-title"}).text

    def _filter_li_html_for_ingredients(self, ing):
        try:
            return "recipe__list-qty" in ing.find_next().attrs['class']
        except KeyError:
            return False

    def get_ingredients(self):
        ingredients_div = self.soup.find(attrs={"class": "mv-create-ingredients"}).find_all("li")
        return [x.text.encode('ascii', 'ignore').decode('utf-8') for x in ingredients_div]

    def get_steps(self):
        steps_div = self.soup.find(attrs={"class": "mv-create-instructions"}).find_all("li")
        return [x.text for x in steps_div]
