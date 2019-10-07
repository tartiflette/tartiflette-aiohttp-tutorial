import os

from aiohttp import web
from tartiflette_aiohttp import register_graphql_handlers


def run() -> None:
    """
    Entry point of the application.
    """
    web.run_app(
        register_graphql_handlers(
            app=web.Application(),
            engine_sdl=os.path.dirname(os.path.abspath(__file__)) + "/sdl",
            engine_modules=[
                "recipes_manager.query_resolvers",
                "recipes_manager.mutation_resolvers",
                "recipes_manager.subscription_resolvers",
                "recipes_manager.directives.rate_limiting",
                "recipes_manager.directives.auth",
            ],
            executor_http_endpoint="/graphql",
            executor_http_methods=["POST"],
            graphiql_enabled=True,
            subscription_ws_endpoint="/ws",
        )
    )
