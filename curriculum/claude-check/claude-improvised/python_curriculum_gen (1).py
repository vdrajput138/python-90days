import os
import json

print("🚀 Python Curriculum Generator - Week 1 Complete Content")
print("=" * 70)

# Complete Week 1 Content for All Learners
WEEK_1_CONTENT = {
    "Viru_QA_Automation_MLOps": {
        "role": "QA Automation & MLOps Engineer",
        "week_focus": "Functions, Modules, and File Handling",
        "days": {
            "day_1": {
                "topics": [
                    "Functions - Basics",
                    "Parameters and Arguments",
                    "Return Values",
                ],
                "references": [
                    "https://realpython.com/defining-your-own-python-function/",
                    "https://www.youtube.com/watch?v=9Os0o3wzS_I (Corey Schafer - Functions)",
                    "Book: Python Crash Course by Eric Matthes - Chapter 8",
                ],
                "questions": [
                    "1. Write a function to check if a number is prime.",
                    "2. Create a function that returns the factorial of a number using recursion.",
                    "3. Write a function to calculate the area of a circle given its radius.",
                    "4. Create a function that takes a list and returns the sum of all even numbers.",
                    "5. Write a function to convert Celsius to Fahrenheit and vice versa.",
                    "6. Create a function that accepts variable number of arguments (*args) and returns their average.",
                    "7. Write a function to check if a string is a palindrome (ignore case and spaces).",
                    "8. Create a function that returns both quotient and remainder of two numbers as a tuple.",
                    "9. Write a function to find the maximum of three numbers without using max().",
                    "10. Create a function that validates if an email format is correct (basic check for @ and .).",
                ],
            },
            "day_2": {
                "topics": ["Lambda Functions", "Map, Filter, Reduce", "Function Scope"],
                "references": [
                    "https://realpython.com/python-lambda/",
                    "https://www.youtube.com/watch?v=hUes6y2b--0 (Lambda, Map, Filter)",
                    "https://docs.python.org/3/howto/functional.html",
                ],
                "questions": [
                    "1. Use lambda to create a function that squares a number and test it.",
                    "2. Use map() to convert a list of strings to uppercase.",
                    "3. Use filter() to get all even numbers from a list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].",
                    "4. Use reduce() from functools to find the product of all numbers in a list.",
                    "5. Write a lambda function to sort a list of tuples by the second element.",
                    "6. Use map() with lambda to calculate the square root of numbers in a list (hint: x**0.5).",
                    "7. Use filter() to get all strings with length > 5 from a list of words.",
                    "8. Chain map() and filter() to get squares of even numbers from [1, 2, 3, 4, 5, 6].",
                    "9. Create a lambda function that takes two arguments and returns the larger one.",
                    "10. Use reduce() to find the maximum number in a list without using max().",
                ],
            },
            "day_3": {
                "topics": [
                    "Modules - Import and Usage",
                    "Creating Custom Modules",
                    "Standard Library",
                ],
                "references": [
                    "https://realpython.com/python-modules-packages/",
                    "https://www.youtube.com/watch?v=CqvZ3vGoGs0 (Modules and Packages)",
                    "https://docs.python.org/3/tutorial/modules.html",
                ],
                "questions": [
                    "1. Create a module 'math_utils.py' with functions: add, subtract, multiply, divide.",
                    "2. Import only the 'add' and 'multiply' functions from your custom module.",
                    "3. Use the 'os' module to list all files and directories in the current directory.",
                    "4. Use 'datetime' module to get current date, time, and format it as 'DD-MM-YYYY HH:MM:SS'.",
                    "5. Create a module 'string_utils.py' with functions: reverse_string, count_vowels, capitalize_words.",
                    "6. Use 'random' module to generate 10 random integers between 1-100 and find their average.",
                    "7. Use 'math' module to calculate sine, cosine, and tangent of 45 degrees.",
                    "8. Create an alias for your module and use it to call functions (e.g., import math_utils as mu).",
                    "9. Use 'sys' module to print Python version and command line arguments.",
                    "10. Create a module for list operations (find_max, find_min, remove_duplicates) and test it.",
                ],
            },
            "day_4": {
                "topics": [
                    "File Handling - Read/Write",
                    "Working with Text Files",
                    "File Paths",
                ],
                "references": [
                    "https://realpython.com/read-write-files-python/",
                    "https://www.youtube.com/watch?v=Uh2ebFW8OYM (File Handling)",
                    "Book: Automate the Boring Stuff with Python - Chapter 9",
                ],
                "questions": [
                    "1. Write a program to create a text file and write 5 lines to it.",
                    "2. Read a text file and print its contents line by line.",
                    "3. Read a file and count the total number of lines, words, and characters.",
                    "4. Read a file and count the occurrence of a specific word (case-insensitive).",
                    "5. Append 3 new lines to an existing file without overwriting it.",
                    "6. Read a file, convert all text to uppercase, and save to a new file.",
                    "7. Copy contents from one file to another file.",
                    "8. Read a file and print only lines that contain the word 'error' or 'ERROR'.",
                    "9. Merge two text files into a third file with a separator line between them.",
                    "10. Read a file and create a dictionary with word frequencies (word: count).",
                ],
            },
            "day_5": {
                "topics": [
                    "Exception Handling",
                    "Try-Except-Finally",
                    "Raising Exceptions",
                ],
                "references": [
                    "https://realpython.com/python-exceptions/",
                    "https://www.youtube.com/watch?v=NIWwJbo-9_8 (Exception Handling)",
                    "https://docs.python.org/3/tutorial/errors.html",
                ],
                "questions": [
                    "1. Write a program that handles ZeroDivisionError when dividing two numbers.",
                    "2. Create a function that raises ValueError if input is negative.",
                    "3. Handle FileNotFoundError when trying to open a non-existent file.",
                    "4. Write a program with try-except-else-finally blocks to demonstrate all parts.",
                    "5. Create a custom exception class 'InvalidAgeError' for age validation (age must be 0-120).",
                    "6. Handle multiple exceptions (TypeError, ValueError, ZeroDivisionError) in separate blocks.",
                    "7. Write a function that validates user input and raises appropriate custom exceptions.",
                    "8. Use exception handling to safely convert a list of strings to integers.",
                    "9. Handle IndexError when accessing list elements with user input.",
                    "10. Create a program that logs exceptions to a file with timestamp and error details.",
                ],
            },
            "day_6": {
                "quiz_questions": [
                    "1. What keyword is used to define a function in Python?",
                    "2. What does a function return if no return statement is specified?",
                    "3. What is the difference between parameters and arguments?",
                    "4. Can a function return multiple values? If yes, how?",
                    "5. What is a lambda function? Give its syntax.",
                    "6. Write a lambda function to add 10 to a number.",
                    "7. What does the map() function do? What does it return?",
                    "8. What does the filter() function return?",
                    "9. Which module is required to use reduce() function?",
                    "10. What is the scope of a variable defined inside a function?",
                    "11. What is the 'global' keyword used for?",
                    "12. How do you import a specific function from a module?",
                    "13. What is the difference between 'import module' and 'from module import *'?",
                    "14. What does 'if __name__ == \"__main__\"' do?",
                    "15. How do you create an alias for a module?",
                    "16. Which function opens a file in Python?",
                    "17. What mode opens a file for appending? What about reading?",
                    "18. What is the difference between 'r' and 'rb' modes?",
                    "19. Do you need to close a file after opening it? Why?",
                    "20. What is the advantage of using 'with' statement for file handling?",
                    "21. What exception is raised when dividing by zero?",
                    "22. What is the purpose of the 'finally' block?",
                    "23. Can you have multiple except blocks for one try block?",
                    "24. What keyword is used to raise an exception manually?",
                    "25. What is the parent class of all exceptions in Python?",
                    "26. Write the syntax for try-except-else-finally.",
                    "27. What is a user-defined exception? How do you create one?",
                    "28. Can a function call itself? What is it called?",
                    "29. What are *args and **kwargs? Give examples.",
                    "30. What is the difference between local and global variables?",
                    "31. How do you pass a function as an argument to another function?",
                    "32. What is a higher-order function?",
                    "33. Can lambda functions have multiple statements?",
                    "34. What does the read() method do? What about readline()?",
                    "35. What does readline() return when end of file is reached?",
                    "36. How do you get a list of all lines in a file?",
                    "37. What module helps in working with file and directory paths?",
                    "38. What is the difference between 'a' and 'w' file modes?",
                    "39. Can you catch multiple exception types in one except block? How?",
                    "40. What happens if an exception is not caught?",
                    "41. How do you check if a file exists before opening it?",
                    "42. What is the purpose of the 'pass' statement in an except block?",
                    "43. Can you nest try-except blocks?",
                    "44. What is exception chaining (raise...from)?",
                    "45. How do you print the exception message in an except block?",
                ]
            },
            "day_7": {
                "project": {
                    "title": "Test Data Generator for QA Automation",
                    "description": """
Create a comprehensive Test Data Generator tool for QA automation testing.

REQUIREMENTS:
1. Create a module 'data_generators.py' with functions to generate:
   - Random first names (at least 20 names in a list)
   - Random last names (at least 20 surnames)
   - Random email addresses (firstname.lastname@domain.com)
   - Random phone numbers (10 digits, format: XXX-XXX-XXXX)
   - Random addresses (street, city, state, zip)
   - Random dates of birth (age range 18-80)
   - Random user IDs (alphanumeric, 8 characters)

2. Main program features:
   - Accept command line arguments for:
     * Number of records to generate
     * Output format (csv, json, txt)
     * Output filename
   - Generate test data and save to specified format
   - Handle all exceptions appropriately
   - Use functions, lambda expressions, and map/filter where applicable
   - Log all operations and errors to 'generator.log'

3. Data validation:
   - Validate generated emails (must have @ and .)
   - Validate phone numbers (must be 10 digits)
   - Ensure no duplicate user IDs

4. Output formats:
   - CSV: Headers with all fields
   - JSON: List of user objects
   - TXT: Formatted text, one user per line

5. Additional features:
   - Option to filter generated data by age range
   - Summary statistics (how many records generated, time taken)
   - Error handling with meaningful messages
   - Take screenshot of sample data in console

EXAMPLE USAGE:
python test_data_generator.py --count 100 --format csv --output testdata.csv --min-age 25 --max-age 45

SKILLS APPLIED:
- Functions and modules
- Lambda expressions
- File handling (CSV, JSON, TXT)
- Exception handling
- Command-line arguments
- Logging
- Data validation
- Random data generation
                    """,
                }
            },
        },
    },
    "Sid_Data_Engineering": {
        "role": "Data Engineer",
        "week_focus": "Advanced Python for Data Engineering",
        "days": {
            "day_1": {
                "topics": [
                    "Functions for Data Processing",
                    "Args and Kwargs",
                    "Type Hints",
                ],
                "references": [
                    "https://realpython.com/defining-your-own-python-function/",
                    "https://www.youtube.com/watch?v=9Os0o3wzS_I",
                    "Book: Python for Data Analysis by Wes McKinney - Chapter 3",
                ],
                "questions": [
                    "1. Write a function to calculate mean, median, and mode of a list of numbers.",
                    "2. Create a function that takes variable number of lists and merges them.",
                    "3. Write a function to clean null/None values from a list and return cleaned list.",
                    "4. Create a function that accepts **kwargs for database connection (host, port, user, password).",
                    "5. Write a function to flatten a nested list of any depth using recursion.",
                    "6. Create a function to calculate standard deviation of a dataset.",
                    "7. Write a function that validates data types in a list (all int, all str, mixed).",
                    "8. Create a function to merge two dictionaries with conflict resolution (keep first, keep second, or combine).",
                    "9. Write a function to remove duplicates from a list while preserving order.",
                    "10. Create a function that parses ISO date strings and returns datetime objects.",
                ],
            },
            "day_2": {
                "topics": [
                    "Functional Programming",
                    "Map, Filter, Reduce",
                    "Comprehensions",
                ],
                "references": [
                    "https://realpython.com/python-lambda/",
                    "https://www.youtube.com/watch?v=hUes6y2b--0",
                    "https://docs.python.org/3/howto/functional.html",
                ],
                "questions": [
                    "1. Use lambda with map() to normalize a list of numbers to 0-1 range (min-max scaling).",
                    "2. Use filter() to remove None, empty strings, and zero values from a mixed list.",
                    "3. Use reduce() to calculate the product of all numbers in a list.",
                    "4. Chain map() and filter(): convert strings to int, then keep only even numbers.",
                    "5. Use list comprehension to extract 'name' and 'age' from a list of dictionaries.",
                    "6. Create nested list comprehension to flatten a 2D list and filter values > 10.",
                    "7. Use dict comprehension to swap keys and values in a dictionary.",
                    "8. Combine lambda with sorted() to sort list of dicts by multiple keys.",
                    "9. Use map() to convert a list of date strings to datetime objects.",
                    "10. Use filter() with lambda to remove statistical outliers (values > 2 std deviations).",
                ],
            },
            "day_3": {
                "topics": [
                    "Modules and Packages",
                    "Virtual Environments",
                    "Requirements Management",
                ],
                "references": [
                    "https://realpython.com/python-modules-packages/",
                    "https://www.youtube.com/watch?v=CqvZ3vGoGs0",
                    "https://docs.python.org/3/tutorial/venv.html",
                ],
                "questions": [
                    "1. Create 'data_validators.py' module with functions to validate email, phone, date formats.",
                    "2. Create 'data_transformers.py' with functions: normalize, standardize, encode_categorical.",
                    "3. Import specific functions using 'from module import func1, func2'.",
                    "4. Create a virtual environment named 'data_env' and activate it.",
                    "5. Install pandas, numpy, and requests using pip in your virtual environment.",
                    "6. Create requirements.txt with all installed packages and versions.",
                    "7. Create a package 'data_utils' with __init__.py and submodules.",
                    "8. Use 'os' and 'pathlib' modules to create a directory structure for a data project.",
                    "9. Use 'sys' module to add custom module paths programmatically.",
                    "10. Create 'db_connectors.py' module with classes for different database connections.",
                ],
            },
            "day_4": {
                "topics": [
                    "File I/O - CSV, JSON, Parquet",
                    "Data Serialization",
                    "File Formats",
                ],
                "references": [
                    "https://realpython.com/read-write-files-python/",
                    "https://www.youtube.com/watch?v=Uh2ebFW8OYM",
                    "Book: Python for Data Analysis - Chapter 6",
                ],
                "questions": [
                    "1. Read a CSV file using csv module with DictReader.",
                    "2. Write a list of dictionaries to CSV with custom delimiter and headers.",
                    "3. Read a JSON file with nested structure and flatten it.",
                    "4. Write complex nested dictionary to JSON with proper indentation.",
                    "5. Use 'with' statement to safely read and write multiple files.",
                    "6. Parse CSV with different delimiters (comma, pipe, tab).",
                    "7. Handle file encoding issues (UTF-8, Latin-1) while reading international data.",
                    "8. Read a large CSV file (simulated) in chunks using generator.",
                    "9. Append new records to existing CSV without overwriting.",
                    "10. Convert data between formats: CSV to JSON and JSON to CSV.",
                ],
            },
            "day_5": {
                "topics": [
                    "Exception Handling for Data Pipelines",
                    "Logging",
                    "Error Recovery",
                ],
                "references": [
                    "https://realpython.com/python-exceptions/",
                    "https://realpython.com/python-logging/",
                    "https://docs.python.org/3/library/logging.html",
                ],
                "questions": [
                    "1. Handle FileNotFoundError and provide alternative data source.",
                    "2. Create custom exceptions: DataValidationError, DataTransformError.",
                    "3. Use try-except-else-finally for database connection with cleanup.",
                    "4. Set up logging with different handlers (console and file).",
                    "5. Log errors to file with timestamp, severity, and stack trace.",
                    "6. Create logger with different levels (DEBUG for dev, INFO for prod).",
                    "7. Handle JSON parsing errors and log malformed data.",
                    "8. Create exception handling for data type mismatches with type conversion attempts.",
                    "9. Log complete data pipeline execution: start time, steps, errors, end time.",
                    "10. Implement retry logic with exponential backoff for API calls.",
                ],
            },
            "day_6": {
                "quiz_questions": [
                    "1. What is the difference between *args and **kwargs?",
                    "2. What are type hints in Python? Give an example.",
                    "3. What does a function return by default if no return statement?",
                    "4. Can you modify a list passed as argument? Why?",
                    "5. What is a lambda function? What are its limitations?",
                    "6. What's the difference between map() and list comprehension?",
                    "7. When would you use filter() vs list comprehension with if?",
                    "8. What module is required for reduce()? Why?",
                    "9. What does functools.partial do?",
                    "10. What is a closure in Python?",
                    "11. What is a virtual environment? Why use it?",
                    "12. What command creates a virtual environment?",
                    "13. How do you activate a virtual environment?",
                    "14. What is pip? What is pip freeze?",
                    "15. What is requirements.txt and how to create it?",
                    "16. What is __init__.py for in a package?",
                    "17. What's the difference between a module and a package?",
                    "18. What does if __name__ == '__main__' mean?",
                    "19. How do you import a module from parent directory?",
                    "20. What is the difference between 'import' and 'from...import'?",
                    "21. What are the main file modes in Python?",
                    "22. What's the difference between read() and readline()?",
                    "23. What does 'with open()' do? Why use it?",
                    "24. What is the CSV module used for?",
                    "25. What's the difference between csv.reader and csv.DictReader?",
                    "26. What does json.loads() do vs json.load()?",
                    "27. What does json.dumps() do vs json.dump()?",
                    "28. What is file encoding? Name 2 common encodings.",
                    "29. How do you handle large files that don't fit in memory?",
                    "30. What is the difference between text and binary file modes?",
                    "31. What is exception handling? Why is it important?",
                    "32. What's the difference between except Exception and bare except?",
                    "33. What does the finally block do? When does it execute?",
                    "34. What is exception chaining (raise from)?",
                    "35. How do you create a custom exception?",
                    "36. What is logging? Why not just use print()?",
                    "37. What are the standard log levels in Python?",
                    "38. What's the difference between logger and logging?",
                    "39. What is a logging handler?",
                    "40. What is a logging formatter?",
                    "41. Can you have multiple except blocks? Give example.",
                    "42. What does 'raise' keyword do without arguments?",
                    "43. What is the else clause in try-except?",
                    "44. How do you log exceptions with stack trace?",
                    "45. What is the difference between assert and exception handling?",
                ]
            },
            "day_7": {
                "project": {
                    "title": "ETL Pipeline - Extract, Transform, Load",
                    "description": """
Build a complete ETL (Extract, Transform, Load) data pipeline.

REQUIREMENTS:

1. EXTRACT Module (extract.py):
   - Read data from multiple CSV files in a directory
   - Read configuration from JSON file (file paths, column mappings)
   - Handle missing files with proper exceptions
   - Support different file encodings (UTF-8, Latin-1)
   - Log all extraction activities

2. TRANSFORM Module (transform.py):
   - Data cleaning functions:
     * Remove null/None values
     * Remove duplicate rows
     * Normalize column names (lowercase, replace spaces with underscores)
     * Trim whitespace from string columns
   - Data validation:
     * Validate data types
     * Check for required fields
     * Validate email format
     * Validate date ranges
   - Data transformation:
     * Calculate derived columns (e.g., age from DOB)
     * Aggregate data (group by, sum, average)
     * Join multiple datasets
   - Log all transformation steps

3. LOAD Module (load.py):
   - Write cleaned data to new CSV
   - Generate JSON output for API consumption
   - Create summary statistics file
   - Generate data quality report (missing values, duplicates found, records processed)
   - Log loading activities

4. MAIN Pipeline (pipeline.py):
   - Orchestrate Extract -> Transform -> Load
   - Modular design with separate functions for each step
   - Comprehensive exception handling at each stage
   - Logging:
     * Console: INFO level
     * File: DEBUG level
     * Separate error log
   - Configuration file for pipeline settings
   - Command-line arguments:
     * --input-dir: Input directory path
     * --output-dir: Output directory path
     * --config: Config file path
   - Generate execution report:
     * Start time, end time, duration
     * Records extracted, transformed, loaded
     * Errors encountered
     * Data quality metrics

5. Configuration (config.json):
   {
     "input_files": ["users.csv", "transactions.csv"],
     "output_file": "cleaned_data.csv",
     "encoding": "utf-8",
     "required_columns": ["id", "name", "email"],
     "transformations": ["remove_nulls", "remove_duplicates", "validate_emails"]
   }

EXAMPLE USAGE:
python pipeline.py --input-dir ./raw_data --output-dir ./processed_data --config config.json

BONUS FEATURES:
- Parallel processing for multiple files
- Data sampling for testing
- Incremental loads (process only new data)
- Email notifications on completion/failure

SKILLS APPLIED:
- Functions and modules
- File handling (CSV, JSON)
- Exception handling
- Logging
- Command-line arguments
- Data validation and transformation
- Modular code design
                    """,
                }
            },
        },
    },
    "Aakash_Data_Analyst": {
        "role": "Data Analyst",
        "week_focus": "Python Fundamentals for Data Analysis",
        "days": {
            "day_1": {
                "topics": [
                    "Functions for Data Analysis",
                    "Statistical Functions",
                    "Return Multiple Values",
                ],
                "references": [
                    "https://realpython.com/defining-your-own-python-function/",
                    "https://www.youtube.com/watch?v=9Os0o3wzS_I",
                    "Book: Python for Data Analysis - Chapter 3",
                ],
                "questions": [
                    "1. Write a function to calculate mean, median, and mode of a dataset.",
                    "2. Create a function that returns min, max, range, and quartiles of a list.",
                    "3. Write a function to calculate percentage change between two values.",
                    "4. Create a function that normalizes a list of numbers using min-max normalization.",
                    "5. Write a function to calculate correlation coefficient between two lists.",
                    "6. Create a function that takes a list of numbers and returns outliers (values beyond 1.5*IQR).",
                    "7. Write a function to calculate moving average with specified window size.",
                    "8. Create a function that groups data by categories and returns count per category.",
                    "9. Write a function to calculate percentage distribution of values in a list.",
                    "10. Create a function that calculates year-over-year growth rate.",
                ],
            },
            "day_2": {
                "topics": [
                    "List Comprehensions",
                    "Lambda for Data Filtering",
                    "Data Transformations",
                ],
                "references": [
                    "https://realpython.com/python-lambda/",
                    "https://www.youtube.com/watch?v=hUes6y2b--0",
                    "Book: Python for Data Analysis - Chapters 3",
                ],
                "questions": [
                    "1. Use list comprehension to convert list of prices from dollars to euros (rate: 0.85).",
                    "2. Use filter() to get all transactions above $1000 from a list.",
                    "3. Use map() to calculate 10% tax on a list of prices.",
                    "4. Use list comprehension to extract all 'sales' values from list of dictionaries.",
                    "5. Chain filter() and map() to get squared values of even numbers.",
                    "6. Use dict comprehension to create category: count mapping from a list.",
                    "7. Use lambda with sorted() to sort list of dicts by 'revenue' in descending order.",
                    "8. Use list comprehension with condition to categorize values (low/medium/high).",
                    "9. Use map() to apply percentage formatting to a list of decimals.",
                    "10. Use filter() to remove incomplete records (missing required fields) from dataset.",
                ],
            },
            "day_3": {
                "topics": [
                    "Working with CSV Data",
                    "Data Import/Export",
                    "File Organization",
                ],
                "references": [
                    "https://realpython.com/python-csv/",
                    "https://www.youtube.com/watch?v=q5uM4VKywbA",
                    "https://docs.python.org/3/library/csv.html",
                ],
                "questions": [
                    "1. Read a CSV file containing sales data and print first 5 rows.",
                    "2. Read CSV and calculate total sales (sum of 'amount' column).",
                    "3. Read CSV and count records per category.",
                    "4. Read CSV and filter rows where 'status' is 'completed'.",
                    "5. Read CSV with DictReader and calculate average price.",
                    "6. Write aggregated results (category: total_sales) to new CSV.",
                    "7. Read multiple CSV files from a directory and combine them.",
                    "8. Read CSV and create summary statistics (count, mean, min, max per column).",
                    "9. Read CSV, sort by date column, and write sorted data to new file.",
                    "10. Read CSV and export filtered data to JSON format.",
                ],
            },
            "day_4": {
                "topics": [
                    "JSON Data Handling",
                    "Nested Data Structures",
                    "Data Extraction",
                ],
                "references": [
                    "https://realpython.com/python-json/",
                    "https://www.youtube.com/watch?v=9N6a-VLBa2I",
                    "https://docs.python.org/3/library/json.html",
                ],
                "questions": [
                    "1. Read JSON file containing nested customer data and extract all email addresses.",
                    "2. Parse JSON API response and extract specific fields (id, name, value).",
                    "3. Read JSON with list of transactions and calculate total amount.",
                    "4. Flatten nested JSON structure (convert nested dict to single level).",
                    "5. Read JSON and convert it to CSV format.",
                    "6. Merge two JSON files containing related data.",
                    "7. Read JSON, filter by criteria, and write filtered results to new JSON.",
                    "8. Extract data from deeply nested JSON (3+ levels deep).",
                    "9. Read JSON and create summary report with aggregations.",
                    "10. Handle malformed JSON gracefully and log errors.",
                ],
            },
            "day_5": {
                "topics": [
                    "Error Handling for Data Analysis",
                    "Data Validation",
                    "Logging Results",
                ],
                "references": [
                    "https://realpython.com/python-exceptions/",
                    "https://realpython.com/python-logging/",
                    "https://docs.python.org/3/tutorial/errors.html",
                ],
                "questions": [
                    "1. Handle missing files when loading data and provide meaningful error message.",
                    "2. Create custom exception for invalid data format (e.g., negative sales amount).",
                    "3. Validate data types in dataset and convert or raise exception appropriately.",
                    "4. Handle division by zero when calculating percentages or ratios.",
                    "5. Set up logging to track data processing steps and errors.",
                    "6. Handle empty datasets and provide appropriate default values.",
                    "7. Validate date formats and handle parsing errors.",
                    "8. Create try-except wrapper for data calculations that might fail.",
                    "9. Log summary statistics to file after each analysis run.",
                    "10. Implement data quality checks and log all validation failures.",
                ],
            },
            "day_6": {
                "quiz_questions": [
                    "1. What is the difference between mean, median, and mode?",
                    "2. How do you calculate percentage change?",
                    "3. What is data normalization? Name one technique.",
                    "4. What are outliers? How to detect them?",
                    "5. What is a moving average? When is it useful?",
                    "6. What does IQR stand for? How to calculate it?",
                    "7. What is correlation? Range of correlation coefficient?",
                    "8. What is the purpose of lambda functions?",
                    "9. What does map() function do?",
                    "10. What does filter() function return?",
                    "11. What is list comprehension syntax?",
                    "12. When to use list comprehension vs loop?",
                    "13. What is dict comprehension?",
                    "14. How to sort a list of dictionaries by a key?",
                    "15. What is the difference between sort() and sorted()?",
                    "16. What module handles CSV files?",
                    "17. What is csv.DictReader? How is it different from csv.reader?",
                    "18. How do you skip the header row in CSV?",
                    "19. What is the default delimiter in CSV module?",
                    "20. How to write headers to a CSV file?",
                    "21. What is JSON? What does it stand for?",
                    "22. What does json.load() do?",
                    "23. What does json.dumps() do? What about indent parameter?",
                    "24. How do you access nested values in JSON?",
                    "25. Can JSON have comments? Can Python dict?",
                    "26. How to convert CSV to JSON?",
                    "27. What is data validation?",
                    "28. What exception occurs when dividing by zero?",
                    "29. What exception occurs when accessing invalid list index?",
                    "30. What is a custom exception? How to create one?",
                    "31. What does 'with open()' statement do?",
                    "32. What is the finally block used for?",
                    "33. Can you have multiple except blocks?",
                    "34. What is logging? Why use it instead of print?",
                    "35. What are the log levels in Python?",
                    "36. How to log to a file?",
                    "37. What is data cleaning?",
                    "38. What are missing values? How to handle them?",
                    "39. What are duplicate records?",
                    "40. What is data aggregation?",
                    "41. What is grouping in data analysis?",
                    "42. What is a pivot table concept?",
                    "43. What is the difference between count and sum?",
                    "44. What is data filtering?",
                    "45. Why validate data before analysis?",
                ]
            },
            "day_7": {
                "project": {
                    "title": "Sales Data Analysis Report Generator",
                    "description": """
Build a Sales Data Analysis and Report Generator application.

REQUIREMENTS:

1. DATA LOADING (data_loader.py):
   - Read sales data from CSV file
   - Expected columns: date, product_id, product_name, category, quantity, unit_price, customer_id, region
   - Handle missing files gracefully
   - Validate data structure (required columns exist)
   - Log loading process

2. DATA CLEANING (data_cleaner.py):
   - Remove duplicate transactions
   - Handle missing values (remove or fill with defaults)
   - Validate data types (convert if needed)
   - Remove invalid records (negative prices/quantities)
   - Standardize date formats
   - Log all cleaning operations

3. DATA ANALYSIS (analyzer.py):
   Calculate and return:
   - Total revenue (quantity * unit_price)
   - Number of transactions
   - Number of unique products
   - Number of unique customers
   - Average transaction value
   - Revenue by category
   - Revenue by region
   - Top 5 selling products
   - Monthly revenue trend
   - Customer purchase frequency

4. REPORT GENERATION (report_generator.py):
   Create comprehensive report with:
   - Executive Summary (total revenue, transactions, growth)
   - Category Performance (revenue, percentage contribution)
   - Regional Performance (revenue by region)
   - Product Performance (top sellers, worst performers)
   - Customer Insights (total customers, average purchases)
   - Time Analysis (monthly trends, peak months)
   - Export to:
     * Text file (formatted report)
     * JSON (for further processing)
     * CSV (summary tables)

5. MAIN APPLICATION (sales_analysis.py):
   - Command-line interface
   - Arguments:
     * --input: Path to sales CSV
     * --output-dir: Directory for reports
     * --start-date: Filter from date
     * --end-date: Filter to date
   - Orchestrate: Load → Clean → Analyze → Report
   - Exception handling at each step
   - Progress logging
   - Generate execution summary

6. SAMPLE DATA STRUCTURE:
   date,product_id,product_name,category,quantity,unit_price,customer_id,region
   2024-01-15,P001,Laptop,Electronics,2,899.99,C101,North
   2024-01-16,P002,Mouse,Electronics,5,29.99,C102,South

EXAMPLE USAGE:
python sales_analysis.py --input sales_data.csv --output-dir ./reports --start-date 2024-01-01

OUTPUT FILES:
- sales_report_2024-11-16.txt
- sales_summary.json
- category_performance.csv
- analysis.log

BONUS FEATURES:
- Compare two time periods (YoY, MoM growth)
- Identify trending products (increasing sales)
- Customer segmentation (high/medium/low value)
- Generate charts (using matplotlib - if time permits)

SKILLS APPLIED:
- Functions and modules
- File I/O (CSV, JSON, TXT)
- Data cleaning and validation
- Statistical calculations
- Aggregations and grouping
- Exception handling
- Logging
- Command-line arguments
- Report formatting
                    """,
                }
            },
        },
    },
    "Abhijeet_Data_Science": {
        "role": "Data Science Developer",
        "week_focus": "Scientific Python Programming",
        "days": {
            "day_1": {
                "topics": [
                    "Functions for ML Workflows",
                    "Data Preprocessing Functions",
                    "Pipeline Functions",
                ],
                "references": [
                    "https://realpython.com/defining-your-own-python-function/",
                    "https://www.youtube.com/watch?v=9Os0o3wzS_I",
                    "Book: Python for Data Science Handbook",
                ],
                "questions": [
                    "1. Write a function to split data into train and test sets (80-20 split).",
                    "2. Create a function to normalize features using min-max scaling.",
                    "3. Write a function to standardize features (mean=0, std=1).",
                    "4. Create a function that handles missing values (mean/median/mode imputation).",
                    "5. Write a function to encode categorical variables (one-hot encoding logic).",
                    "6. Create a function to detect and cap outliers using IQR method.",
                    "7. Write a function to calculate correlation matrix from 2D data.",
                    "8. Create a function to perform train-test split with stratification (maintain class distribution).",
                    "9. Write a function to apply log transformation to skewed features.",
                    "10. Create a function that generates polynomial features (x, x^2, x^3).",
                ],
            },
            "day_2": {
                "topics": [
                    "Vectorized Operations",
                    "List Comprehensions for ML",
                    "Functional Programming",
                ],
                "references": [
                    "https://realpython.com/python-lambda/",
                    "https://www.youtube.com/watch?v=hUes6y2b--0",
                    "Book: Python for Data Science Handbook - Chapter 2",
                ],
                "questions": [
                    "1. Use list comprehension to apply sigmoid function to a list of values.",
                    "2. Use map() to apply ReLU activation (max(0, x)) to a list.",
                    "3. Use filter() to remove features with zero variance.",
                    "4. Use list comprehension to calculate squared errors between predictions and actuals.",
                    "5. Use lambda with map() to normalize each row of a 2D list.",
                    "6. Use reduce() to calculate dot product of two vectors.",
                    "7. Use list comprehension to create interaction features (x1*x2) for all pairs.",
                    "8. Use filter() and lambda to remove highly correlated features (correlation > 0.95).",
                    "9. Use map() to apply batch normalization formula to each value.",
                    "10. Use nested list comprehension to create distance matrix between points.",
                ],
            },
            "day_3": {
                "topics": [
                    "Data Pipeline Modules",
                    "Model Utilities",
                    "Configuration Management",
                ],
                "references": [
                    "https://realpython.com/python-modules-packages/",
                    "https://www.youtube.com/watch?v=CqvZ3vGoGs0",
                    "https://docs.python.org/3/tutorial/modules.html",
                ],
                "questions": [
                    "1. Create 'preprocessing.py' module with scaling, encoding, and imputation functions.",
                    "2. Create 'feature_engineering.py' with functions for creating derived features.",
                    "3. Create 'model_utils.py' with functions to save/load model artifacts.",
                    "4. Create virtual environment 'ml_env' and install numpy, pandas, scikit-learn.",
                    "5. Create requirements.txt with specific versions of ML packages.",
                    "6. Create 'metrics.py' module with functions: accuracy, precision, recall, f1_score.",
                    "7. Create package structure: ml_pipeline/data, ml_pipeline/models, ml_pipeline/utils.",
                    "8. Use 'os' module to create directory structure for ML project (data/raw, data/processed, models).",
                    "9. Create 'config.py' to store hyperparameters, file paths, and constants.",
                    "10. Create 'validators.py' module to validate input data shapes and types.",
                ],
            },
            "day_4": {
                "topics": [
                    "Data Serialization",
                    "Model Persistence",
                    "Dataset Handling",
                ],
                "references": [
                    "https://realpython.com/read-write-files-python/",
                    "https://www.youtube.com/watch?v=Uh2ebFW8OYM",
                    "Book: Hands-On Machine Learning - Chapter 2",
                ],
                "questions": [
                    "1. Read CSV dataset and split into features (X) and target (y).",
                    "2. Save preprocessed data to pickle file for later use.",
                    "3. Read JSON file containing model configuration (hyperparameters).",
                    "4. Write model training results (metrics, params) to JSON.",
                    "5. Save trained model weights/parameters to file (simulate with dict).",
                    "6. Load saved model parameters from file.",
                    "7. Read large dataset in chunks and process iteratively.",
                    "8. Write feature importance scores to CSV.",
                    "9. Save and load train-test split indices to ensure reproducibility.",
                    "10. Create data versioning: save dataset with timestamp in filename.",
                ],
            },
            "day_5": {
                "topics": [
                    "Exception Handling in ML Pipelines",
                    "Validation",
                    "Logging Experiments",
                ],
                "references": [
                    "https://realpython.com/python-exceptions/",
                    "https://realpython.com/python-logging/",
                    "https://docs.python.org/3/library/logging.html",
                ],
                "questions": [
                    "1. Handle ValueError when data shape is incorrect for model.",
                    "2. Create custom exception: InsufficientDataError (for datasets too small).",
                    "3. Validate input data: check for NaN, infinite values, correct shape.",
                    "4. Handle division by zero in metric calculations (e.g., precision when TP+FP=0).",
                    "5. Set up experiment logging: log hyperparameters, metrics, and training time.",
                    "6. Handle errors during model training and log failure details.",
                    "7. Validate feature names match between training and inference data.",
                    "8. Create try-except wrapper for data preprocessing with detailed error messages.",
                    "9. Log model performance metrics after each training run.",
                    "10. Implement data quality checks: log warnings for suspicious values (e.g., age > 150).",
                ],
            },
            "day_6": {
                "quiz_questions": [
                    "1. What is train-test split? Why is it important?",
                    "2. What is the typical train-test split ratio?",
                    "3. What is normalization? Give the formula.",
                    "4. What is standardization? How is it different from normalization?",
                    "5. What is one-hot encoding? When do you use it?",
                    "6. What are outliers? How to detect them?",
                    "7. What is the IQR method for outlier detection?",
                    "8. What is missing data imputation?",
                    "9. What are common strategies for handling missing values?",
                    "10. What is feature scaling? Why is it needed?",
                    "11. What is polynomial feature generation?",
                    "12. What is the sigmoid function? Where is it used?",
                    "13. What is ReLU activation function?",
                    "14. What is a correlation matrix?",
                    "15. What correlation value indicates strong positive correlation?",
                    "16. What is feature engineering?",
                    "17. What are interaction features?",
                    "18. What is log transformation? When to use it?",
                    "19. What is stratified sampling?",
                    "20. Why use stratification in train-test split?",
                    "21. What is vectorization? Why is it faster?",
                    "22. What is model persistence?",
                    "23. What is pickle in Python?",
                    "24. What is data versioning?",
                    "25. What is a virtual environment? Why use it in ML projects?",
                    "26. What is requirements.txt?",
                    "27. What information should you log in ML experiments?",
                    "28. What is hyperparameter tuning?",
                    "29. What is cross-validation?",
                    "30. What is overfitting? What is underfitting?",
                    "31. What are model evaluation metrics?",
                    "32. What is accuracy? When is it misleading?",
                    "33. What is precision? What is recall?",
                    "34. What is F1-score?",
                    "35. What is a confusion matrix?",
                    "36. What is the difference between classification and regression?",
                    "37. What is a pipeline in ML?",
                    "38. What is data leakage? Why is it a problem?",
                    "39. What is feature selection? Why is it important?",
                    "40. What is dimensionality reduction?",
                    "41. What is the curse of dimensionality?",
                    "42. What is a baseline model?",
                    "43. What is model validation?",
                    "44. What is batch processing of data?",
                    "45. What is the purpose of random seed/state?",
                ]
            },
            "day_7": {
                "project": {
                    "title": "ML Pipeline - Data Preprocessing and Model Preparation",
                    "description": """
Build a complete Machine Learning preprocessing pipeline from scratch.

REQUIREMENTS:

1. DATA LOADING MODULE (data_loader.py):
   - Load dataset from CSV
   - Validate data structure and types
   - Check for minimum required samples
   - Split features and target variable
   - Handle multi-class and binary classification datasets
   - Log data statistics (shape, columns, data types)

2. DATA VALIDATION MODULE (data_validator.py):
   - Check for missing values (count and percentage)
   - Detect outliers using multiple methods (IQR, Z-score)
   - Check for duplicate rows
   - Validate feature value ranges
   - Check for class imbalance in target
   - Generate data quality report

3. DATA PREPROCESSING MODULE (preprocessor.py):
   Functions to implement:
   - handle_missing_values(strategy='mean'/'median'/'mode'/'drop')
   - remove_outliers(method='iqr'/'zscore', threshold=1.5)
   - scale_features(method='minmax'/'standard')
   - encode_categorical(method='onehot'/'label')
   - remove_duplicates()
   - handle_skewness(apply_log=True)
   
4. FEATURE ENGINEERING MODULE (feature_engineer.py):
   - create_polynomial_features(degree=2)
   - create_interaction_features()
   - bin_numerical_features(n_bins=5)
   - extract_datetime_features(date_column)
   - select_features_by_correlation(threshold=0.95)
   - calculate_feature_importance_proxy()

5. TRAIN-TEST SPLIT MODULE (splitter.py):
   - train_test_split(test_size=0.2, stratify=True)
   - cross_validation_split(n_folds=5)
   - time_series_split() # for temporal data
   - Save split indices for reproducibility

6. PIPELINE ORCHESTRATOR (ml_pipeline.py):
   Main pipeline class that:
   - Loads data
   - Validates data quality
   - Applies preprocessing steps in order
   - Performs feature engineering
   - Splits data
   - Saves processed data
   - Generates comprehensive report
   - Logs all steps and decisions

7. CONFIGURATION (config.json):
   {
     "data_path": "dataset.csv",
     "target_column": "target",
     "test_size": 0.2,
     "random_state": 42,
     "preprocessing": {
       "handle_missing": "mean",
       "remove_outliers": true,
       "scaling": "standard",
       "encode_categorical": true
     },
     "feature_engineering": {
       "polynomial_degree": 2,
       "create_interactions": true,
       "remove_low_variance": true
     }
   }

8. MAIN SCRIPT (main.py):
   - Parse command-line arguments
   - Load configuration
   - Initialize pipeline
   - Run complete preprocessing
   - Generate reports:
     * Data quality report
     * Preprocessing summary
     * Feature statistics
     * Train-test split info
   - Save outputs:
     * Processed train data
     * Processed test data
     * Preprocessing artifacts (scalers, encoders)
     * Execution log

EXAMPLE USAGE:
python main.py --config config.json --input data.csv --output ./processed/

SAMPLE DATASET (Iris-like):
sepal_length,sepal_width,petal_length,petal_width,species
5.1,3.5,1.4,0.2,setosa
4.9,3.0,1.4,0.2,setosa
...

OUTPUT FILES:
- X_train.csv, y_train.csv
- X_test.csv, y_test.csv
- preprocessing_report.txt
- data_quality_report.json
- feature_stats.csv
- pipeline.log

BONUS FEATURES:
- Handle text features (TF-IDF vectorization)
- Implement SMOTE for class imbalance
- Feature importance calculation
- Automated feature selection
- Hyperparameter optimization preparation
- Save preprocessing pipeline (for deployment)

VALIDATION:
- Unit tests for each preprocessing function
- Check data shape consistency
- Verify no data leakage (test data not used in training transformations)
- Ensure reproducibility with random seeds

SKILLS APPLIED:
- Functions and modules
- OOP (Pipeline class)
- File I/O (CSV, JSON, Pickle)
- Data validation and preprocessing
- Statistical methods
- Exception handling
- Logging and reporting
- Configuration management
- Scientific computing concepts
                    """,
                }
            },
        },
    },
}


