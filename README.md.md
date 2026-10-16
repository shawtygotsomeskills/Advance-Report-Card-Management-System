# 🎓 Advance Report Card Management System

A menu-driven **Python** application to manage student records, generate report cards, and visualize class performance with charts. Built with **pandas**, **csv**, and **matplotlib**. 📊

---

## 📌 Table of Contents

- [✨ Features](#-features)
- [🛠️ Tech Stack](#️-tech-stack)
- [📂 Project Structure](#-project-structure)
- [⚙️ Installation](#️-installation)
- [▶️ How to Run](#️-how-to-run)
- [📋 Main Menu](#-main-menu)
- [🧾 Sample Report Card](#-sample-report-card)
- [📊 Charts](#-charts)
- [🗃️ Data Storage](#️-data-storage)
- [🚀 Future Improvements](#-future-improvements)
- [👤 Author](#-author)

---

## ✨ Features

| # | Feature | Description |
|---|---------|-------------|
| 1️⃣ | **Add Student Record** ➕ | Enter a student's details and subject marks, saved to a CSV file |
| 2️⃣ | **View All Records** 📖 | Display every student's record in a clean table |
| 3️⃣ | **Search Student** 🔍 | Find a student by roll number or name |
| 4️⃣ | **Print Report Card** 🧾 | Generate a formatted report card with total, percentage and grade |
| 5️⃣ | **Class Statistics** 📈 | View topper, average, highest/lowest marks and more |
| 6️⃣ | **Chart: Student's Marks** 📊 | Bar chart of one student's marks across subjects |
| 7️⃣ | **Chart: Subject-wise Average** 📚 | Bar chart showing the class average in each subject |
| 8️⃣ | **Chart: Class Percentage Comparison** 🏆 | Compare the percentage of all students side by side |
| 9️⃣ | **Delete a Record** 🗑️ | Remove a student's record from the data file |
| 0️⃣ | **Exit** 🚪 | Safely close the program |

---

## 🛠️ Tech Stack

- 🐍 **Python 3.8+**
- 🐼 **pandas**: data handling, filtering and statistics
- 📄 **csv**: reading and writing student records
- 📉 **matplotlib**: charts and visualizations

---

## 📂 Project Structure

```
📦 report-card-management-system
 ┣ 📜 main.py            # Main program with menu and all functions
 ┣ 📄 students.csv       # Student data (auto-created on first record)
 ┗ 📘 README.md          # Project documentation
```

> 📝 Adjust file names to match your project.

---

## ⚙️ Installation

1. **Clone or download** the project 📥
   ```bash
   git clone https://github.com/your-username/report-card-management-system.git
   cd report-card-management-system
   ```

2. **Install the required libraries** 📦
   ```bash
   pip install pandas matplotlib
   ```
   > `csv` is part of Python's standard library, so no installation is needed. ✅

---

## ▶️ How to Run

```bash
python main.py
```

---

## 📋 Main Menu

```
==========================================
   🎓 ADVANCE REPORT CARD MANAGEMENT 🎓
==========================================
 1. Add student record
 2. View all records
 3. Search student
 4. Print report card
 5. Class statistics
 6. Chart: a student's marks
 7. Chart: subject-wise average
 8. Chart: class percentage comparison
 9. Delete a record
 0. Exit
==========================================
Enter your choice:
```

---

## 🧾 Sample Report Card

```
==========================================
            📄 REPORT CARD
==========================================
 Name       : Aarav Sharma
 Roll No.   : 101
------------------------------------------
 Subject          Marks
 English           85
 Maths             92
 Science           88
 Social Studies    79
 Hindi             90
------------------------------------------
 Total      : 434 / 500
 Percentage : 86.8%
 Grade      : A
==========================================
```

> 🔧 Update the sample to match your own subjects and grading scheme.

---

## 📊 Charts

The program uses **matplotlib** to generate three types of charts:

- 📌 **Student's Marks**: subject-wise marks of a single student
- 📌 **Subject-wise Average**: how the whole class performs in each subject
- 📌 **Class Percentage Comparison**: percentage of every student, making it easy to spot toppers and those who need support

*(Add screenshots here: `![Chart](screenshots/chart1.png)`)* 🖼️

---

## 🗃️ Data Storage

- All records are stored in a **CSV file** 📄
- **csv** handles adding new records, while **pandas** handles viewing, searching, deleting, statistics and chart data
- Data is saved automatically, so it **persists** between runs 💾

---

## 🚀 Future Improvements

- 🔐 Login system for teachers and admins
- 📤 Export report cards as PDF
- 🗄️ Database support (SQLite / MySQL)
- ✏️ Edit/update existing records
- 🖥️ GUI version using Tkinter or a web version with Flask
- 📅 Multi-term and yearly performance tracking

---

## 👤 Author

**Jyotirmay** ✍️

Made with ❤️ and Python 🐍

---

⭐ If you found this project helpful, don't forget to give it a star!
