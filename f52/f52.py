"""Parser and Formatter for Food52 recipes."""
import bs4
import requests

class Food52():
    website = "Food52"
    general_url = "food52.com"
    prefix = "f52"
    def __init__(self, url_link):
        self.url_link = url_link
        self.document = requests.get(url_link)
        self.soup = bs4.BeautifulSoup(self.document.text, features="html.parser")

    def get_food_image(self):
        return self.soup.find(attrs={"class": "img__pin"}).attrs['data-pin-media']

    def get_title(self):
        return [x.text for x in self.soup.find_all(attrs={"class": "recipe__title"})][0]

    def _filter_li_html_for_ingredients(self, ing):
        try:
            return "recipe__list-qty" in ing.find_next().attrs['class']
        except KeyError:
            return False

    def get_ingredients(self):
        lis = self.soup.find_all("li")
        ingredients = list(filter(self._filter_li_html_for_ingredients, lis))
        return[x.text.replace('\n', " ").strip() for x in ingredients]

    def get_steps(self):
        return [x.text for x in self.soup.find_all(attrs={"class": "recipe__list-step"})]
