from typing import Any, Callable, Dict, Optional

import time

from tartiflette import Directive

_RATE_LIMIT_RULES = {}


def rate_limit_new_rule(name, max_attempts, duration):
    _RATE_LIMIT_RULES[name] = {
        "max_attempts": max_attempts,
        "duration": duration,
        "start_time": int(time.time()),
        "nb_attempts": 1
    }


def rate_limit_check_and_bump(name, max_attempts, duration):
    rule = _RATE_LIMIT_RULES[name]

    if int(time.time()) > (rule["start_time"] + rule["duration"]):
        rate_limit_new_rule(name, max_attempts, duration)
        return True

    _RATE_LIMIT_RULES[name]["nb_attempts"] = rule["nb_attempts"] + 1

    if rule["nb_attempts"] >= rule["max_attempts"]:
        rate_limit_new_rule(name, max_attempts, duration)
        return False

    return True


@Directive("rateLimiting")
class RateLimiting:
    async def on_field_execution(
        self,
        directive_args: Dict[str, Any],
        next_resolver: Callable,
        parent_result: Optional[Any],
        args: Dict[str, Any],
        ctx: Optional[Dict[str, Any]],
        info: "Info",
    ) -> Any:
        if not (directive_args.get('name') in _RATE_LIMIT_RULES):
            rate_limit_new_rule(
                directive_args.get('name'),
                directive_args.get("max_attempts"),
                directive_args.get("duration")
            )
        else:
            is_valid = rate_limit_check_and_bump(
                directive_args.get('name'),
                directive_args.get("max_attempts"),
                directive_args.get("duration")
            )
            if not is_valid:
                raise Exception("You reached the limit of the rate limiting")

        return await next_resolver(parent_result, args, ctx, info)
