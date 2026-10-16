"""
Report Card Management System
-----------------------------
Libraries : pandas (data handling), csv/os (file storage), matplotlib (charts)
Storage   : students_records.csv (created automatically in the same folder)

Features
  1. Add a student's record (name, class, roll no, section, marks)
  2. View all records
  3. Search a student (by roll number or name)
  4. Print a student's report card (total, percentage, grade, result)
  5. Class statistics (topper, subject averages, pass/fail count)
  6. Chart: one student's marks
  7. Chart: subject-wise class average
  8. Chart: percentage comparison of all students in a class
  9. Delete a record
  0. Exit
"""

import csv
import os

import pandas as pd
import matplotlib.pyplot as plt

FILE_NAME = "students_records.csv"
SUBJECTS = ["English", "Hindi", "Maths", "Science", "SST"]
MAX_MARKS = 100          # maximum marks per subject
PASS_MARKS = 33          # minimum marks needed in every subject
COLUMNS = ["Name", "Class", "Roll No", "Section"] + SUBJECTS + ["Total", "Percentage", "Grade", "Result"]


# ----------------------------------------------------------------------------
# File helpers
# ----------------------------------------------------------------------------
def init_file():
    """Create the CSV file with a header row if it doesn't exist yet."""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as f:
            csv.writer(f).writerow(COLUMNS)


def load_data():
    """Read the CSV into a pandas DataFrame."""
    init_file()
    df = pd.read_csv(FILE_NAME, dtype={"Class": str, "Section": str})
    return df


def save_data(df):
    df.to_csv(FILE_NAME, index=False)


def append_row(row):
    """Append a single record to the CSV file."""
    with open(FILE_NAME, "a", newline="") as f:
        csv.writer(f).writerow([row[c] for c in COLUMNS])


# ----------------------------------------------------------------------------
# Calculation helpers
# ----------------------------------------------------------------------------
def get_grade(percentage):
    if percentage >= 90:
        return "A+"
    if percentage >= 80:
        return "A"
    if percentage >= 70:
        return "B+"
    if percentage >= 60:
        return "B"
    if percentage >= 50:
        return "C"
    if percentage >= 40:
        return "D"
    return "E"


def calculate(marks):
    """Return total, percentage, grade and result from a list of marks."""
    total = sum(marks)
    percentage = round(total / (MAX_MARKS * len(SUBJECTS)) * 100, 2)
    passed = all(m >= PASS_MARKS for m in marks)
    grade = get_grade(percentage) if passed else "E"
    return total, percentage, grade, "Pass" if passed else "Fail"


