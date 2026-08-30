"""Tkinter interface for the Student Information Management System"""

import tkinter as tk
from tkinter import messagebox, ttk

import data


class StudentInformationApp:
    """Collect, save, and display student information."""

    def __init__(self, window):
        self.window = window
        self.window.title("Student Information Management System")
        self.window.geometry("720x620")
        self.window.minsize(620, 560)

        self.student_name = tk.StringVar()
        self.student_course = tk.StringVar()
        self.student_id = tk.StringVar()
        self.subject_name = tk.StringVar()

        self.current_student_subjects = []
        self.build_interface()

    def build_interface(self):
        """Create and arrange all GUI controls."""
        main_frame = ttk.Frame(self.window, padding=24)
        main_frame.pack(fill="both", expand=True)
        main_frame.columnconfigure(0, weight=1)

        ttk.Label(
            main_frame,
            text="Student Information Management System",
            font=("Arial", 18, "bold"),
        ).grid(row=0, column=0, sticky="w", pady=(0, 6))
        ttk.Label(
            main_frame,
            text="Enter the student's details and enrolled subjects.",
        ).grid(row=1, column=0, sticky="w", pady=(0, 18))

        details_frame = ttk.LabelFrame(
            main_frame, text="Student Details", padding=14
        )
        details_frame.grid(row=2, column=0, sticky="ew")
        details_frame.columnconfigure(1, weight=1)

        ttk.Label(details_frame, text="Student Name:").grid(
            row=0, column=0, sticky="w", padx=(0, 12), pady=6
        )
        self.name_entry = ttk.Entry(
            details_frame, textvariable=self.student_name
        )
        self.name_entry.grid(row=0, column=1, sticky="ew", pady=6)

        ttk.Label(details_frame, text="Course:").grid(
            row=1, column=0, sticky="w", padx=(0, 12), pady=6
        )
        ttk.Entry(details_frame, textvariable=self.student_course).grid(
            row=1, column=1, sticky="ew", pady=6
        )

        ttk.Label(details_frame, text="Student ID: ").grid(
            row=2, column=0, sticky="w", padx=(0, 12), pady=6
        )
        self.student_id_display = ttk.Label(details_frame, text="")
        self.student_id_display.grid(
            row=2, column=1, sticky="ew", pady=6
        )

        subjects_frame = ttk.LabelFrame(
            main_frame, text="Enrolled Subjects", padding=14
        )
        subjects_frame.grid(row=3, column=0, sticky="nsew", pady=16)
        subjects_frame.columnconfigure(0, weight=1)
        subjects_frame.rowconfigure(1, weight=1)
        main_frame.rowconfigure(3, weight=1)

        subject_entry = ttk.Entry(
            subjects_frame, textvariable=self.subject_name
        )
        subject_entry.grid(row=0, column=0, sticky="ew", padx=(0, 8))
        subject_entry.bind("<Return>", lambda _event: self.add_subject())
        ttk.Button(
            subjects_frame, text="Add Subject", command=self.add_subject
        ).grid(row=0, column=1, sticky="ew")

        list_frame = ttk.Frame(subjects_frame)
        list_frame.grid(row=1, column=0, columnspan=2, sticky="nsew", pady=10)
        list_frame.columnconfigure(0, weight=1)
        list_frame.rowconfigure(0, weight=1)

        self.subject_list = tk.Listbox(
            list_frame, height=8, selectmode=tk.EXTENDED
        )
        self.subject_list.grid(row=0, column=0, sticky="nsew")
        subject_scrollbar = ttk.Scrollbar(
            list_frame, orient="vertical", command=self.subject_list.yview
        )
        subject_scrollbar.grid(row=0, column=1, sticky="ns")
        self.subject_list.configure(yscrollcommand=subject_scrollbar.set)

        ttk.Button(
            subjects_frame,
            text="Remove Selected Subject",
            command=self.remove_subject,
        ).grid(row=2, column=0, columnspan=2, sticky="ew")

        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=4, column=0, sticky="ew")
        for column in range(3):
            button_frame.columnconfigure(column, weight=1)

        ttk.Button(
            button_frame, text="Load Student", command=self.load_student
        ).grid(row=0, column=0, sticky="ew", padx=(0, 6))
        ttk.Button(
            button_frame, text="Save Student", command=self.save_student
        ).grid(row=0, column=1, sticky="ew", padx=(0, 6))
        ttk.Button(
            button_frame, text="View Students", command=self.view_students
        ).grid(row=0, column=2, sticky="ew", padx=6)
        ttk.Button(
            button_frame, text="Clear Form", command=self.clear_fields
        ).grid(row=0, column=3, sticky="ew", padx=(6, 0))
        self.name_entry.focus_set()

    def add_subject(self):
        """Add a non-empty, non-duplicate subject to the list."""
        subject = self.subject_name.get().strip()
        if not subject:
            messagebox.showwarning(
                "Missing Subject", "Please enter a subject name."
            )
            return

        existing = [
            value.casefold() for value in self.subject_list.get(0, tk.END)
        ]
        if subject.casefold() in existing:
            messagebox.showwarning(
                "Duplicate Subject", "That subject is already in the list."
            )
            return

        self.subject_list.insert(tk.END, subject)
        self.current_student_subjects.append(subject)
        self.subject_name.set("")

    def remove_subject(self):
        """Remove all selected subjects from the list."""
        selected = self.subject_list.curselection()
        if not selected:
            messagebox.showwarning(
                "No Selection", "Please select a subject to remove."
            )
            return
        for index in reversed(selected):
            self.subject_list.delete(index)
            self.current_student_subjects.pop(index)

    def load_student(self):
        name = self.student_name.get().strip()
        course = self.student_course.get().strip()

        loadedStudent = data.getStudentDictionary(name, course)
        if(loadedStudent == {}): 
            messagebox.showerror(title="student_not_found_error", message="Student was not found, please try again.")
            return

        self.student_id = loadedStudent["Student ID"]
        self.student_id_display.config(text=self.student_id)

        self.current_student_subjects = self.current_student_subjects + loadedStudent["Subjects"]
        for subject in loadedStudent["Subjects"]:
            self.subject_list.insert(tk.END, subject)


    def save_student(self):
        """Validate and save one complete student dictionary."""
        name = self.student_name.get().strip()
        course = self.student_course.get().strip()
        subjects = self.current_student_subjects

        print(subjects)

        if not name or not course:
            messagebox.showwarning(
                "Missing Information",
                "Please enter the student's name and course.",
            )
            return
        if not subjects:
            messagebox.showwarning(
                "Missing Subjects", "Please add at least one enrolled subject."
            )
            return

        student = data.createStudentDictionary(name, course, subjects, studentIDParam=self.student_id)
        data.addToFile(student)
        student_id = student["Student ID"]
        messagebox.showinfo(
            "Student Saved",
            "Student added successfully!\n\n"
            f"Name: {student['Name']}\n"
            f"Course: {student['Course']}\n"
            f"Student ID: {student_id[0]}-{student_id[1]}\n"
            f"Subjects: {student['Subjects']}",
        )
        self.student_id = "";
        self.current_student_subjects = []
        self.clear_fields()

    def view_students(self):
        """Open a scrollable window containing every saved record."""
        students = data.getFileContents()
        if not students:
            messagebox.showinfo("Student Records", "No student records found.")
            return

        records_window = tk.Toplevel(self.window)
        records_window.title("Saved Student Records")
        records_window.geometry("850x400")

        frame = ttk.Frame(records_window, padding=14)
        frame.pack(fill="both", expand=True)
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)

        columns = ("student_id", "name", "course", "subjects")
        table = ttk.Treeview(frame, columns=columns, show="headings")
        table.heading("student_id", text="Student ID")
        table.heading("name", text="Name")
        table.heading("course", text="Course")
        table.heading("subjects", text="Subjects")
        table.column("student_id", width=110, anchor="center")
        table.column("name", width=210)
        table.column("course", width=160)
        table.column("subjects", width=330)
        table.grid(row=0, column=0, sticky="nsew")

        scrollbar = ttk.Scrollbar(
            frame, orient="vertical", command=table.yview
        )
        scrollbar.grid(row=0, column=1, sticky="ns")
        table.configure(yscrollcommand=scrollbar.set)

        for student in students:
            student_id = student.get("Student ID", ("", ""))
            id_text = "-".join(str(part) for part in student_id)
            course = student.get("Course", student.get("Program", ""))
            subjects = student.get("Subjects", [])
            table.insert(
                "",
                tk.END,
                values=(
                    id_text,
                    student.get("Name", ""),
                    course,
                    ", ".join(subjects) if subjects else "No subjects recorded",
                ),
            )

        ttk.Button(
            frame, text="Close", command=records_window.destroy
        ).grid(row=1, column=0, columnspan=2, pady=(12, 0))

    def clear_fields(self):
        """Reset every input control."""
        self.student_name.set("")
        self.student_course.set("")
        self.subject_name.set("")
        self.subject_list.delete(0, tk.END)
        self.name_entry.focus_set()


def main():
    """Start the desktop application."""
    window = tk.Tk()
    StudentInformationApp(window)
    window.mainloop()


if __name__ == "__main__":
    main()
