# Implements a secure wrapper to eval, making it easier to use.
# Based on https://realpython.com/python-eval-function/
from typing import Any


# Evaluates Python's eval() in a secure way. Makes sure:
# - Cannot evaluate functions that are not whitelisted.
# - Cannot access __builtins__ which would allow for arbitrary imports
def eval_expr(expression: str, allowed_names: dict = {}) -> Any:
    # Compile the expression
    code = compile(expression, "<string>", "eval")
    # Reject names that aren't allowed
    for name in code.co_names:
        if name not in allowed_names:
            raise NameError(f"Use of {name} not allowed")
    # Return evaluation result
    return eval(code, {"__builtins__": {}}, allowed_names)
