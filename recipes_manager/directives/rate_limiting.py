import time

from typing import Any, Callable, Dict, Optional

from tartiflette import Directive

_RATE_LIMIT_RULES = {}


def rate_limit_new_rule(name, max_attempts, duration):
    _RATE_LIMIT_RULES[name] = {
        "max_attempts": max_attempts,
        "duration": duration,
        "start_time": int(time.time()),
        "nb_attempts": 1,
    }


def rate_limit_check_and_bump(name, max_attempts, duration):
    rule = _RATE_LIMIT_RULES[name]

    if int(time.time()) > (rule["start_time"] + rule["duration"]):
        rate_limit_new_rule(name, max_attempts, duration)
        return True

    _RATE_LIMIT_RULES[name]["nb_attempts"] += 1

    return rule["nb_attempts"] <= rule["max_attempts"]


@Directive("rateLimiting")
class RateLimiting:
    async def on_field_execution(
        self,
        directive_args: Dict[str, Any],
        next_resolver: Callable,
        parent: Optional[Any],
        args: Dict[str, Any],
        ctx: Optional[Any],
        info: "ResolveInfo",
    ) -> Any:
        if directive_args["name"] not in _RATE_LIMIT_RULES:
            rate_limit_new_rule(
                directive_args["name"],
                directive_args["maxAttempts"],
                directive_args["duration"],
            )

        is_valid = rate_limit_check_and_bump(
            directive_args["name"],
            directive_args["maxAttempts"],
            directive_args["duration"],
        )
        if not is_valid:
            raise Exception("You reached the limit of the rate limiting")
        return await next_resolver(parent, args, ctx, info)
