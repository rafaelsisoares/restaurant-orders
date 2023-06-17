from src.models.ingredient import Ingredient  # noqa: F401, E261, E501

BACON_HASH = hash('bacon')
FARINHA_HASH = hash('farinha')


# Req 1
def test_ingredient():
    bacon = Ingredient('bacon')
    farinha_de_trigo = Ingredient('farinha')
    farinha_de_rosca = Ingredient('farinha')
    presunto = Ingredient('presunto')

    assert bacon != farinha_de_trigo
    assert farinha_de_trigo == farinha_de_rosca
    assert bacon.restrictions == presunto.restrictions
    assert farinha_de_trigo.name == 'farinha'
    assert hash(bacon) != hash(presunto)
    assert hash(farinha_de_trigo) == hash(farinha_de_rosca)
    assert repr(presunto) == "Ingredient('presunto')"
    assert len(bacon.restrictions) == 2
    assert len(farinha_de_rosca.restrictions) == 1
