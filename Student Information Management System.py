import tkinter as tk
from tkinter import messagebox


window = tk.Tk()
window.title("Student Information Management System")
window.geometry("500x500")


student_name = tk.StringVar()
student_program = tk.StringVar()


def add_student():

    name = student_name.get()
    program = student_program.get()

    if name == "" or program == "":
        messagebox.showwarning(
            "Missing Information",
            "Please enter student name and program."
        )
        return

    studentDict = data.getStudentDictionary(
        name,
        program
    )

    data.addToFile(studentDict)

    messagebox.showinfo(
        "Success",
        "Student Added Successfully!\n\n"
        f"Name: {studentDict['Name']}\n"
        f"Program: {studentDict['Program']}\n"
        f"Student ID: {studentDict['Student ID'][0]}-{studentDict['Student ID'][1]}"
    )

    clear_fields()


def view_students():

    students = data.getFileContents()

    if len(students) == 0:
        messagebox.showinfo(
            "Students",
            "No student records found."
        )
        return

    records = ""

    for student in students:
        records += (
            f"Name: {student['Name']}\n"
            f"Program: {student['Program']}\n"
            f"Student ID: {student['Student ID'][0]}-{student['Student ID'][1]}\n"
            "--------------------------\n"
        )

    messagebox.showinfo(
        "Student Records",
        records
    )


def clear_fields():
    student_name.set("")
    student_program.set("")


title = tk.Label(
    window,
    text="Student Information\nManagement System",
    font=("Arial", 16, "bold")
)

title.pack(pady=20)


tk.Label(
    window,
    text="Student Name"
).pack()

tk.Entry(
    window,
    textvariable=student_name,
    width=40
).pack(pady=5)


tk.Label(
    window,
    text="Program"
).pack()

tk.Entry(
    window,
    textvariable=student_program,
    width=40
).pack(pady=5)


tk.Button(
    window,
    text="Add Student",
    command=add_student,
    width=25
).pack(pady=10)


tk.Button(
    window,
    text="View Students",
    command=view_students,
    width=25
).pack(pady=10)


tk.Button(
    window,
    text="Clear",
    command=clear_fields,
    width=25
).pack(pady=10)


window.mainloop()