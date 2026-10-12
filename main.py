import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ==========================================
# 1. FUNCTION TO CALCULATE GRADES
# ==========================================
def calculate_grade(score):
    if pd.isna(score):
        return "N/A"
    elif score >= 90:
        return "A+"
    elif score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"


# ==========================================
# 2. DATA VISUALIZATION FUNCTION
# ==========================================
def create_visualizations(df):

    # Chart 1: Grade Distribution
    grade_counts = df["Grade"].value_counts()

    grade_order = ["A+", "A", "B", "C", "D", "F", "N/A"]
    grade_counts = grade_counts.reindex(
        grade_order, fill_value=0
    )
    grade_counts = grade_counts[grade_counts > 0]

    plt.figure(figsize=(8, 5))
    grade_counts.plot(kind="bar")
    plt.title("Student Grade Distribution")
    plt.xlabel("Grade")
    plt.ylabel("Number of Records")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig("grade_distribution.png")
    plt.show()
    plt.close()

    # Chart 2: Pass vs Fail
    result_counts = df["Result"].value_counts()

    plt.figure(figsize=(6, 6))
    result_counts.plot(
        kind="pie",
        autopct="%1.1f%%",
        startangle=90
    )
    plt.title("Student Pass vs Fail")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig("pass_fail_chart.png")
    plt.show()
    plt.close()

    # Chart 3: Exam Score Distribution
    valid_scores = df["Exam_Score"].dropna()

    plt.figure(figsize=(8, 5))
    plt.hist(
        valid_scores,
        bins=10,
        edgecolor="black"
    )
    plt.title("Distribution of Exam Scores")
    plt.xlabel("Exam Score")
    plt.ylabel("Number of Records")
    plt.tight_layout()
    plt.savefig("exam_score_distribution.png")
    plt.show()
    plt.close()

    print("\nVISUALIZATION REPORT")
    print("-" * 40)
    print("Created: grade_distribution.png")
    print("Created: pass_fail_chart.png")
    print("Created: exam_score_distribution.png")


