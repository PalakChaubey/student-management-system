import csv
import os
from tabulate import tabulate
import tkinter as tk
from tkinter import messagebox, simpledialog

FILE_NAME = "students.csv"

# Create file if not exists
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Roll", "Name", "Marks"])

# ---------------------- CSV OPERATIONS ----------------------

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")

    with open(FILE_NAME, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([roll, name, marks])

    print("✅ Student record added successfully!")


def view_students():
    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        data = list(reader)

        if len(data) <= 1:
            print("⚠️ No records found.")
        else:
            print(tabulate(data[1:], headers=data[0], tablefmt="grid"))


def delete_student():
    roll = input("Enter Roll Number to delete: ")
    updated = []
    found = False

    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] != roll:
                updated.append(row)
            else:
                found = True

    with open(FILE_NAME, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(updated)

    if found:
        print("🗑️ Record deleted successfully!")
    else:
        print("⚠️ No record found with that Roll Number.")


def update_student():
    roll = input("Enter Roll Number to update: ")
    updated = []
    found = False

    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == roll:
                new_marks = input(f"Enter new marks for {row[1]}: ")
                updated.append([row[0], row[1], new_marks])
                found = True
            else:
                updated.append(row)

    with open(FILE_NAME, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(updated)

    if found:
        print("✏️ Record updated successfully!")
    else:
        print("⚠️ No record found with that Roll Number.")


def search_student():
    roll = input("Enter Roll Number to search: ")

    with open(FILE_NAME, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["Roll"] == roll:
                print("\n🎯 Student Found:")
                print(tabulate([row.values()], row.keys(), tablefmt="grid"))
                return

    print("❌ No student found with this Roll Number.")


# ---------------------- GUI VERSION ----------------------

def gui_add():
    roll = simpledialog.askstring("Input", "Enter Roll Number:")
    name = simpledialog.askstring("Input", "Enter Name:")
    marks = simpledialog.askstring("Input", "Enter Marks:")

    if roll and name and marks:
        with open(FILE_NAME, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([roll, name, marks])
        messagebox.showinfo("Success", "Student added!")
    else:
        messagebox.showwarning("Error", "All fields required!")


def gui_search():
    roll = simpledialog.askstring("Search", "Enter Roll Number:")
    if not roll:
        return

    with open(FILE_NAME, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["Roll"] == roll:
                messagebox.showinfo(
                    "Student Found",
                    f"Roll: {row['Roll']}\nName: {row['Name']}\nMarks: {row['Marks']}"
                )
                return

    messagebox.showerror("Not Found", "No student with this roll number.")


def open_gui():
    win = tk.Tk()
    win.title("Student Management System")
    win.geometry("350x300")

    tk.Button(win, text="Add Student", width=20, command=gui_add).pack(pady=10)
    tk.Button(win, text="Search Student", width=20, command=gui_search).pack(pady=10)
    tk.Button(win, text="Exit", width=20, command=win.destroy).pack(pady=10)

    win.mainloop()


# ---------------------- TERMINAL MENU ----------------------

def main():
    while True:
        print("\n===== Student Record Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Open GUI")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            open_gui()
        elif choice == '7':
            print("👋 Exiting program. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Try again.")


if __name__ == "__main__":
    main()