# Function to create the curriculum structure
def create_week_1_curriculum():
    base_path = os.getcwd()

    for person_name, person_data in WEEK_1_CONTENT.items():
        # Create person directory
        person_path = os.path.join(base_path, person_name)
        os.makedirs(person_path, exist_ok=True)

        # Create week_1 directory
        week_path = os.path.join(person_path, "week_1")
        os.makedirs(week_path, exist_ok=True)

        # Create README for the person
        person_readme = f"""# {person_data['role']} - Python Learning Path

## Week 1: {person_data['week_focus']}

This week focuses on building strong Python fundamentals specifically tailored for {person_data['role']}.

### Structure
- **Days 1-5**: Core learning with topics, references, and practice questions
- **Day 6**: Comprehensive quiz (45 questions)
- **Day 7**: Mini project applying the week's concepts

### Daily Commitment
- 2-3 hours of focused learning
- Complete all practice questions
- Review references thoroughly
- Take notes on key concepts

"""

        with open(os.path.join(person_path, "README.md"), "w", encoding="utf-8") as f:
            f.write(person_readme)

        # Create each day
        for day_name, day_data in person_data["days"].items():
            day_path = os.path.join(week_path, day_name)
            os.makedirs(day_path, exist_ok=True)

            # Create day README
            day_readme = f"# {day_name.replace('_', ' ').title()}\n\n"

            if "topics" in day_data:
                day_readme += "## 📚 Topics Covered\n"
                for topic in day_data["topics"]:
                    day_readme += f"- {topic}\n"
                day_readme += "\n"

            if "references" in day_data:
                day_readme += "## 🔗 Learning References\n"
                for ref in day_data["references"]:
                    day_readme += f"- {ref}\n"
                day_readme += "\n"

            if "questions" in day_data:
                day_readme += "## 💻 Practice Questions\n\n"
                day_readme += "Complete these exercises to reinforce your learning:\n\n"
                for question in day_data["questions"]:
                    day_readme += f"{question}\n\n"

            if "quiz_questions" in day_data:
                day_readme += "## 📝 Weekly Quiz\n\n"
                day_readme += "Test your understanding of this week's topics:\n\n"
                for question in day_data["quiz_questions"]:
                    day_readme += f"{question}\n\n"

            if "project" in day_data:
                day_readme += f"## 🚀 Mini Project: {day_data['project']['title']}\n\n"
                day_readme += day_data["project"]["description"]
                day_readme += "\n"

            with open(os.path.join(day_path, "README.md"), "w", encoding="utf-8") as f:
                f.write(day_readme)

            # Create practice files
            if day_name not in ["day_6", "day_7"]:
                practice_content = f"""# {day_name.replace('_', ' ').title()} - Practice Solutions

# Write your solutions below for each question
# Follow proper Python coding conventions
# Add comments to explain your logic

# Question 1
# Your solution here


# Question 2
# Your solution here


# Question 3
# Your solution here


# Question 4
# Your solution here


# Question 5
# Your solution here


# Question 6
# Your solution here


# Question 7
# Your solution here


# Question 8
# Your solution here


# Question 9
# Your solution here


# Question 10
# Your solution here

"""
                with open(
                    os.path.join(day_path, "practice.py"), "w", encoding="utf-8"
                ) as f:
                    f.write(practice_content)

            elif day_name == "day_6":
                quiz_content = f"""# Week 1 Quiz - Answer Sheet

# Write your answers below each question
# For coding questions, write the actual code
# For theory questions, write explanations

\"\"\"
Quiz Instructions:
1. Answer all 45 questions
2. For coding questions, write executable Python code
3. For theory questions, provide clear explanations
4. Take your time and think through each question
5. Review your answers before submitting

Time: 90 minutes recommended
\"\"\"

# Your answers below:

"""
                with open(
                    os.path.join(day_path, "quiz_answers.py"), "w", encoding="utf-8"
                ) as f:
                    f.write(quiz_content)

            elif day_name == "day_7":
                project_content = f"""# Week 1 Mini Project
# {person_data['days']['day_7']['project']['title']}

\"\"\"
Project Implementation

Follow the requirements outlined in README.md
Structure your code with proper functions and modules
Add comprehensive comments and docstrings
Handle exceptions appropriately
Test your code with sample data
\"\"\"

# Your implementation starts here

def main():
    \"\"\"Main function to run the project\"\"\"
    pass

if __name__ == "__main__":
    main()
"""
                with open(
                    os.path.join(day_path, "project.py"), "w", encoding="utf-8"
                ) as f:
                    f.write(project_content)


