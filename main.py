import os
import pandas as pd
import numpy as np

FILE_NAME = "students"
SUBJECTS = ["Maths", "Physics", "Chemistry", "English", "Computer"]
PASS_MARK = 50


def load_data(filename):
    return pd.read_csv(f"{filename}.csv")


def calculate_average(total):
    return total / len(SUBJECTS)


def assign_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= PASS_MARK:
        return "D"
    else:
        return "F"


def check_pass_fail(average):
    if average >= PASS_MARK:
        return "Pass"
    else:
        return "Fail"


def main():
    df = load_data(FILE_NAME)

    print("\n=== DATASET PREVIEW ===")
    print(df.head().to_string(index=False))
    print("\nNumber of students:", len(df))
    print("Columns:", list(df.columns))

    marks = df[SUBJECTS].to_numpy()
    df["Total"] = np.sum(marks, axis=1)

    averages = []
    grades = []
    results = []
    for total in df["Total"]:
        average = calculate_average(total)
        averages.append(round(average, 2))
        grades.append(assign_grade(average))
        results.append(check_pass_fail(average))

    df["Average"] = averages
    df["Grade"] = grades
    df["Result"] = results

    print("\n=== STUDENT RESULTS ===")
    print(df[["Student_ID", "Name", "Total", "Average", "Grade", "Result"]].to_string(index=False))

    print("\n=== CLASS SUMMARY ===")
    print("Highest total marks:", np.max(df["Total"]))
    print("Lowest total marks: ", np.min(df["Total"]))
    print("Overall class average:", round(np.mean(df["Average"]), 2))

    print("\n=== SUBJECT-WISE ANALYSIS ===")
    best_subject = ""
    best_subject_average = -1
    for subject in SUBJECTS:
        values = df[subject].to_numpy()
        subject_average = round(np.mean(values), 2)
        print(subject, "-> average:", subject_average,
              "| highest:", np.max(values),
              "| lowest:", np.min(values))
        if subject_average > best_subject_average:
            best_subject = subject
            best_subject_average = subject_average
    print("Best subject:", best_subject, "with average", best_subject_average)

    print("\n=== PASS / FAIL ===")
    passed = len(df[df["Result"] == "Pass"])
    print("Students passed:", passed)
    print("Students failed:", len(df) - passed)

    print("\n=== GRADE COUNT ===")
    for grade in ["A", "B", "C", "D", "F"]:
        print("Grade", grade, ":", len(df[df["Grade"] == grade]), "students")

    print("\n=== TOP 3 STUDENTS ===")
    top_students = df.sort_values(by="Average", ascending=False).head(3)
    rank = 1
    for index, row in top_students.iterrows():
        print(rank, "-", row["Name"], "with average", row["Average"])
        rank = rank + 1


if __name__ == "__main__":
    main()
