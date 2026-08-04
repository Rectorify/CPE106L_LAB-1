# Simple Python Calculator

A minor Python project that demonstrates a command-line calculator together with automated tests using `pytest`.
The calculator accepts two numbers and one arithmetic operator, validates the input, and prints either the calculated result or `invalid`.

## Project Structure

```text
calara_johnsteven_labactivity1/
├── src/
│   └── calculator.py
├── tests/
│   └── test_calculator.py
└── README.md
```

## Supported Operations

The calculator supports the following operators:
Addition: `+`
Subtraction: `-`
Multiplication: `*`
Division: `/`
Modulo: `%`

## Input Format

Enter an expression using the following format:

```text
<number> <operator> <number>
```

Examples:

```text
2 + 3
10 / 2
7 % 3
```

The numbers and operator must be separated by spaces.

## Validation

The program prints `invalid` when:

* The input does not contain exactly two operands and one operator.
* Either operand is not a valid number.
* The operator is unsupported.
* Division or modulo by zero is attempted.
* An operand is `NaN`, positive infinity, or negative infinity.
* The result is outside the supported finite floating-point range.

## Running the Calculator

From the project root, run:

```powershell
python src/calculator.py
```

Then enter an expression:

```text
2 + 3
```

Example output:

```text
5.0
```

Invalid input produces:

```text
invalid
```

## Running the Tests

The tests use `pytest`. Install it if necessary:

```powershell
python -m pip install pytest
```

Run the tests from the project root:

```powershell
python -m pytest -q
```

For more detailed test output, run:

```powershell
python -m pytest -v
```

## Test Coverage

The test suite checks:

* Correct results for all supported operators.
* Integer, decimal, negative, and scientific-notation operands.
* Inputs containing extra whitespace.
* Missing or extra input values.
* Non-numeric operands.
* Unsupported operators.
* `NaN` and infinite values.
* Division and modulo by zero.
* Very large calculations and unexpected crashes.

## Requirements

* Python 3.9 or later
* `pytest` for running the tests

## Purpose

This project is intended as a small demonstration of:
Separating application code from test code.
Validating command-line input.
Handling invalid arithmetic operations safely.
Writing parameterized and resilience-focused tests with `pytest`.

