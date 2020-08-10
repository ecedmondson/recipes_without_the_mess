"""Parser and Formatter for Bon Appetit recipes."""
import bs4
import requests

# recipe_website = "https://www.bonappetit.com/recipe/spiced-lamb-burger"
# recipe_website = "https://www.bonappetit.com/recipe/manoushe-with-zaatar-oil-tomatoes-and-cucumber"
# recipe_website = "https://www.bonappetit.com/recipe/bruleed-bourbon-maple-pumpkin-pie"

class LeitesCulinaria():
    website = "LeitesCulinaria"
    general_url = "leitesculinaria.com"
    prefix = "lc"
    def __init__(self, url_link):
        self.url_link = url_link
        self.document = requests.get(url_link)
        self.soup = bs4.BeautifulSoup(self.document.text, features="html.parser")

    def get_food_image(self):
        photo = self.soup.find(attrs={"class": "tasty-pins-hidden-image-container"})
        if photo is not None:
            return photo.find("img").attrs["src"]
        article = self.soup.find("article").find("img")
        if article is not None:
            return article.attrs["src"]
        return None

    def get_title(self):
        return [x.text for x in self.soup.find_all(attrs={"class": "recipe-title"})][0]

    def get_ingredients(self):
        return [x.text for x in self.soup.find_all(attrs={"class": "ingredient"})]

    def get_steps(self):
        return [x.text for x in self.soup.find_all(attrs={"class": "direction"})]

