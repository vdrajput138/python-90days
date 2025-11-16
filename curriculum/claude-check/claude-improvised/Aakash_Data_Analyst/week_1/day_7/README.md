# Day 7

## 🚀 Mini Project: Sales Data Analysis Report Generator


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
                    
