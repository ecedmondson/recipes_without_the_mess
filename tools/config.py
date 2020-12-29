import argparse
from ba.ba import BonAppetit
from lc.lc import LeitesCulinaria
from f52.f52 import Food52
from dd.dd import DimitrasDishes
from nyt.nyt import NYT
from osg.osg import OhSheGlows

def get_parser():
    parser = argparse.ArgumentParser()
    group = parser.add_argument_group("Recipe Parse")
    parser.add_argument("recipe_link", help="URL for recipe")    
    group.add_argument("--bon-appetit", "-ba", action="store_const", dest="action", const=BonAppetit,)
    group.add_argument("--leites-culinaria", "-lc", action="store_const", dest="action", const=LeitesCulinaria,)
    group.add_argument("--food52", "-f52", action="store_const", dest="action", const=Food52,)
    group.add_argument("--dimitras-dishes", "-dd", action="store_const", dest="action", const=DimitrasDishes,)
    group.add_argument("--nyt-cooking", "-nyt", action="store_const", dest="action", const=NYT,)
    group.add_argument("--oh-she-glows", "-osh", action="store_const", dest="action", const=OSG,)
    return parser
