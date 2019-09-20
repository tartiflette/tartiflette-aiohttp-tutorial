from tartiflette import Resolver

from recipes_manager.data import INGREDIENTS, RECIPES


@Resolver("Query.recipes")
async def resolve_query_recipes(parent, args, ctx, info):
    return RECIPES


@Resolver("Query.recipe")
async def resolve_query_recipe(parent, args, ctx, info):
    for recipe in RECIPES:
        if recipe["id"] == args["id"]:
            return recipe
    return None


@Resolver("Recipe.ingredients")
async def resolve_recipe_ingredients(parent, args, ctx, info):
    if parent and parent["id"] in INGREDIENTS:
        return INGREDIENTS[parent["id"]]
    return None
