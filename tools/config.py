import argparse

def parser():
    parser = argparse.ArgumentParser()
    group = parser.add_argument_group("Recipe Parse")
    parser.add_argument("recipe_link", help="URL for recipe")    
    group.add_argument("--bon-appetit", "-ba", action="store_const", dest="action", const=BonAppetit,)
    return parser

def main():
    parser = get_parser()
    args = parser.parse_args()
    recipe = args.action(args.recipe_link)
