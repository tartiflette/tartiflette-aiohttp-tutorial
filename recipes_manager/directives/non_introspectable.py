from typing import Any, Callable, Dict, Optional

from tartiflette.directive import Directive
from tartiflette.directive import CommonDirective


@Directive("nonIntrospectable")
class NonIntrospectable(CommonDirective):
    @staticmethod
    def on_introspection(
        directive_args: Dict[str, Any],
        next_directive: Callable,
        introspected_element: Any,
        ctx: Optional[Dict[str, Any]],
        info: "Info",
    ) -> Any:
        return None
