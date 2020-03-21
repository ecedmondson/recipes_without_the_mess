import bs4
import requests

# recipe_website = "https://www.bonappetit.com/recipe/spiced-lamb-burger"
# recipe_website = "https://www.bonappetit.com/recipe/manoushe-with-zaatar-oil-tomatoes-and-cucumber"
recipe_website = "https://www.bonappetit.com/recipe/bruleed-bourbon-maple-pumpkin-pie"
html = requests.get(recipe_website)

soup = bs4.BeautifulSoup(html.text)

ingredients = [x.text for x in soup.find_all(attrs={"class": "ingredient"})]
print(ingredients)
steps = [x.text for x in soup.find_all(attrs={"class": "step"})]
print(steps)
