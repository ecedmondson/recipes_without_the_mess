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
        return self.soup.find(attrs={"class": "recipe-image"}).find_next().attrs['data-src']

    def get_title(self):
        return self.soup.find(attrs={"class": "recipe-title-header"}).find_next().text

    def _filter_li_html_for_ingredients(self, ing):
        try:
            return "recipe__list-qty" in ing.find_next().attrs['class']
        except KeyError:
            return False

    def get_ingredients(self):
        lis = list(filter(lambda x: not bool(x.attrs), self.soup.find(attrs={"class": "recipe-ingredients"}).children))[0]
        return [x.text.encode('ascii', 'ignore').decode('utf-8') for x in lis.children]

    def get_steps(self):
        unicode_ = "\u200b"
        thing = [x.text.find(unicode_) for x in self.soup.find_all(attrs={"class": "step"})]
        print(thing)
