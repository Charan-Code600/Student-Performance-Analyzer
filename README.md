




# 📊 Student Performance Analyzer

A menu-driven command-line application built with **Python** and **Pandas** that helps track, analyze, and visualize student academic performance — from raw marks to class-wide insights, all in one place.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge&logo=plotly&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)

---

## 🚀 Overview

Student Performance Analyzer is a lightweight, terminal-based tool for managing a class of students and instantly generating performance insights — total & average marks, grades, pass/fail status, class statistics, and visual charts — without ever touching a spreadsheet manually.

It's built to be **crash-proof**: every user input is validated, every edge case (missing files, empty data, duplicate names) is handled gracefully, and the underlying data file stays clean no matter how many times you run an analysis.

---

## ✨ Features

| # | Feature | Description |
|---|---------|-------------|
| 1 | 👀 **View All Students** | Instantly view the full student dataset |
| 2 | ➕ **Add New Student** | Add a record with real-time validation and duplicate-name detection |
| 3 | ➗ **Total & Average Marks** | Auto-calculates total and average marks per student |
| 4 | 🏅 **Grade & Pass/Fail Status** | Assigns grades (A+, A, B, C, Fail) based on performance |
| 5 | 📈 **Class Statistics** | Highest, lowest, and class-wide average score |
| 6 | 📚 **Subject-wise Analysis** | Identifies the toughest subject across the class |
| 7 | 🏆 **Top 5 Students** | Ranks and displays the best performers |
| 8 | 📊 **Visualize Data** | Generates a bar chart of average marks — handles duplicate names cleanly |

---

## 🛠️ Tech Stack

- **Python 3** — core logic
- **Pandas** — data storage, manipulation & analysis
- **Matplotlib** — data visualization

---

## 🧠 What Makes This Robust

- ✅ **Auto-recovery** — missing or empty `students.csv` is detected and a fresh file is created automatically
- ✅ **Strict input validation** — marks and attendance are locked to a 0–100 range; invalid entries are rejected and re-prompted, never crash the program
- ✅ **Duplicate protection** — adding a student with an existing name triggers a confirmation prompt
- ✅ **Clean data separation** — only raw student data is ever written to disk; calculated fields (Total, Average, Grade, Status) are generated fresh each time and never pollute the saved file
- ✅ **Safe chart rendering** — duplicate student names are auto-labeled (e.g. `charan (1)`, `charan (2)`) so no data silently disappears from the chart
- ✅ **Full exception handling** — every menu action is wrapped so unexpected errors never crash the session

---

## 💻 Sample Run

```
************************************************
╔══════════════════════════════════════════════╗
║         STUDENT PERFORMANCE ANALYZER         ║
╚══════════════════════════════════════════════╝
************************************************
    View All Students          enter ---> 1
    Add New Student            enter ---> 2
    Total & Average Marks      enter ---> 3
    Grade & Pass/Fail Status   enter ---> 4
    Class Statistics           enter ---> 5
    Subject-wise Analysis      enter ---> 6
    Top 5 Students             enter ---> 7
    Visualize Data (Chart)     enter ---> 8
    Exit                       enter ---> 9
************************************************

Enter your choice: 5
Highest Average: 84.67 (by charan)
Lowest Average: 45.33 (by shubham)
Class Average: 67.33
```

**Chart Output (Option 8):**

A clean bar chart plotting each student's average marks — duplicate names are automatically distinguished so every record is visible.

---

## ⚙️ Getting Started

**1. Install dependencies:**
```bash
pip install pandas matplotlib
```

**2. Run the program:**
```bash
python student_performance_analyzer.py
```

That's it — no setup required. The program creates `students.csv` automatically on first run.

---

## 📁 Project Structure

```
📦 student-performance-analyzer
 ┣ 📜 student_performance_analyzer.py   # Main application
 ┣ 📜 students.csv                      # Auto-generated data file
 ┗ 📜 README.md                         # You are here
```

---

## 🧪 Testing

This project was manually tested end-to-end, covering:
- File auto-creation and empty-file recovery
- Input validation (invalid types, out-of-range values)
- Duplicate-name handling
- Data integrity across repeated calculations
- Chart rendering with duplicate entries
- Invalid menu choices

---

## 👤 Author

**Charan Aade | Python & Data Analysis Developer** 

🔗 [GitHub](https://github.com/Charan-Code600)





