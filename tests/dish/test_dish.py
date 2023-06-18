from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501
from pytest import raises

MASSA_LASANHA = Ingredient('massa de lasanha')
PARMESAO = Ingredient('queijo parmesao')
CARNE = Ingredient('carne')
CALDO_CARNE = Ingredient('caldo de carne')
PRICE = 35.5


# Req 2
def test_dish():
    picadinho = Dish('Picadinho de Carne', PRICE - 10)
    picadinho.add_ingredient_dependency(CARNE, 15)
    picadinho.add_ingredient_dependency(CALDO_CARNE, 2)
    lasanha = Dish('Lasanha', PRICE)
    lasanha.add_ingredient_dependency(MASSA_LASANHA, 2)
    lasanha.add_ingredient_dependency(PARMESAO, 3)

    assert lasanha.name == 'Lasanha'
    assert hash(lasanha) != hash(picadinho)
    assert repr(picadinho) == "Dish('Picadinho de Carne', R$25.50)"
    assert hash(lasanha) == hash(lasanha)
    assert picadinho == picadinho
    assert len(lasanha.get_ingredients()) == 2
    assert lasanha.recipe.get(PARMESAO) == 3
    for ingredient in lasanha.get_ingredients():
        assert isinstance(ingredient, Ingredient)
    assert len(picadinho.get_restrictions()) == 2
    for restriction in picadinho.get_restrictions():
        assert isinstance(restriction, Restriction)

    with raises(TypeError, match="Dish price must be float."):
        Dish('Sopa de Morcego', 'preco muito alto')

    with raises(ValueError, match="Dish price must be greater then zero."):
        Dish('Olho de porco assado', -10)
