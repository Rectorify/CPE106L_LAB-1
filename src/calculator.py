import math
import operator
from collections.abc import Callable


OPERATIONS: dict[str, Callable[[float, float], float]] = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "%": operator.mod,
}


def parse_expression(expression: str) -> tuple[float, str, float]:
    """
    Parse an expression in the format:

        number operator number

    Example:
        10.5 * 2

    Raises:
        ValueError: If the expression is malformed or contains invalid values.
    """
    parts = expression.split()

    if len(parts) != 3:
        raise ValueError("Expression must contain exactly three values.")

    left_text, symbol, right_text = parts

    if symbol not in OPERATIONS:
        raise ValueError(f"Unsupported operator: {symbol}")

    try:
        left = float(left_text)
        right = float(right_text)
    except ValueError as exc:
        raise ValueError("Both operands must be numbers.") from exc

    if not math.isfinite(left) or not math.isfinite(right):
        raise ValueError("Operands must be finite numbers.")

    if symbol in {"/", "%"} and right == 0:
        raise ValueError("Division or modulo by zero is not allowed.")

    return left, symbol, right


def calculate(left: float, symbol: str, right: float) -> float:
    """
    Perform a validated arithmetic operation.

    Raises:
        ValueError: If the operator is unsupported or the result is not finite.
    """
    operation = OPERATIONS.get(symbol)

    if operation is None:
        raise ValueError(f"Unsupported operator: {symbol}")

    try:
        result = operation(left, right)
    except ZeroDivisionError as exc:
        raise ValueError("Division or modulo by zero is not allowed.") from exc
    except ArithmeticError as exc:
        raise ValueError("The calculation could not be completed.") from exc

    if not math.isfinite(result):
        raise ValueError("The result is outside the supported numeric range.")

    return result


def evaluate_expression(expression: str) -> float:
    """Parse and evaluate a complete calculator expression."""
    left, symbol, right = parse_expression(expression)
    return calculate(left, symbol, right)


def main() -> None:
    try:
        expression = input()
        result = evaluate_expression(expression)
    except (EOFError, ValueError):
        print("invalid")
    else:
        print(result)


if __name__ == "__main__":
    main()
