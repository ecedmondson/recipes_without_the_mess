import argparse
from ba.ba import BonAppetit
from lc.lc import LeitesCulinaria

def get_parser():
    parser = argparse.ArgumentParser()
    group = parser.add_argument_group("Recipe Parse")
    parser.add_argument("recipe_link", help="URL for recipe")    
    group.add_argument("--bon-appetit", "-ba", action="store_const", dest="action", const=BonAppetit,)
    group.add_argument("--leites-culinaria", "-lc", action="store_const", dest="action", const=LeitesCulinaria,)
    return parser
