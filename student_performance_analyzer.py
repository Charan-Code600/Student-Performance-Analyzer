



import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("students.csv")

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

while True:
    print("""
      
===== STUDENT PERFORMANCE ANALYZER =====
      
    View All Students Data                             enter ---> 1
    Add New Student Record                             enter ---> 2
    Calculate Total & Average Marks                    enter ---> 3
    Show Grade & Pass/Fail Status                      enter ---> 4
    Class Statistics (Highest, Lowest, Average)        enter ---> 5
    Subject-wise Analysis (Toughest Subject)           enter ---> 6
    Top 5 Students                                     enter ---> 7
    Visualize Data (Charts)                            enter ---> 8
    Exit                                               enter ---> 9
       
""")
    choice = input("Enter your choice: ")

    if choice == "1":
        print(df)

    elif choice == "2":
        name = input("Enter student name: ")
        math = int(input("Enter Math marks: "))
        science = int(input("Enter Science marks: "))
        english = int(input("Enter English marks: "))
        attendance = int(input("Enter Attendance %: "))
    
        new_student = {
        "Name": name,
        "Math": math,
        "Science": science,
        "English": english,
        "Attendance": attendance
        }
    
        df.loc[len(df)] = new_student
        df.to_csv("students.csv", index=False)
        print(f"{name} added successfully!")

    elif choice == "3":
        df["Total"] = df["Math"] + df["Science"] + df["English"]
        df["Average"] = round(df["Total"] / 3, 2)
        print(df)

    elif choice == "4":
        df["Total"] = df["Math"] + df["Science"] + df["English"]
        df["Average"] = round(df["Total"] / 3, 2)
        df["Grade"] = df["Average"].apply(get_grade)
        df["Status"] = df["Average"].apply(lambda x: "Pass" if x >= 40 else "Fail")
        print(df)

    elif choice == "5":
        df["Total"] = df["Math"] + df["Science"] + df["English"]
        df["Average"] = round(df["Total"] / 3, 2)
    
        highest = df["Average"].max()
        lowest = df["Average"].min()
        class_avg = round(df["Average"].mean(), 2)
    
        top_student = df[df["Average"] == highest]["Name"].values[0]
        low_student = df[df["Average"] == lowest]["Name"].values[0]
    
        print(f"Highest Average: {highest} (by {top_student})")
        print(f"Lowest Average: {lowest} (by {low_student})")
        print(f"Class Average: {class_avg}")

    elif choice == "6":
        math_avg = round(df["Math"].mean(), 2)
        science_avg = round(df["Science"].mean(), 2)
        english_avg = round(df["English"].mean(), 2)
    
        print(f"Math Average: {math_avg}")
        print(f"Science Average: {science_avg}")
        print(f"English Average: {english_avg}")
    
        subject_avgs = {"Math": math_avg, "Science": science_avg, "English": english_avg}
        toughest = min(subject_avgs, key=subject_avgs.get)
    
        print(f"Toughest Subject: {toughest}")

    elif choice == "7":
        df["Total"] = df["Math"] + df["Science"] + df["English"]
        df["Average"] = round(df["Total"] / 3, 2)
    
        top5 = df.sort_values(by="Average", ascending=False).head(5)
        print(top5[["Name", "Average"]])

    elif choice == "8":
        df["Total"] = df["Math"] + df["Science"] + df["English"]
        df["Average"] = round(df["Total"] / 3, 2)
    
        plt.bar(df["Name"], df["Average"], color="skyblue")
        plt.xlabel("Student Name")
        plt.ylabel("Average Marks")
        plt.title("Student Performance - Average Marks")
        plt.show()
        
    elif choice == "9":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please enter a number between 1-9.")
