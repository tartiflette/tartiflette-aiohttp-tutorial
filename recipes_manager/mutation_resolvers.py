from tartiflette import Resolver

from recipes_manager.data import RECIPES


@Resolver("Mutation.updateRecipe")
async def resolve_mutation_update_recipe(parent, args, ctx, info):
    recipe_id = args["input"]["id"]
    name = args["input"].get("name")
    cooking_time = args["input"].get("cookingTime")

    if not (name and cooking_time):
        raise Exception(
            "You should provide at least one value for either name or "
            "cookingTime."
        )

    for index, recipe in enumerate(RECIPES):
        if recipe["id"] == recipe_id:
            if name:
                RECIPES[index]["name"] = name
            if cooking_time:
                RECIPES[index]["cookingTime"] = cooking_time
            return RECIPES[index]

    raise Exception(f"The recipe < {recipe_id} > does not exist.")