# ==========================================
# 3. MAIN PROGRAM
# ==========================================
def main():

    print("=" * 45)
    print("STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("=" * 45)

    # Load dataset
    try:
        df = pd.read_csv("StudentPerformanceFactors.csv")
    except FileNotFoundError:
        print("\nERROR: Dataset file not found!")
        print(
            "Place StudentPerformanceFactors.csv "
            "in the same folder as main.py."
        )
        return

    if df.empty:
        print("ERROR: The dataset is empty.")
        return

    if "Exam_Score" not in df.columns:
        print("ERROR: Exam_Score column is missing.")
        return

    # ==========================================
    # 4. DATA QUALITY ANALYSIS
    # ==========================================
    print("\nDATA QUALITY REPORT")
    print("-" * 40)

    print("\nMissing Values:")
    print(df.isnull().sum())

    duplicate_count = int(df.duplicated().sum())
    print("\nDuplicate Records:", duplicate_count)

    invalid_scores = df[
    (df["Exam_Score"] < 0) |
    (df["Exam_Score"] > 100)
    ]

    print("Invalid Exam Scores:", len(invalid_scores))

    if not invalid_scores.empty:
        print("\nRecords with invalid exam scores:")
        print(invalid_scores[["Exam_Score"]])

        print("\nPlease investigate these records.")

    # ==========================================
    # 5. DATASET INFORMATION
    # ==========================================
    print("\nFIRST 5 RECORDS")
    print("-" * 40)
    print(df.head())

    print("\nDATASET SHAPE")
    print(df.shape)

    print("\nCOLUMN NAMES")
    print(df.columns.tolist())

    # ==========================================
    # 6. PERFORMANCE STATISTICS
    # ==========================================
    average_score = df["Exam_Score"].mean()
    highest_score = df["Exam_Score"].max()
    lowest_score = df["Exam_Score"].min()

    print("\nSTUDENT PERFORMANCE STATISTICS")
    print("-" * 40)
    print("Total Records:", len(df))
    print("Average Exam Score:", round(average_score, 2))
    print("Highest Exam Score:", highest_score)
    print("Lowest Exam Score:", lowest_score)

    # ==========================================
    # 7. PASS AND FAIL ANALYSIS
    # ==========================================
    # Passing threshold: 60
    # Records without a score are marked N/A.
    df["Result"] = np.select(
        [
            df["Exam_Score"].isna(),
            df["Exam_Score"] >= 60
        ],
        [
            "N/A",
            "PASS"
        ],
        default="FAIL"
    )

    pass_count = int((df["Result"] == "PASS").sum())
    fail_count = int((df["Result"] == "FAIL").sum())
    ungraded_count = int((df["Result"] == "N/A").sum())

    scored_count = pass_count + fail_count

    print("\nPASS AND FAIL ANALYSIS")
    print("-" * 40)
    print("Total Records:", len(df))
    print("Passed:", pass_count)
    print("Failed:", fail_count)
    print("Records Without Scores:", ungraded_count)

    if scored_count > 0:
        pass_percentage = (pass_count / scored_count) * 100
        print("Pass Percentage:", round(pass_percentage, 2), "%")
    else:
        print("Pass Percentage: N/A")

    # ==========================================
    # 8. GRADE ASSIGNMENT
    # ==========================================
    df["Grade"] = df["Exam_Score"].apply(calculate_grade)

    print("\nGRADE DISTRIBUTION")
    print("-" * 40)
    print(df["Grade"].value_counts())

    print("\nFIRST 10 RECORDS WITH RESULTS")
    print("-" * 40)
    print(
        df[["Exam_Score", "Result", "Grade"]].head(10)
    )

    # ==========================================
    # 9. TOP 10 PERFORMING RECORDS
    # ==========================================
    top_students = df.nlargest(10, "Exam_Score")

    print("\nTOP 10 PERFORMING RECORDS")
    print("-" * 40)
    print(
        top_students[["Exam_Score", "Result", "Grade"]]
    )

    # ==========================================
    # 10. CATEGORY-WISE ANALYSIS
    # ==========================================
    categories = [
        "Gender",
        "School_Type",
        "Motivation_Level",
        "Parental_Involvement"
    ]

    print("\nCATEGORY-WISE PERFORMANCE ANALYSIS")
    print("-" * 40)

    category_results = []

    for category in categories:

        if category not in df.columns:
            print(f"\nSkipping {category}: column not found.")
            continue

        print(f"\nAverage Exam Score by {category}:")

        averages = df.groupby(category)["Exam_Score"].mean()
        print(averages.round(2))

        for group_name, average in averages.items():
            category_results.append({
                "Category": category,
                "Group": group_name,
                "Average_Exam_Score": round(average, 2)
                if pd.notna(average) else np.nan
            })

    # ==========================================
    # 11. EXPORT STUDENT RESULTS
    # ==========================================
    df.to_csv("student_results.csv", index=False)
    print("\nSaved: student_results.csv")

    top_students.to_csv("top_students.csv", index=False)
    print("Saved: top_students.csv")

    category_df = pd.DataFrame(
        category_results,
        columns=[
            "Category",
            "Group",
            "Average_Exam_Score"
        ]
    )

    category_df.to_csv("category_analysis.csv", index=False)
    print("Saved: category_analysis.csv")

    # ==========================================
    # 12. EXPORT DATA QUALITY REPORT
    # ==========================================
    missing_values = df.isnull().sum()

    quality_report = pd.DataFrame({
        "Column": missing_values.index,
        "Missing_Values": missing_values.values
    })

    total_missing = int(df.isnull().sum().sum())

    summary_rows = pd.DataFrame([
        {
            "Column": "ALL_COLUMNS_TOTAL",
            "Missing_Values": total_missing
        },
        {
            "Column": "DUPLICATE_RECORDS",
            "Missing_Values": duplicate_count
        },
        {
            "Column": "INVALID_EXAM_SCORES",
            "Missing_Values": len(invalid_scores)
        }
    ])

    quality_report = pd.concat(
        [quality_report, summary_rows],
        ignore_index=True
    )

    quality_report.to_csv(
        "data_quality_report.csv",
        index=False
    )

    print("Saved: data_quality_report.csv")

    # ==========================================
    # 13. CREATE VISUALIZATIONS
    # ==========================================
    print("\nCreating visualizations...")

    create_visualizations(df)

    # ==========================================
    # 14. COMPLETION MESSAGE
    # ==========================================
    print("\n" + "=" * 45)
    print("PROJECT EXECUTION COMPLETED SUCCESSFULLY!")
    print("=" * 45)


# ==========================================
# 15. RUN THE PROGRAM
# ==========================================
if __name__ == "__main__":
    main()