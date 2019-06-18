import collections

from tartiflette import Resolver

from recipes_manager.data import INGREDIENTS, RECIPES


@Resolver("Mutation.updateRecipe")
async def update_recipe(parent, args, ctx, info):
    if not args.get("input"):
        raise Exception("'input' parameter is mandatory")

    for index, recipe in enumerate(RECIPES):
        if recipe["id"] == args["input"].get("id"):
            if "name" in args["input"]:
                RECIPES[index]["name"] = args["input"]["name"]

            if "cookingTime" in args["input"]:
                RECIPES[index]["cookingTime"] = args["input"]["cookingTime"]

            return RECIPES[index]

    raise Exception("The recipe specified is not found.")
