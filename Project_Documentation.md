# Student Performance Analytics System

## 1. Introduction

The Student Performance Analytics System is a Python-based data analysis project developed to analyze student examination performance. It uses Pandas and NumPy to process and analyze data and Matplotlib to create visualizations.

The project generates performance summaries, classifies examination scores into grades, identifies pass and fail results, compares performance across different categories, and checks data quality.

## 2. Project Objective

The main objectives of this project are:

* To analyze examination scores using Python.
* To calculate grades based on examination scores.
* To classify students as pass or fail.
* To compare average scores across different categories.
* To identify missing values, duplicate records, and invalid scores.
* To represent findings using charts.
* To export analysis results into CSV files.

## 3. Technologies Used

| Technology | Purpose                                            |
| ---------- | -------------------------------------------------- |
| Python     | Main programming language                          |
| Pandas     | Data loading, cleaning, manipulation, and analysis |
| NumPy      | Numerical operations and pass/fail classification  |
| Matplotlib | Data visualization                                 |
| CSV        | Dataset storage and analytical report export       |
| Git        | Version control                                    |
| GitHub     | Project hosting and sharing                        |

## 4. Dataset Description

The project uses a dataset named `StudentPerformanceFactors.csv`.

The dataset contains 6,607 records and 20 columns. It includes examination scores and factors that may be associated with student performance.

Examples of columns include:

* Hours_Studied
* Attendance
* Previous_Scores
* Sleep_Hours
* Tutoring_Sessions
* Motivation_Level
* Parental_Involvement
* School_Type
* Gender
* Exam_Score

The dataset contains information about study habits, educational circumstances, and examination performance.

**Note:** The original dataset is excluded from the public GitHub repository. Users must obtain the dataset separately from an authorized source before running the project.

## 5. Project Implementation

### 5.1 Data Loading

Pandas is used to load the dataset from a CSV file into a DataFrame.

### 5.2 Data Quality Analysis

The system checks for:

* Missing values
* Duplicate records
* Examination scores outside the expected range of 0–100

The results are exported to `data_quality_report.csv`.

### 5.3 Grade Calculation

The system assigns grades according to the following rules:

| Examination Score | Grade |
| ----------------- | ----- |
| 90 and above      | A+    |
| 80–89             | A     |
| 70–79             | B     |
| 60–69             | C     |
| 50–59             | D     |
| Below 50          | F     |

### 5.4 Pass/Fail Classification

The system classifies examination scores of 60 or above as PASS and scores below 60 as FAIL.

### 5.5 Category-Wise Analysis

The system calculates average examination scores for categories such as:

* Gender
* School Type
* Motivation Level
* Parental Involvement

These comparisons describe differences in the dataset and do not establish that any particular factor causes higher or lower scores.

### 5.6 Top Performers

The system identifies the ten records with the highest examination scores and exports them to `top_students.csv`.

Because the dataset does not contain student names or IDs, these records cannot be linked to named individuals.

### 5.7 Data Visualization

Matplotlib is used to generate charts showing:

* Grade distribution
* Pass/fail distribution
* Examination score distribution

## 6. Project Files

| File                          | Description                          |
| ----------------------------- | ------------------------------------ |
| `main.py`                     | Main Python program                  |
| `README.MD`                   | Project overview and instructions    |
| `REQUIREMENTS.TXT`            | Required Python libraries            |
| `.gitignore`                  | Specifies files excluded from Git    |
| `category_analysis.csv`       | Category-wise analysis results       |
| `data_quality_report.csv`     | Data quality findings                |
| `student_results.csv`         | Processed examination results        |
| `top_students.csv`            | Top ten examination-score records    |
| `grade_distribution.png`      | Grade distribution chart             |
| `pass_fail_chart.png`         | Pass/fail chart                      |
| `exam_score_distribution.png` | Examination score distribution chart |

## 7. Results

The program successfully processed the dataset and generated the analytical reports and charts.

The recorded analysis produced the following findings:

* Total records analyzed: 6,607
* Duplicate records detected: 0
* Missing values were found in three columns: Teacher_Quality, Parental_Education_Level, and Distance_from_Home.
* One examination score was identified outside the expected 0–100 range.
* The system generated grade classifications, pass/fail results, category-wise comparisons, and a top-ten score report.

The program's original pass/fail classification counted 6,539 records as PASS and 68 as FAIL. The classification used the rule that scores of 60 or above are PASS.

These figures describe the recorded program output. Invalid scores should be reviewed before using the results for formal reporting.

## 8. Learning Outcomes

Through this project, the following concepts were practiced:

* Python programming fundamentals
* Variables, conditions, loops, and functions
* Pandas DataFrames
* NumPy operations
* Data quality checks
* Descriptive data analysis
* Group-wise comparisons
* Data visualization
* CSV file handling
* Git and GitHub version control

## 9. Limitations and Future Improvements

Potential improvements include:

* Handling invalid scores before calculating final statistics.
* Adding a more comprehensive data-cleaning process.
* Improving chart labels and presentation.
* Adding an interactive dashboard.
* Allowing users to upload their own datasets.
* Adding unit tests to verify calculations.
* Improving error handling when input files are missing.

## 10. Conclusion

The Student Performance Analytics System demonstrates how Python libraries can be used to process a dataset, evaluate examination scores, inspect data quality, summarize performance, and generate visual reports.

The project provides practical experience in data analysis, data visualization, report generation, and version control. It also establishes a foundation for more advanced data analytics projects.

## 11. GitHub Repository

Project repository:

https://github.com/KumariShail/student-performance-analytics
