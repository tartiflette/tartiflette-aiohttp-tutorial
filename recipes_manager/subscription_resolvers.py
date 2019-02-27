import asyncio

from tartiflette import Resolver, Subscription

print("yop")

@Subscription("Subscription.launchAndWaitCookingTimer")
async def subscription_cooking_time(
    parent_result, args, ctx, info
):
  print("BLABLA")
  while True:
    print("Yop")
    yield {
      "remainingTime": 3,
      "status": "COOKED"
    }
            
    await asyncio.sleep(1)