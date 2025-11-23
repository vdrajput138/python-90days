# Day 7

## 🚀 Mini Project: ETL Pipeline - Extract, Transform, Load


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
                    
