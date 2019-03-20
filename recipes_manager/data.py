# Dictrionnary which contains the ingredients based on the
# Recipe ID as key.
INGREDIENTS = {
    1: [
        { "name": "potato", "quantity": 10, "type": "UNIT" },
        { "name": "onion", "quantity": 2, "type": "UNIT" },
        { "name": "bacon", "quantity": 100, "type": "GRAM" },
        { "name": "white wine", "quantity": 0.05, "type": "LITER" },
        { "name": "reblochon AOP", "quantity": 1, "type": "UNIT" }
    ],
    2: [
        { "name": "potato", "quantity": 1000, "type": "GRAM" },
        { "name": "bacon", "quantity": 200, "type": "GRAM" },
        { "name": "onion", "quantity": 200, "type": "GRAM" },
        { "name": "reblochon AOP", "quantity": 1, "type": "UNIT" },
        { "name": "tablespoon of oil", "quantity": 2, "type": "UNIT" },
        { "name": "clove of garlic", "quantity": 1, "type": "UNIT" },
    ],
    3: [
        { "name": "potato", "quantity": 1000, "type": "GRAM" },
        { "name": "smoked bacon", "quantity": 200, "type": "GRAM" },
        { "name": "onion", "quantity": 2, "type": "UNIT" },
        { "name": "reblochon AOP", "quantity": 1, "type": "UNIT" },
        { "name": "fresh cream", "quantity": 0.100, "type": "LITER" },
        { "name": "butter", "quantity": 40, "type": "GRAM" },
        { "name": "tablespoon of pepper", "quantity": 1, "type": "UNIT" },
    ]
}

RECIPES = [
    {
        "id": 1,
        "name": "Tartiflette by Eric Guelpa",
        "cookingTime": 15
    },
    {
        "id": 2,
        "name": "La 'vraie' Tartiflette",
        "cookingTime": 20
    },
    {
        "id": 3,
        "name": "Tartiflette by Alain Ducasse",
        "cookingTime": 25
    }
]