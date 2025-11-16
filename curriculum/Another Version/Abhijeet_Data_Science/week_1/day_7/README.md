# Day 7

## 🚀 Mini Project: ML Pipeline - Data Preprocessing and Model Preparation


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
                    
