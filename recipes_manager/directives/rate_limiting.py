from typing import Any, Callable, Dict, Optional

from tartiflette.directive import Directive
from tartiflette.directive import CommonDirective


@Directive("rateLimiting")
class RateLimiting(CommonDirective):
    @staticmethod
    async def on_execution(
        _directive_args: Dict[str, Any],
        next_resolver: Callable,
        parent_result: Optional[Any],
        args: Dict[str, Any],
        ctx: Optional[Dict[str, Any]],
        info: "Info",
    ) -> Any:
        _key = f"ratelimiting_{_directive_args.get('name')}"
        _max_attemps = _directive_args.get("max_attempts")
        _duration = _directive_args.get("duration")
        cached_value = await ctx["app"]["redis"].get(_key)

        if cached_value:
            cached_value = int(cached_value)
            if cached_value <= 0:
                print(f"@rateLimiting({_key}: {_duration}s): rate limited")
                raise Exception("You reached the limit of the rate limiting")
            _max_attemps = cached_value - 1

        await ctx["app"]["redis"].setex(_key, _duration, str(_max_attemps))
        print(f"@rateLimiting({_key}: {_duration}s): {_max_attemps}")
        return await next_resolver(parent_result, args, ctx, info)
