"""Formatting an HTML document out of retrieved recipe data"""
li = "    <li>{ITEM}</li>\n"

def ordered(items):
    items.insert(0, "<ol>\n")
    items.append("</ol>\n")
    return items

def unordered(items):
    items.insert(0, "<ul>\n")
    items.append("</ul>\n")
    return items

class HTMLTemplate():
    def __init__(self, ingredients, steps, title, image, recipe_link, source, home, prefix):
        self.ingredients = ingredients
        self.steps = steps
        self.title = title
        self.image = image
        self.recipe_link = recipe_link
        self.source = source
        self.home = home
        self.prefix = prefix

    def read_template(self):
        template = open("templates/recipe_template.html", "r")
        lines = template.readlines()
        template.close()
        return lines

    def format_steps(self):
        steps = [li.replace("{ITEM}", x) for x in self.steps]
        return ordered(steps)

    def format_ingredients(self):
        ingredients = [li.replace("{ITEM}", x) for x in self.ingredients]
        return unordered(ingredients)

    def write_recipe(self):
        template = self.read_template()
        # Replace {TITLE}
        template = [x.replace("{TITLE}", self.title) if "{TITLE}" in x else x for x in template]
        # Replace {IMG}
        template = [x.replace("{IMG}", self.image)if "{IMG}" in x else x for x in template]
        # Replace {INGREDIENTS}
        str = [x for x in template if "{INGREDIENTS}" in x][0]
        ind = template.index(str)
        first_half = template[:ind]
        second_half = template[ind + 1:]
        template = first_half + self.format_ingredients() + second_half
        # Replace {STEPS}
        str = [x for x in template if "{STEPS}" in x][0]
        ind = template.index(str)
        first_half = template[:ind]
        second_half = template[ind + 1:]
        template = first_half + self.format_steps() + second_half
        # Repalce {GENERAL}
        template = [x.replace("{GENERAL}", self.home) if "{GENERAL}" in x else x for x in template]
        # Replace {WEBSITE}, which is the home source of the recipe
        template = [x.replace("{WEBSITE}", self.source) if "{WEBSITE}" in x else x for x in template]
        # Replace {URL}, which is the url to the original recipe
        template = [x.replace("{URL}", self.recipe_link) if "{URL}" in x else x for x in template]
        title = self.title.replace(" ", "_")
        file = open(f"templates/{self.prefix}/{self.prefix}_{title.lower()}.html", "w+")
        for line in template:
            file.write(line)
        file.close()

        

    

    
    
