import collections

from tartiflette import Resolver

from recipes_manager.data import INGREDIENTS_QUANTITY, RECIPES


@Resolver("Query.recipes")
async def resolver_recipe(parent, args, ctx, info):
    return RECIPES


@Resolver("Query.recipe")
async def resolver_recipe(parent, args, ctx, info):
    recipe = [r for r in RECIPES if r["id"] == int(args["id"])]

    if not recipe:
        return None

    return recipe[0]


@Resolver("Recipe.ingredientsQuantity")
async def resolver_recipe(parent, args, ctx, info):
    if parent and parent["id"] in INGREDIENTS_QUANTITY:
        return INGREDIENTS_QUANTITY[parent["id"]]
    
    return None
