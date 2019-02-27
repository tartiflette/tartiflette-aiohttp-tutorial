import collections

from tartiflette import Resolver

from recipes_manager.data import INGREDIENTS_QUANTITY, RECIPES


@Resolver("Mutation.updateRecipe")
async def resolver_recipe(parent, args, ctx, info):
    print(args["input"])
    
    recipe_input = {
        "id": 1,
        "name": "The best Tartiflette by Eric Guelpa",
        "cookingTime": 12
    }
    
    for index, recipe in enumerate(RECIPES):
        if recipe["id"] == recipe_input["id"]:
            if "name" in recipe_input:
                RECIPES[index]["name"] = recipe_input["name"]

            if "cookingTime" in recipe_input:
                RECIPES[index]["cookingTime"] = recipe_input["cookingTime"]

            return RECIPES[index]

    raise Exception("The recipe specified is not found.")
