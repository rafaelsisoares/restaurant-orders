from csv import DictReader
from typing import Dict

from src.models.dish import Recipe
from src.models.ingredient import Ingredient

BASE_INVENTORY = "data/inventory_base_data.csv"

Inventory = Dict[Ingredient, int]


def read_csv_inventory(inventory_file_path=BASE_INVENTORY) -> Dict:
    inventory = dict()

    with open(inventory_file_path, encoding="utf-8") as file:
        for row in DictReader(file):
            ingredient = Ingredient(row["ingredient"])
            inventory[ingredient] = int(row["initial_amount"])

    return inventory


# Req 5
class InventoryMapping:
    def __init__(self, inventory_file_path=BASE_INVENTORY) -> None:
        self.inventory = read_csv_inventory(inventory_file_path)

    # Req 5.1
    def check_recipe_availability(self, recipe: Recipe):
        ingredient = list(recipe.keys())[0]
        amount = list(recipe.values())[0]
        if (
            ingredient in self.inventory.keys()
            and self.inventory[ingredient] >= amount
        ):
            return True
        return False

    # Req 5.2
    def consume_recipe(self, recipe: Recipe) -> None:
        if recipe.keys():
            if not self.check_recipe_availability(recipe):
                raise ValueError("Recipe not available")
            ingredients = list(recipe.keys())
            amount = list(recipe.values())
            for i in range(len(ingredients)):
                self.inventory[ingredients[i]] -= amount[i]
