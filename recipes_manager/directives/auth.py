from typing import Any, Callable, Dict, Optional
from urllib.parse import urlparse

from tartiflette import Directive


def _is_expected_domain(req: "yarl.URL", expected_domain: str) -> bool:
    """
    Determines whether or not the user come from the expected domain.
    :param req: incoming aiohttp request
    :param expected_domain: expected domain from which the user should come
    from
    :type req: yarl.URL
    :type expected_domain: str
    :return: whether or not the user come from the expected domain
    :rtype: bool
    """
    parsed_url = urlparse(str(req.url))
    return parsed_url.hostname == expected_domain


@Directive("auth")
class AuthDirective:
    """
    Directive to limit access to field and introspection if the user doesn't
    come from the expected domain.
    """

    async def on_introspection(
        self,
        directive_args: Dict[str, Any],
        next_directive: Callable,
        introspected_element: Any,
        ctx: Dict[str, Any],
        info: "ResolveInfo",
    ) -> Optional[Any]:
        """
        Blocks the introspection if the user doesn't come from the expected
        domain.
        :param directive_args: computed arguments related to the directive
        :param next_directive: next directive to call
        :param introspected_element: current introspected element
        :param ctx: context filled in at engine initialization
        :param info: information related to the execution and field resolution
        :type directive_args: Dict[str, Any]
        :type next_directive: Callable
        :type introspected_element: Any
        :type ctx: Dict[str, Any]
        :type info: ResolveInfo
        :return: the introspected element
        :rtype: Any
        """
        # This piece of code is built ONLY for tutorial purpose.
        # Do NOT use this in real application.
        if not _is_expected_domain(ctx["req"], directive_args["domain"]):
            return None
        return await next_directive(introspected_element, ctx, info)

    async def on_field_execution(
        self,
        directive_args: Dict[str, Any],
        next_resolver: Callable,
        parent: Optional[Any],
        args: Dict[str, Any],
        ctx: Dict[str, Any],
        info: "ResolveInfo",
    ) -> Any:
        """
        Blocks the field access if the user doesn't come from the expected
        domain.
        :param directive_args: computed arguments related to the directive
        :param next_resolver: next resolver to call
        :param parent: initial value filled in to the engine `execute` or
        `subscribe` method or field parent value
        :param args: computed arguments related to the field
        :param ctx: context filled in at engine initialization
        :param info: information related to the execution and field resolution
        :type directive_args: Dict[str, Any]
        :type next_resolver: Callable
        :type parent: Optional[Any]
        :type args: Dict[str, Any]
        :type ctx: Dict[str, Any]
        :type info: ResolveInfo
        :return: result of the field resolution
        :rtype: Any
        :raises Exception: if the user doesn't come from the expected domain
        """
        # This piece of code is built ONLY for tutorial purpose.
        # Do NOT use this in real application.
        if not _is_expected_domain(ctx["req"], directive_args["domain"]):
            raise Exception(
                "You are not allowed to execute this action. Please retry "
                f"from '{directive_args['domain']}'."
            )
        return await next_resolver(parent, args, ctx, info)
