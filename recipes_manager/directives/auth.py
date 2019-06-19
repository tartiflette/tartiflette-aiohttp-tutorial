from typing import Any, Callable, Dict, Optional

from tartiflette import Directive


@Directive("auth")
class Auth:
    async def on_introspection(
        self,
        directive_args: Dict[str, Any],
        next_directive: Callable,
        introspected_element: Any,
        ctx: Optional[Dict[str, Any]],
        info: "Info",
    ) -> Any:
        # We limit the introspection only if the user comes from "localhost:8080"
        # This piece of code is built ONLY for tutorial purpose. Do not use this
        # in real application.
        if ctx["req"].host != "localhost:8080":
            return None

        return await next_directive(introspected_element, ctx, info)


    async def on_field_execution(
        self,
        directive_args: Dict[str, Any],
        next_resolver: Callable,
        parent_result: Optional[Any],
        args: Dict[str, Any],
        ctx: Optional[Dict[str, Any]],
        info: "Info",
    ) -> Any:
        # We limit the introspection only if the user comes from "localhost:8080"
        # This piece of code is built ONLY for tutorial purpose. Do not use this
        # in real application.
        if ctx["req"].host != "localhost:8080":
            raise Exception("You are not allowed to execute this action. Please retry from 'localhost:8080'")

        return await next_resolver(parent_result, args, ctx, info)
