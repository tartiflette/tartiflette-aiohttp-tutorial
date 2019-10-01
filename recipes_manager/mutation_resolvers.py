from typing import Any, Dict, Optional

from tartiflette import Resolver

from recipes_manager.data import RECIPES


@Resolver("Mutation.updateRecipe")
async def resolve_mutation_update_recipe(
    parent: Optional[Any],
    args: Dict[str, Any],
    ctx: Dict[str, Any],
    info: "ResolveInfo",
) -> Dict[str, Any]:
    """
    Resolver in charge of the mutation of a recipe.
    :param parent: initial value filled in to the engine `execute` method
    :param args: computed arguments related to the mutation
    :param ctx: context filled in at engine initialization
    :param info: information related to the execution and field resolution
    :type parent: Optional[Any]
    :type args: Dict[str, Any]
    :type ctx: Dict[str, Any]
    :type info: ResolveInfo
    :return: the mutated recipe
    :rtype: Dict[str, Any]
    :raises Exception: if the recipe id doesn't exist
    """
    recipe_id = args["input"]["id"]
    name = args["input"].get("name")
    cooking_time = args["input"].get("cookingTime")

    if not (name or cooking_time):
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
