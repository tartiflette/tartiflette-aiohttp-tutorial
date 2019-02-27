import os
from aiohttp import web

from tartiflette import Engine
from tartiflette_aiohttp import register_graphql_handlers

import recipes_manager.query_resolvers
import recipes_manager.mutation_resolvers
import recipes_manager.subscription_resolvers


# Tartiflette Engine, the only one :)
# Will load the SDL files from the ./sdl folder
engine = Engine(
    os.path.dirname(os.path.abspath(__file__)) + "/sdl"
)


def run():
    app = web.Application()

    web.run_app(
        register_graphql_handlers(
            app=app,
            engine=engine,
            subscription_ws_endpoint="/ws",
            executor_http_endpoint='/graphql',
            executor_http_methods=['POST'],
            graphiql_enabled=True
        )
    )