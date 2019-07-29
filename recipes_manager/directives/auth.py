from typing import Any, Callable, Dict, Optional

from tartiflette import Directive


@Directive("auth")
class Auth:
    async def on_introspection(
        self,
        directive_args: Dict[str, Any],
        next_directive: Callable,
        introspected_element: Any,
        ctx: Optional[Any],
        info: "ResolveInfo",
    ) -> Any:
        # We limit the introspection only if the user comes from `localhost`.
        # This piece of code is built ONLY for tutorial purpose.
        # Do not use this in real application.
        if not ctx["req"].host.startswith("localhost"):
            return None
        return await next_directive(introspected_element, ctx, info)

    async def on_field_execution(
        self,
        directive_args: Dict[str, Any],
        next_resolver: Callable,
        parent: Optional[Any],
        args: Dict[str, Any],
        ctx: Optional[Any],
        info: "ResolveInfo",
    ) -> Any:
        # We limit the introspection only if the user comes from `localhost`.
        # This piece of code is built ONLY for tutorial purpose.
        # Do not use this in real application.
        if not ctx["req"].host.startswith("localhost"):
            raise Exception(
                "You are not allowed to execute this action. Please retry "
                "from 'localhost'"
            )
        return await next_resolver(parent, args, ctx, info)
