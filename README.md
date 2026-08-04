# Lab Activity 1: Software Tools, Standards, and Git Version Control

## Overview

This repository documents the completion of Lab Activity 1 for **CPE106L-4 Software Design Laboratory**. The activity focused on preparing a clean Python laboratory workspace, using an isolated Python environment, organizing source and test files, establishing a Git repository, and recording evidence of basic version-control operations.

A simple command-line calculator was used as the Python program for demonstrating the required workspace, execution, testing, documentation, and Git workflow.

## Objectives

The activity was completed to demonstrate the following objectives:

1. Create a clean and organized Python laboratory workspace.
2. Prepare an isolated Python environment for the project.
3. Develop and test a basic Python program.
4. Initialize and maintain a local Git repository.
5. Connect the local repository to GitHub.
6. Perform and document basic Git operations, including staging, committing, pulling, rebasing, and pushing changes.
7. Submit evidence of program execution, testing, environment configuration, and version-control history.

## Laboratory Environment

The prescribed activity identified Ubuntu WSL as the intended workspace. However, WSL was unavailable on the laboratory computer because its use required administrator permissions. To complete the environment-management objective, **Anaconda Prompt** and a Conda environment named `calara_lab1` were used as the permitted alternative.

The recorded laboratory environment was:

```text
Operating platform: Windows (win32)
Environment manager: Anaconda / Conda
Environment name: calara_lab1
Python version: 3.12.13
pytest version: 9.1.1
```

The active Python interpreter during testing was:

```text
C:\Users\jsbcalara1\.conda\envs\calara_lab1\python.exe
```

The use of Conda preserved the main purpose of the virtual-environment objective by isolating the Python interpreter and test dependencies from the base environment.

## Workspace Organization

The project uses separate directories for source code, automated tests, and supporting evidence.

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

### Workspace Components

- `src/calculator.py` contains the Python calculator program.
- `tests/test_calculator.py` contains the automated input-validation and resilience tests.
- `screenshots/` contains evidence of the environment, program execution, test results, and Git history.
- `README.md` documents the completed activity and its results.

Temporary Python files and cache directories, such as `__pycache__/` and `.pytest_cache/`, are not part of the required project deliverables.

## Python Environment

The isolated project environment was created and activated through Conda. The relevant environment operations were:

```powershell
conda create --name calara_lab1 python=3.12
conda activate calara_lab1
python -m pip install pytest
```

Environment activation was verified using:

```powershell
conda info --envs
python --version
where python
```

The verification output showed `calara_lab1` as the active environment and confirmed that Python was executed from the environment-specific interpreter path.

After a development or testing session, the environment can be closed with:

```powershell
conda deactivate
```

Evidence of the active environment is stored in:

```text
screenshots/conda_environment_activation.png
```

## Demonstration Program

The project uses a command-line calculator to demonstrate Python development and testing within the prepared workspace.

The calculator accepts expressions in the following format:

```text
<number> <operator> <number>
```

The supported operators are:

- `+` for addition
- `-` for subtraction
- `*` for multiplication
- `/` for division
- `%` for modulo

A valid expression produces a floating-point result. Invalid expressions produce the message `invalid` without exposing an unhandled traceback during normal execution.

The program validates malformed expressions, unsupported operators, non-numeric operands, non-finite values, and division or modulo by zero.

The application was executed from the project root using:

```powershell
python src\calculator.py
```

## Program Execution Evidence

The documented sample runs include valid and invalid expressions.

```text
Input:  2 + 3
Output: 5.0

Input:  10 / 2
Output: 5.0

Input:  10 / 0
Output: invalid

Input:  one + 2
Output: invalid
```

The corresponding terminal evidence is stored in:

```text
screenshots/calculator_sample_runs.png
```

## Automated Testing

The test suite uses `pytest` to evaluate the calculator as a separate process. The tests verify correct output, input validation, exit behavior, and resilience against malformed expressions.

The test coverage includes:

- All five supported arithmetic operators
- Integer, decimal, negative, and scientific-notation operands
- Additional whitespace
- Empty and incomplete expressions
- Incorrect token positions
- Non-numeric operands
- Unsupported operators
- Extra input elements
- `NaN` and infinite values
- Division and modulo by zero
- Very large numeric inputs
- Unexpected program termination

The test suite was executed with:

```powershell
python -m pytest -v
```

The recorded result was:

```text
Tests collected: 25
Tests passed: 25
Tests failed: 0
Completion time: 1.60 seconds
```

The full test-session evidence is stored in:

```text
screenshots/pytest_results.png
```

## Git Repository and Version Control

A Git repository was established for the project to track changes to the source code, tests, documentation, and screenshots. The repository uses the `main` branch and is connected to a remote GitHub repository.

The basic version-control workflow demonstrated in the activity included:

```powershell
git status
git add .
git commit -m "Descriptive commit message"
git pull --rebase origin main
git push origin main
git log --oneline
```

These operations documented the following version-control concepts:

- Inspecting the working tree
- Staging project changes
- Creating meaningful commits
- Reviewing commit history
- Integrating remote changes
- Resolving a README merge conflict during rebase
- Synchronizing the local `main` branch with GitHub

The repository contains more than the required three meaningful commits. The commit history records the initial repository setup, project documentation, additional screenshot evidence, README revisions, and final documentation updates.

Git commit-history evidence is stored in:

```text
screenshots/github_commit_history.png
```

The remote repository is available at:

https://github.com/Rectorify/CPE106L_LAB-1

## Evidence Summary

The project evidence is organized in the `screenshots/` directory:

- `conda_environment_activation.png` — active Conda environment, Python version, and interpreter path
- `calculator_sample_runs.png` — valid and invalid calculator executions
- `pytest_results.png` — automated test execution showing 25 passing tests
- `github_commit_history.png` — GitHub commit history showing meaningful version-control activity

## Results

The activity produced an organized Python workspace with separate source, test, documentation, and evidence components. An isolated Conda environment was used in place of WSL because of laboratory administrator restrictions. The calculator executed correctly, and all 25 automated tests passed.

The Git repository documented the development process through multiple meaningful commits and was synchronized with GitHub. The screenshots provide evidence of environment activation, program execution, automated testing, and basic version-control operations.

## Submission Contents

The submitted project folder contains:

```text
README.md
src/calculator.py
tests/test_calculator.py
screenshots/
```

The complete folder is uploaded to the designated Drive location with link access enabled for evaluation. The GitHub repository provides an additional copy of the source files and the recorded version-control history.

## Author

**John Steven B. Calara**  
CPE106L-4 Software Design Laboratory
