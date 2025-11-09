#!/usr/bin/env python3
"""
Smart Week 01 – Python Basics Generator
---------------------------------------
Creates folders for days 1–6 (Sunday skipped)
Adds unique topic-based problems for each role
Updates/creates tracker.md
"""

from datetime import date, timedelta
from pathlib import Path

# -------------------------------------------------------------------
# Week configuration
# -------------------------------------------------------------------
WEEK_NAME   = "week_01_basics"
START_DATE  = date(2025, 11, 12)           # Wed Nov 12 2025
DAYS_ACTIVE = 6

ROLES = {
    "aakash_data_science" : "Data Science",
    "abhijit_data_science": "Data Science",
    "sid_data_engineering": "Data Engineering",
    "viru_qa"             : "QA Automation"
}

TOPICS = [
    "Python Setup + Syntax",
    "Variables & Data Types",
    "Input/Output & Operators",
    "Conditional Statements",
    "Loops (for/while)",
    "Practice & Mini Quiz"
]

# -------------------------------------------------------------------
# Role-specific problems by topic
# -------------------------------------------------------------------
PROBLEMS = {
    "Python Setup + Syntax": {
        "Data Science": [
            "Install Python 3.10 and verify the version.",
            "Write a simple program to print your name and goal.",
            "Use comments and docstrings correctly in a script.",
            "Run a Python file from command line and Jupyter.",
            "Explore `dir()` and `help()` on `math` module."
        ],
        "Data Engineering": [
            "Check Python 3 installation and create a virtual env.",
            "Write a script that prints system path and Python version.",
            "Create a `.py` that reads command-line args and prints them.",
            "Explore `os` and `sys` modules to list current directory files.",
            "Write a short script printing memory usage (psutil if available)."
        ],
        "QA Automation": [
            "Install Python and `pytest` in a virtual env.",
            "Write a basic script printing 'QA Automation Setup OK'.",
            "Create a pytest test that asserts 2 + 2 == 4.",
            "Write and run a test file using `pytest -v`.",
            "Document how to install dependencies via `requirements.txt`."
        ]
    },
    "Variables & Data Types": {
        "Data Science": [
            "Create variables of each data type and print types.",
            "Swap two variables without a temp variable.",
            "Write a program converting string input to int, float, bool.",
            "Perform arithmetic and logical operations on sample numbers.",
            "Challenge: Implement BMI calculator using variables."
        ],
        "Data Engineering": [
            "Store configuration details in a dict and print keys.",
            "Demonstrate mutable vs immutable objects with examples.",
            "Convert list → tuple → set and back.",
            "Write code that parses comma-separated input into list of ints.",
            "Challenge: Summarize numeric list with min, max, avg."
        ],
        "QA Automation": [
            "Declare variables for test details and print them.",
            "Write a script that asserts type correctness using `assert isinstance()`.",
            "Simulate login credentials and mask password output.",
            "Demonstrate use of f-strings for formatted test reports.",
            "Challenge: Create parameterized pytest test that checks data types."
        ]
    },
    "Input/Output & Operators": {
        "Data Science": [
            "Take user input of height & weight, calculate BMI.",
            "Accept two numbers and show results of +, -, *, /, %, **.",
            "Convert a list of numbers into their squares.",
            "Function converting Celsius ↔ Fahrenheit.",
            "Challenge: Read 5 numbers and print average (2 decimals)."
        ],
        "Data Engineering": [
            "Read CSV lines from console, split and print columns.",
            "Perform arithmetic on integer inputs and log to file.",
            "Write a program showing difference between `//` and `/`.",
            "Use logical operators to validate numeric ranges.",
            "Challenge: Simulate simple calculator via functions."
        ],
        "QA Automation": [
            "Take user input for username/password and validate rules.",
            "Compare equality/identity of two variables using asserts.",
            "Write pytest to check addition/multiplication results.",
            "Combine logical conditions to validate test outcomes.",
            "Challenge: Build small CLI that asks for 3 numbers and validates sum."
        ]
    },
    "Conditional Statements": {
        "Data Science": [
            "Write program checking if number is positive, negative, or zero.",
            "Find largest among 3 numbers using if/elif/else.",
            "Check leap year using nested if.",
            "Assign grade based on score input.",
            "Challenge: Build mini calculator with if-based menu."
        ],
        "Data Engineering": [
            "Validate file extension (.csv/.json) using if/else.",
            "Check if directory exists, else create one.",
            "Program: compare two strings ignoring case.",
            "Use ternary operator for quick comparison.",
            "Challenge: Determine environment (dev/prod) from input."
        ],
        "QA Automation": [
            "Write script verifying HTTP status code 200 → PASS else FAIL.",
            "Create pytest that marks tests PASS/FAIL using conditions.",
            "Simulate test skipping based on feature flag.",
            "Use assert + if to compare expected vs actual output.",
            "Challenge: Design test that validates even/odd numbers using parametrize."
        ]
    },
    "Loops (for/while)": {
        "Data Science": [
            "Use for-loop to print numbers 1–10.",
            "Compute factorial using while-loop.",
            "Print even numbers between 1–50.",
            "Iterate over list of tuples and unpack values.",
            "Challenge: Generate Fibonacci ≤ 100."
        ],
        "Data Engineering": [
            "Loop through lines of text file and count words.",
            "Use enumerate() to print line numbers.",
            "Simulate retry logic (3 attempts) with while-loop.",
            "Break/continue example processing mixed data.",
            "Challenge: Read log file & count ‘ERROR’ entries."
        ],
        "QA Automation": [
            "Loop through list of test cases and print names.",
            "Use while-loop to retry failed test until pass or limit 3.",
            "Collect pytest test names via loop & display summary.",
            "Demonstrate nested loops with test suites/tests.",
            "Challenge: Count passed/failed tests using loop over dict."
        ]
    },
    "Practice & Mini Quiz": {
        "Data Science": [
            "Create list of 10 numbers and compute sum & avg.",
            "Build dict of student→score and print top 3.",
            "Write function returning square of each list element.",
            "Combine loops & conditions to count even/odd numbers.",
            "Challenge: Mini project – analyze small dataset (hardcoded)."
        ],
        "Data Engineering": [
            "Parse sample CSV string into list of dicts.",
            "Read config dict and print all key/value pairs.",
            "Write function to validate and transform user input.",
            "Generate synthetic data list using loops.",
            "Challenge: Combine data from 2 lists into list of tuples."
        ],
        "QA Automation": [
            "Create pytest fixture returning browser name.",
            "Write test verifying multiplication table 5 × 1-10.",
            "Use for-loop inside pytest test to validate multiple inputs.",
            "Combine assert + loop to check all items in list are > 0.",
            "Challenge: Mini pytest suite validating math functions."
        ]
    }
}

