




import pandas as pd
import matplotlib.pyplot as plt

FILENAME = "students.csv"
RAW_COLUMNS = ["Name", "Math", "Science", "English", "Attendance"]

print("""

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

*************************************************
""")

def main():
    df = load_data()

    while True:

        print("")
        print("*" *50)
        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                view_all_students(df)
            elif choice == "2":
                df = add_student(df)
            elif choice == "3":
                show_totals(df)
            elif choice == "4":
                show_grades(df)
            elif choice == "5":
                class_statistics(df)
            elif choice == "6":
                subject_analysis(df)
            elif choice == "7":
                top_5_students(df)
            elif choice == "8":
                visualize_data(df)
            elif choice == "9":
                print("Exiting program...")
                break
            else:
                print("Invalid choice! Please enter a number between 1-9.")
        except Exception as e:
            print(f"\nSomething went wrong: {e}")
            print("Please try again.")


def load_data():
    try:
        return pd.read_csv(FILENAME)
    except (FileNotFoundError, pd.errors.EmptyDataError):
        print(f"\n'{FILENAME}' not found or empty. Creating a new file...")
        data = pd.DataFrame(columns=RAW_COLUMNS)
        data.to_csv(FILENAME, index=False)
        return data


def save_data(df):
    """Save only the raw columns — calculated columns (Total/Average/Grade/Status)
    must never be written to the CSV, or reloading the file will corrupt future calculations."""
    df[RAW_COLUMNS].to_csv(FILENAME, index=False)


def get_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 75:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 40:
        return "C"
    else:
        return "Fail"


def calculate_totals(data):
    """Returns a NEW dataframe with Total/Average added — never mutates the original df,
    so the caller's data stays clean for future operations."""
    data = data.copy()
    data["Total"] = data["Math"] + data["Science"] + data["English"]
    data["Average"] = round(data["Total"] / 3, 2)
    return data


def get_valid_marks(subject):
    while True:
        try:
            marks = int(input(f"Enter {subject} marks (0-100): "))
            if 0 <= marks <= 100:
                return marks
            print("Marks must be between 0 and 100. Try again.")
            print()
        except ValueError:
            print("Invalid input! Enter a whole number.")


def get_valid_attendance():
    while True:
        try:
            attendance = int(input("Enter Attendance % (0-100): "))
            if 0 <= attendance <= 100:
                return attendance
            print("Attendance must be between 0 and 100. Try again.")
            print()
        except ValueError:
            print("Invalid input! Enter a whole number.")


def view_all_students(df):
    if df.empty:
        print("\nNo student records found yet. Add one first (Option 2).")
        return
    print(f"\nAvailable columns: {list(df.columns)}\n")
    print(df)


def add_student(df):
    name = input("Enter student name: ").strip()
    if name == "":
        print("Name cannot be empty!")
        print("-------------------------------------")
        return df

    if not df.empty and name.lower() in df["Name"].str.lower().values:
        confirm = input(f"'{name}' already exists. Add anyway? (y/n): ").strip().lower()
        if confirm != "y":
            print("Add cancelled.")
            return df
    print("")
    math = get_valid_marks("Math")
    print()
    science = get_valid_marks("Science")
    print()
    english = get_valid_marks("English")
    print()
    attendance = get_valid_attendance()

    df.loc[len(df)] = {"Name": name, "Math": math, "Science": science,
                        "English": english, "Attendance": attendance}
    save_data(df)
    print(f"\n{name} added successfully!")
    return df


def show_totals(df):
    if df.empty:
        print("\nNo student records found yet.")
        return
    temp = calculate_totals(df)
    print(f"\nAvailable columns: {list(temp.columns)}\n")
    print(temp)


def show_grades(df):
    if df.empty:
        print("\nNo student records found yet.")
        return
    temp = calculate_totals(df)
    temp["Grade"] = temp["Average"].apply(get_grade)
    temp["Status"] = temp["Average"].apply(lambda x: "Pass" if x >= 40 else "Fail")
    print(f"\nAvailable columns: {list(temp.columns)}\n")
    print(temp)


def class_statistics(df):
    if df.empty:
        print("\nNo student records found yet.")
        return
    temp = calculate_totals(df)
    highest, lowest = temp["Average"].max(), temp["Average"].min()
    class_avg = round(temp["Average"].mean(), 2)
    top_student = temp[temp["Average"] == highest]["Name"].values[0]
    low_student = temp[temp["Average"] == lowest]["Name"].values[0]

    print(f"\nHighest Average: {highest} (by {top_student})")
    print(f"Lowest Average: {lowest} (by {low_student})")
    print(f"Class Average: {class_avg}")


def subject_analysis(df):
    if df.empty:
        print("\nNo student records found yet.")
        return
    math_avg = round(df["Math"].mean(), 2)
    science_avg = round(df["Science"].mean(), 2)
    english_avg = round(df["English"].mean(), 2)

    print(f"\nMath Average: {math_avg}")
    print(f"Science Average: {science_avg}")
    print(f"English Average: {english_avg}")

    subject_avgs = {"Math": math_avg, "Science": science_avg, "English": english_avg}
    toughest = min(subject_avgs, key=subject_avgs.get)
    print(f"Toughest Subject: {toughest}")


def top_5_students(df):
    if df.empty:
        print("\nNo student records found yet.")
        return
    temp = calculate_totals(df)
    top5 = temp.sort_values(by="Average", ascending=False).head(5)
    print(f"\nTop {min(5, len(temp))} Students:\n")
    print(top5[["Name", "Average"]])


def visualize_data(df):
    if df.empty:
        print("\nNo student records found yet. Nothing to visualize.")
        return
    temp = calculate_totals(df)

    name_list = temp["Name"].tolist()
    labels = [
        f"{name} ({i})" if name_list.count(name) > 1 else name
        for i, name in enumerate(name_list)
    ]

    plt.bar(labels, temp["Average"], color="skyblue")
    plt.xlabel("Student Name")
    plt.ylabel("Average Marks")
    plt.title("Student Performance - Average Marks")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()








