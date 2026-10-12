# Student Performance Analytics System 📊

## About the Project

The Student Performance Analytics System is a Python-based data analytics project that analyzes student exam scores and explores the relationship between student-related factors and academic performance.

It uses Pandas, NumPy, and Matplotlib to process data, calculate statistics, identify data quality issues, and generate visualizations.

## Features

* Load and analyze student performance data using Pandas.
* Identify missing values and duplicate records.
* Detect exam scores outside the expected range.
* Calculate average, highest, and lowest exam scores.
* Classify records as Pass or Fail.
* Assign grades based on exam scores.
* Identify the ten highest-scoring records.
* Compare average scores across selected categories.
* Export analysis results to CSV files.
* Generate charts using Matplotlib.

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib

## Dataset

The project uses `StudentPerformanceFactors.csv`, containing 6,607 records and 20 columns.

The dataset includes exam scores and factors such as attendance, hours studied, motivation level, school type, and parental involvement.

**Data quality note:** The initial analysis identified missing values in three columns and one exam score above 100. These issues are flagged for investigation rather than automatically corrected.

## Project Structure

```text
STUDENT-PERFORMANCE-ANALYTICS/
├── main.py
├── StudentPerformanceFactors.csv
├── README.md
├── requirements.txt
├── student_results.csv
├── top_students.csv
├── category_analysis.csv
├── data_quality_report.csv
├── grade_distribution.png
├── pass_fail_chart.png
└── exam_score_distribution.png
```

## Installation and Execution

### 1. Install Python

Install Python 3 if it is not already installed.

### 2. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 3. Run the project

Ensure `StudentPerformanceFactors.csv` is in the same folder as `main.py`, then run:

```bash
python main.py
```

## Generated Outputs

| File                          | Description                                    |
| ----------------------------- | ---------------------------------------------- |
| `student_results.csv`         | Records with calculated grades and results     |
| `top_students.csv`            | Ten highest-scoring records                    |
| `category_analysis.csv`       | Average scores across selected categories      |
| `data_quality_report.csv`     | Missing values, duplicates, and invalid scores |
| `grade_distribution.png`      | Grade distribution chart                       |
| `pass_fail_chart.png`         | Pass/fail pie chart                            |
| `exam_score_distribution.png` | Exam score histogram                           |

## Skills Demonstrated

* Python functions and conditional statements
* Pandas DataFrame operations
* NumPy-based classification
* Data cleaning and quality checks
* Grouping and aggregation
* Exploratory data analysis
* Data visualization
* Exporting results to CSV

## Future Improvements

* Build an interactive dashboard using Streamlit.
* Add more visualizations and filters.
* Improve missing-value handling.
* Investigate and validate invalid exam scores.
* Add more detailed analytical insights.
