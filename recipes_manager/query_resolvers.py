import collections

from tartiflette import Resolver

from recipes_manager.data import INGREDIENTS, RECIPES


@Resolver("Query.recipes")
async def resolve_recipes(parent, args, ctx, info):
    return RECIPES


@Resolver("Query.recipe")
async def resolve_recipe(parent, args, ctx, info):
    recipe = [r for r in RECIPES if r["id"] == int(args["id"])]

    if not recipe:
        return None

    return recipe[0]


@Resolver("Recipe.ingredients")
async def resolve_ingredients(parent, args, ctx, info):
    if parent and parent["id"] in INGREDIENTS:
        return INGREDIENTS[parent["id"]]
    
    return None
