from tools.config import get_parser
from tools.html import HTMLTemplate

def main():
    parser = get_parser()
    args = parser.parse_args()
    recipe = args.action(args.recipe_link)
    template = HTMLTemplate(recipe.get_ingredients(), recipe.get_steps(), recipe.get_title(), recipe.get_food_image(), args.recipe_link, recipe.website, recipe.general_url, recipe.prefix)
    template.write_recipe()

main()
