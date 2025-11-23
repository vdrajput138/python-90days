# Day 7

## 🚀 Mini Project: Test Data Generator for QA Automation


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
                    