# ----------------------------------------------------------------------------
# Input helpers (with validation)
# ----------------------------------------------------------------------------
def ask_text(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("  Input cannot be empty. Try again.")


def ask_int(prompt, low, high):
    while True:
        try:
            value = int(input(prompt).strip())
            if low <= value <= high:
                return value
            print(f"  Enter a number between {low} and {high}.")
        except ValueError:
            print("  Please enter a valid whole number.")


# ----------------------------------------------------------------------------
# Menu functions
# ----------------------------------------------------------------------------
def add_student():
    print("\n--- Add Student Record ---")
    name = ask_text("Student name   : ").title()
    cls = ask_text("Class          : ").upper()
    roll = ask_int("Roll number    : ", 1, 10000)
    section = ask_text("Section        : ").upper()

    df = load_data()
    duplicate = df[(df["Class"] == cls) & (df["Section"] == section) & (df["Roll No"] == roll)]
    if not duplicate.empty:
        print(f"\n  A student with roll no {roll} already exists in Class {cls}-{section}.")
        return

    marks = [ask_int(f"Marks in {s:<8}(0-{MAX_MARKS}): ", 0, MAX_MARKS) for s in SUBJECTS]
    total, percentage, grade, result = calculate(marks)

    row = {"Name": name, "Class": cls, "Roll No": roll, "Section": section}
    row.update(dict(zip(SUBJECTS, marks)))
    row.update({"Total": total, "Percentage": percentage, "Grade": grade, "Result": result})
    append_row(row)

    print(f"\n  Record saved. {name} scored {total}/{MAX_MARKS * len(SUBJECTS)} "
          f"({percentage}%) - Grade {grade} - {result}")


def view_all():
    df = load_data()
    if df.empty:
        print("\n  No records found.")
        return
    print("\n--- All Student Records ---")
    print(df.to_string(index=False))


def find_student():
    """Ask for a roll number (and class/section) or a name; return matching rows."""
    df = load_data()
    if df.empty:
        print("\n  No records found.")
        return None, df

    choice = ask_text("Search by (1) Roll number or (2) Name? : ")
    if choice == "1":
        roll = ask_int("Roll number : ", 1, 10000)
        result = df[df["Roll No"] == roll]
    else:
        name = ask_text("Name (full or part) : ").lower()
        result = df[df["Name"].str.lower().str.contains(name)]

    if result.empty:
        print("\n  No matching student found.")
        return None, df

    if len(result) > 1:
        print("\n  Multiple matches found:")
        print(result[["Name", "Class", "Section", "Roll No", "Percentage"]].to_string())
        idx = ask_int("Enter the index number of the student you want : ", 0, len(df) - 1)
        if idx not in result.index:
            print("  Invalid index.")
            return None, df
        return result.loc[idx], df
    return result.iloc[0], df


def search_student():
    print("\n--- Search Student ---")
    student, _ = find_student()
    if student is not None:
        print()
        print(student.to_string())


def report_card():
    print("\n--- Report Card ---")
    s, _ = find_student()
    if s is None:
        return

    line = "=" * 46
    print(f"\n{line}")
    print(f"{'REPORT CARD':^46}")
    print(line)
    print(f"Name    : {s['Name']}")
    print(f"Class   : {s['Class']}-{s['Section']}        Roll No : {s['Roll No']}")
    print("-" * 46)
    print(f"{'Subject':<15}{'Marks':>10}{'Out of':>10}")
    print("-" * 46)
    for sub in SUBJECTS:
        print(f"{sub:<15}{s[sub]:>10}{MAX_MARKS:>10}")
    print("-" * 46)
    print(f"{'Total':<15}{s['Total']:>10}{MAX_MARKS * len(SUBJECTS):>10}")
    print(f"Percentage : {s['Percentage']}%")
    print(f"Grade      : {s['Grade']}")
    print(f"Result     : {s['Result']}")
    print(line)


def class_statistics():
    df = load_data()
    if df.empty:
        print("\n  No records found.")
        return
    cls = ask_text("\nClass (e.g. 10): ").upper()
    section = input("Section (press Enter for all sections): ").strip().upper()

    data = df[df["Class"] == cls]
    if section:
        data = data[data["Section"] == section]
    if data.empty:
        print("\n  No records for that class/section.")
        return

    topper = data.loc[data["Percentage"].idxmax()]
    print(f"\n--- Statistics: Class {cls} {section} ---")
    print(f"Total students   : {len(data)}")
    print(f"Passed / Failed  : {(data['Result'] == 'Pass').sum()} / {(data['Result'] == 'Fail').sum()}")
    print(f"Class average    : {data['Percentage'].mean():.2f}%")
    print(f"Topper           : {topper['Name']} ({topper['Percentage']}%)")
    print("\nSubject-wise average:")
    print(data[SUBJECTS].mean().round(2).to_string())
    print("\nSubject-wise highest:")
    print(data[SUBJECTS].max().to_string())


# ----------------------------------------------------------------------------
# Charts (matplotlib)
# ----------------------------------------------------------------------------
def chart_student():
    print("\n--- Student Marks Chart ---")
    s, _ = find_student()
    if s is None:
        return
    marks = [s[sub] for sub in SUBJECTS]

    plt.figure(figsize=(8, 5))
    bars = plt.bar(SUBJECTS, marks, color="#4C72B0")
    for bar, m in zip(bars, marks):
        plt.text(bar.get_x() + bar.get_width() / 2, m + 1, str(m), ha="center")
    plt.axhline(PASS_MARKS, color="red", linestyle="--", label=f"Pass marks ({PASS_MARKS})")
    plt.ylim(0, MAX_MARKS + 10)
    plt.ylabel("Marks")
    plt.title(f"{s['Name']} (Class {s['Class']}-{s['Section']}) - {s['Percentage']}%")
    plt.legend()
    plt.tight_layout()
    plt.show()


def chart_subject_average():
    df = load_data()
    if df.empty:
        print("\n  No records found.")
        return
    cls = input("\nClass (press Enter for all classes): ").strip().upper()
    data = df[df["Class"] == cls] if cls else df
    if data.empty:
        print("\n  No records for that class.")
        return

    avg = data[SUBJECTS].mean()
    plt.figure(figsize=(8, 5))
    bars = plt.bar(SUBJECTS, avg, color="#55A868")
    for bar, v in zip(bars, avg):
        plt.text(bar.get_x() + bar.get_width() / 2, v + 1, f"{v:.1f}", ha="center")
    plt.ylim(0, MAX_MARKS + 10)
    plt.ylabel("Average marks")
    plt.title(f"Subject-wise Average - {'Class ' + cls if cls else 'All Classes'}")
    plt.tight_layout()
    plt.show()


def chart_class_comparison():
    df = load_data()
    if df.empty:
        print("\n  No records found.")
        return
    cls = ask_text("\nClass (e.g. 10): ").upper()
    data = df[df["Class"] == cls].sort_values("Percentage", ascending=False)
    if data.empty:
        print("\n  No records for that class.")
        return

    colors = ["#55A868" if r == "Pass" else "#C44E52" for r in data["Result"]]
    plt.figure(figsize=(9, 5))
    plt.bar(data["Name"], data["Percentage"], color=colors)
    plt.xticks(rotation=45, ha="right")
    plt.ylim(0, 105)
    plt.ylabel("Percentage")
    plt.title(f"Class {cls} - Percentage Comparison (green = pass, red = fail)")
    plt.tight_layout()
    plt.show()


# ----------------------------------------------------------------------------
# Delete
# ----------------------------------------------------------------------------
def delete_student():
    print("\n--- Delete Record ---")
    s, df = find_student()
    if s is None:
        return
    confirm = input(f"Delete {s['Name']} (Class {s['Class']}-{s['Section']}, Roll {s['Roll No']})? (y/n): ")
    if confirm.strip().lower() == "y":
        df = df.drop(index=s.name)
        save_data(df)
        print("  Record deleted.")
    else:
        print("  Cancelled.")


# ----------------------------------------------------------------------------
# Main menu
# ----------------------------------------------------------------------------
def main():
    init_file()
    actions = {
        "1": add_student,
        "2": view_all,
        "3": search_student,
        "4": report_card,
        "5": class_statistics,
        "6": chart_student,
        "7": chart_subject_average,
        "8": chart_class_comparison,
        "9": delete_student,
    }
    while True:
        print("\n" + "=" * 40)
        print("   REPORT CARD MANAGEMENT SYSTEM")
        print("=" * 40)
        print("1. Add student record")
        print("2. View all records")
        print("3. Search student")
        print("4. Print report card")
        print("5. Class statistics")
        print("6. Chart: a student's marks")
        print("7. Chart: subject-wise average")
        print("8. Chart: class percentage comparison")
        print("9. Delete a record")
        print("0. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "0":
            print("Goodbye!")
            break
        action = actions.get(choice)
        if action:
            action()
        else:
            print("  Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