# -------------------------------------------------------------------
ROOT = Path(__file__).resolve().parent
PROBLEMS_DIR = ROOT / "problems" / WEEK_NAME
TRACKER_FILE = ROOT / "tracker.md"

# -------------------------------------------------------------------
def make_day_folder(day_num: int, topic: str, current_date: date):
    day_path = PROBLEMS_DIR / f"day_{day_num:02d}"
    day_path.mkdir(parents=True, exist_ok=True)

    for role, track in ROLES.items():
        role_path = day_path / role
        role_path.mkdir(exist_ok=True)
        probs = PROBLEMS[topic][track]

        md_file = role_path / "problem_list.md"
        content = [f"# Day {day_num} – {topic}",
                   f"**Date:** {current_date.strftime('%b %d, %Y')}  ",
                   f"**Track:** {track}", "", "---", "", "## Problems"]
        for i, p in enumerate(probs, 1):
            content.append(f"{i}. {p}")
        content += [
            "", "---", "",
            "## Resources",
            "- [Python Docs](https://docs.python.org/3/)",
            "- [W3Schools Python](https://www.w3schools.com/python/)",
            "- [YouTube – Telusko](https://www.youtube.com/@Telusko)", "",
            "---", "",
            "**Review Rotation:** Aakash → Abhijit → Sid → Viru → Aakash", "",
            "| Member | Status |",
            "|:--|:--|",
            "| Aakash | [ ] |",
            "| Abhijit | [ ] |",
            "| Sid | [ ] |",
            "| Viru | [ ] |"
        ]
        md_file.write_text("\n".join(content), encoding="utf-8")

        nb_file = role_path / f"day_{day_num:02d}_{role.split('_')[0]}.ipynb"
        nb_file.write_text("""{
 "cells": [
  {"cell_type": "markdown","metadata":{},"source":["# Day {day_num} – {topic}\\nWrite your solutions below."]},
  {"cell_type":"code","execution_count":null,"metadata":{},"outputs":[],"source":[]}
 ],
 "metadata":{"kernelspec":{"display_name":"Python 3","language":"python","name":"python3"}},
 "nbformat":4,"nbformat_minor":5
}""".replace("{day_num}", str(day_num)).replace("{topic}", topic), encoding="utf-8")

# -------------------------------------------------------------------
def update_tracker():
    header = "| Day | Date | Topic | Aakash | Abhijit | Sid | Viru |\n|:--|:--|:--|:--|:--|:--|:--|\n"
    lines, cur_date, day = [], START_DATE, 1
    while day <= DAYS_ACTIVE:
        if cur_date.weekday() == 6:  # skip Sunday
            cur_date += timedelta(days=1)
            continue
        lines.append(f"| {day} | {cur_date.strftime('%b %d')} | {TOPICS[day-1]} | [ ] | [ ] | [ ] | [ ] |\n")
        cur_date += timedelta(days=1)
        day += 1

    new_block = f"\n## Week 01 – Python Basics\n\n{header}{''.join(lines)}\n"
    if TRACKER_FILE.exists():
        old = TRACKER_FILE.read_text(encoding="utf-8")
        TRACKER_FILE.write_text(old + new_block, encoding="utf-8")
    else:
        TRACKER_FILE.write_text("# Team Python 90-Day Tracker\n" + new_block, encoding="utf-8")

# -------------------------------------------------------------------
def main():
    print("🚀 Creating Smart Week 01 – Python Basics structure...")
    cur_date, day = START_DATE, 1
    while day <= DAYS_ACTIVE:
        if cur_date.weekday() == 6:
            cur_date += timedelta(days=1)
            continue
        make_day_folder(day, TOPICS[day-1], cur_date)
        cur_date += timedelta(days=1)
        day += 1
    update_tracker()
    print(f"✅ Week 01 created successfully at {PROBLEMS_DIR}")

if __name__ == "__main__":
    main()
