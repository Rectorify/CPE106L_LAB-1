# Lab Activity 1: Software Relevant Tools, Standards, and Code Versioning using GitHub

## Project Overview

The project demonstrates source-code organization, input validation, automated testing, environment management, and version control. The calculator processes a single arithmetic expression composed of two numeric operands and one supported operator.

## Development Environment

The project was developed and tested on a Windows computer in the laboratory using **Anaconda** and an isolated Conda environment named `calara_lab1`.

Ubuntu WSL was listed among the tools for the activity but was unavailable because its use was restricted by the laboratory computer's administrator permissions. Anaconda provided the Python environment used to execute the application and its automated tests.

The recorded environment configuration was:

```text
Environment: calara_lab1
Platform: Windows (win32)
Python: 3.12.13
pytest: 9.1.1
```

The Python interpreter used during testing was located at:

```text
C:\Users\jsbcalara1\.conda\envs\calara_lab1\python.exe
```

## Repository Structure

```text
calara_johnsteven_labactivity1/
├── screenshots/
│   ├── calculator_sample_runs.png
│   ├── conda_environment_activation.png
│   ├── github_commit_history.png
│   └── pytest_results.png
├── src/
│   └── calculator.py
├── tests/
│   └── test_calculator.py
└── README.md
```

### Directory and File Descriptions

- `src/calculator.py` contains the calculator application and its validation logic.
- `tests/test_calculator.py` contains the automated validation and resilience tests.
- `screenshots/` contains terminal and repository evidence collected during the activity.
- `README.md` documents the project, environment, behavior, testing, and results.

## Program Specification

The calculator accepts input in the following structure:

```text
<number> <operator> <number>
```

The operands and operator are separated by spaces. Numeric inputs are converted to floating-point values before calculation.

### Supported Operators

- `+` — addition
- `-` — subtraction
- `*` — multiplication
- `/` — division
- `%` — modulo

### Output Behavior

A valid expression produces a numeric result:

```text
Input:  2 + 3
Output: 5.0
```

Input that fails validation produces:

```text
invalid
```

## Input Validation and Resilience

The application rejects input under the following conditions:

- The expression does not contain exactly three elements.
- Either operand cannot be converted to a number.
- The operator is not supported.
- Division or modulo by zero is attempted.
- Either operand is `NaN`, positive infinity, or negative infinity.
- The calculated result is not a finite floating-point value.

Invalid input is handled without exposing an unhandled traceback during normal program execution.

## Application Execution

The calculator is executed from the project root with:

```powershell
python src\calculator.py
```

The application then reads one expression from standard input, validates it, performs the requested operation, and prints the result or `invalid`.

## Documented Sample Runs

The following cases represent the calculator behavior recorded during the activity.

### Valid Addition

```text
Input:  2 + 3
Output: 5.0
```

### Valid Division

```text
Input:  10 / 2
Output: 5.0
```

### Division by Zero

```text
Input:  10 / 0
Output: invalid
```

### Invalid Operand

```text
Input:  one + 2
Output: invalid
```

Evidence of the command-line executions is stored in `screenshots/calculator_sample_runs.png`.

## Automated Testing

Automated testing is implemented with `pytest`. The test suite runs the calculator as a separate process and evaluates its standard output, error output, exit status, and resistance to malformed input.

The suite covers:

- Addition, subtraction, multiplication, division, and modulo.
- Integer, decimal, negative, and scientific-notation operands.
- Expressions containing additional whitespace.
- Empty and incomplete input.
- Incorrect operand and operator positions.
- Non-numeric operands.
- Unsupported operators.
- Extra expression elements.
- `NaN` and infinite values.
- Division and modulo by zero.
- Very large finite operands.
- Script availability and unexpected program termination.

The test suite is executed from the project root with:

```powershell
python -m pytest -v
```

## Test Results

The recorded test session used Python 3.12.13 and pytest 9.1.1 within the active `calara_lab1` Conda environment.

```text
Collected tests: 25
Passed: 25
Failed: 0
Result: 25 passed in 1.60s
```

The completed test output is documented in `screenshots/pytest_results.png`.

## Evidence and Screenshots

The `screenshots/` directory contains supporting evidence for the laboratory activity:

- `conda_environment_activation.png` documents the active Conda environment, Python version, and interpreter path.
- `calculator_sample_runs.png` documents valid and invalid calculator executions.
- `pytest_results.png` documents the successful automated test session.
- `github_commit_history.png` documents the repository's version-control history.

## Project Results

The calculator successfully performs the five supported arithmetic operations and rejects malformed, unsupported, or unsafe input. The automated test session completed with all 25 test cases passing.

The project also satisfies the organizational requirements of the activity by separating application code, test code, documentation, and evidence into appropriate repository locations.