# Run the generator
if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("🎓 PYTHON CURRICULUM GENERATOR - WEEK 1 COMPLETE CONTENT")
    print("=" * 70)
    print("\nGenerating comprehensive Week 1 curriculum for all 4 learners...")
    print("\n📝 This includes:")
    print("  ✓ All topics with detailed descriptions")
    print("  ✓ Curated learning references (videos, articles, books)")
    print("  ✓ 10 practical questions per day (Days 1-5)")
    print("  ✓ 45 quiz questions (Day 6)")
    print("  ✓ Complete mini project (Day 7)")
    print("  ✓ Practice files for coding")
    print("\n" + "-" * 70)

    create_week_1_curriculum()

    print("\n✅ Week 1 Curriculum Created Successfully!")
    print("\n📁 Directory Structure:")
    for person in WEEK_1_CONTENT.keys():
        print(f"\n{person}/")
        print(f"  ├── README.md")
        print(f"  └── week_1/")
        for day in range(1, 8):
            day_name = f"day_{day}"
            print(f"      ├── {day_name}/")
            print(f"      │   ├── README.md")
            if day <= 5:
                print(f"      │   └── practice.py")
            elif day == 6:
                print(f"      │   └── quiz_answers.py")
            else:
                print(f"      │   └── project.py")

    print("\n" + "=" * 70)
    print("🚀 NEXT STEPS:")
    print("=" * 70)
    print("\n1. Navigate to your folder:")
    for person in WEEK_1_CONTENT.keys():
        role = WEEK_1_CONTENT[person]["role"]
        print(f"   cd {person}  # For {role}")

    print("\n2. Start with Day 1:")
    print("   cd week_1/day_1")
    print("   cat README.md  # Read the content")
    print("   nano practice.py  # Start coding")

    print("\n3. Follow the learning path:")
    print("   • Read all references thoroughly")
    print("   • Complete all 10 practice questions")
    print("   • Test your code")
    print("   • Move to next day")

    print("\n4. End of week:")
    print("   • Day 6: Take the quiz (45 questions)")
    print("   • Day 7: Build the mini project")

    print("\n💡 TIPS:")
    print("   • Spend 2-3 hours per day")
    print("   • Don't skip practice questions")
    print("   • Google when stuck, but try first")
    print("   • Comment your code")
    print("   • Review before moving forward")

    print("\n✨ Happy Learning! ✨\n")
    print("=" * 70 + "\n")
