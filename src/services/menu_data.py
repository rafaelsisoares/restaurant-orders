# Req 3
from csv import DictReader
from src.models.dish import Dish
from src.models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path
        self.dishes = self.build_menu()

    def read(self):
        with open(self.source_path) as file:
            data = list(DictReader(file))
        return data

    def build_menu(self):
        recipes = self.read()
        all_dishes = {}
        for recipe in recipes:
            if recipe["dish"] not in all_dishes:
                all_dishes[recipe["dish"]] = Dish(
                    recipe["dish"], float(recipe["price"])
                )
            current_dish = all_dishes[recipe["dish"]]
            ingredient = Ingredient(recipe["ingredient"])
            current_dish.add_ingredient_dependency(
                ingredient, int(recipe["recipe_amount"])
            )

        return set(all_dishes.values())
