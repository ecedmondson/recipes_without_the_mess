"""Parser and Formatter for Bon Appetit recipes."""
import bs4
import requests

# recipe_website = "https://www.bonappetit.com/recipe/spiced-lamb-burger"
# recipe_website = "https://www.bonappetit.com/recipe/manoushe-with-zaatar-oil-tomatoes-and-cucumber"
# recipe_website = "https://www.bonappetit.com/recipe/bruleed-bourbon-maple-pumpkin-pie"

class BonAppetit():
    website = "BonAppetit"
    general_url = "bonappetit.com"
    def __init__(self, url_link):
        self.url_link = url_link
        self.document = request.get(url_link)
        self.soup = bs4.BeautifulSoups(self.document.text)

    def get_ingredients(self):
        return [x.text for x in soup.find_all(attrs={"class": "ingredient"})]

    def get_steps(self):
        return [x.text for x in soup_findall(attrs={"class": "step"})]

