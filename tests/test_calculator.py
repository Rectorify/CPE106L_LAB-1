"""Resilience and input-validation tests for calculator.py.

Run with:
    pytest -q

These are black-box tests because calculator.py reads input immediately at module load.
The malformed-input tests define the desired resilient behavior: no traceback, no
non-zero exit, and a clear validation message containing "invalid".
"""

from pathlib import Path
import math
import subprocess
import sys

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = PROJECT_ROOT / "src" / "calculator.py"


def run_calculator(user_input: str) -> subprocess.CompletedProcess[str]:
    """Run calculator.py as a user would and capture its output."""
    return subprocess.run(
        [sys.executable, str(SCRIPT)],
        input=user_input,
        text=True,
        capture_output=True,
        timeout=2,
        check=False,
    )


def assert_successful_number(user_input: str, expected: float) -> None:
    result = run_calculator(user_input)
    assert result.returncode == 0, result.stderr
    assert result.stderr == ""
    actual = float(result.stdout.strip())
    assert math.isclose(actual, expected, rel_tol=1e-9, abs_tol=1e-9)


def assert_graceful_rejection(user_input: str) -> None:
    result = run_calculator(user_input)
    assert result.returncode == 0, f"Program crashed: {result.stderr}"
    assert "traceback" not in result.stderr.lower()
    assert "invalid" in result.stdout.lower()


@pytest.mark.parametrize(
    ("user_input", "expected"),
    [
        ("2 + 3\n", 5.0),
        ("9 - 4\n", 5.0),
        ("6 * 7\n", 42.0),
        ("8 / 2\n", 4.0),
        ("10 % 3\n", 1.0),
        ("-2.5 + 1.25\n", -1.25),
        ("1e3 / 2e2\n", 5.0),
        ("   2    +    3   \n", 5.0),
    ],
)
def test_valid_expressions(user_input: str, expected: float) -> None:
    assert_successful_number(user_input, expected)


@pytest.mark.parametrize(
    "user_input",
    [
        "\n",                 # empty input
        "1\n",                # too few tokens
        "1 +\n",              # missing right operand
        "+ 1 2\n",            # misplaced operator
        "1 2 +\n",            # misplaced operator
        "one + 2\n",          # non-numeric left operand
        "1 + two\n",          # non-numeric right operand
        "1 ^ 2\n",            # unsupported operator
        "1 + 2 extra\n",      # too many tokens
        "nan + 1\n",          # NaN must be rejected
        "1 + nan\n",
        "inf + 1\n",          # infinity should be rejected
        "1 + -inf\n",
    ],
)
def test_invalid_input_is_rejected_without_crashing(user_input: str) -> None:
    assert_graceful_rejection(user_input)


@pytest.mark.parametrize("user_input", ["1 / 0\n", "1 % 0\n"])
def test_zero_divisor_is_rejected_without_crashing(user_input: str) -> None:
    assert_graceful_rejection(user_input)


def test_very_large_finite_numbers_do_not_crash() -> None:
    result = run_calculator("1e308 + 1e308\n")
    assert result.returncode == 0, result.stderr
    assert "traceback" not in result.stderr.lower()
    # A hardened implementation may either reject overflow or print a result.
    assert result.stdout.strip()


def test_script_exists() -> None:
    assert SCRIPT.is_file(), f"Expected calculator script at {SCRIPT}"
