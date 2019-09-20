# Dictionnary which contains the ingredients based on the recipe ID as key.
INGREDIENTS = {
    1: [
        {"name": "potato", "quantity": 10, "unitMeasurement": "UNIT"},
        {"name": "onion", "quantity": 2, "unitMeasurement": "UNIT"},
        {"name": "bacon", "quantity": 100, "unitMeasurement": "GRAM"},
        {"name": "white wine", "quantity": 0.05, "unitMeasurement": "LITER"},
        {"name": "reblochon AOP", "quantity": 1, "unitMeasurement": "UNIT"},
    ],
    2: [
        {"name": "potato", "quantity": 1000, "unitMeasurement": "GRAM"},
        {"name": "bacon", "quantity": 200, "unitMeasurement": "GRAM"},
        {"name": "onion", "quantity": 200, "unitMeasurement": "GRAM"},
        {"name": "reblochon AOP", "quantity": 1, "unitMeasurement": "UNIT"},
        {
            "name": "tablespoon of oil",
            "quantity": 2,
            "unitMeasurement": "UNIT",
        },
        {"name": "clove of garlic", "quantity": 1, "unitMeasurement": "UNIT"},
    ],
    3: [
        {"name": "potato", "quantity": 1000, "unitMeasurement": "GRAM"},
        {"name": "smoked bacon", "quantity": 200, "unitMeasurement": "GRAM"},
        {"name": "onion", "quantity": 2, "unitMeasurement": "UNIT"},
        {"name": "reblochon AOP", "quantity": 1, "unitMeasurement": "UNIT"},
        {"name": "fresh cream", "quantity": 0.100, "unitMeasurement": "LITER"},
        {"name": "butter", "quantity": 40, "unitMeasurement": "GRAM"},
        {
            "name": "tablespoon of pepper",
            "quantity": 1,
            "unitMeasurement": "UNIT",
        },
    ],
}

RECIPES = [
    {"id": 1, "name": "Tartiflette by Eric Guelpa", "cookingTime": 15},
    {"id": 2, "name": "La 'vraie' Tartiflette", "cookingTime": 20},
    {"id": 3, "name": "Tartiflette by Alain Ducasse", "cookingTime": 25},
]
