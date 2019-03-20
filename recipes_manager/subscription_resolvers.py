import asyncio

from tartiflette import Subscription

from recipes_manager.data import RECIPES

@Subscription("Subscription.launchAndWaitCookingTimer")
async def on_cooking_time(
    parent_result, args, ctx, info
):
  recipe = [r for r in RECIPES if r["id"] == int(args["id"])]

  if not recipe:
    raise Exception(f"The recipe with the id '{args['d']}' doesn't exist.")

  for index in range(0, recipe[0]["cookingTime"]):
    yield {
      "remainingTime": recipe[0]["cookingTime"] - index,
      "status": "COOKING"
    }
            
    await asyncio.sleep(1)
    
  yield {
    "remainingTime": 0,
    "status": "COOKED"
  }