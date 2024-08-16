# STUDENT MARK TRACKER COMPLETE PROJECT CODE
import tkinter as tk
from tkinter import messagebox
import sqlite3
import tkinter.ttk as ttk

# Connect to the database
conn = sqlite3.connect('Student_marks.db')
cursor = conn.cursor()

# Create the table if it doesn't exist
cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS student_marks (
        id INTEGER PRIMARY KEY,
        name TEXT,
        english INTEGER,
        science INTEGER,
        math INTEGER,
        history INTEGER,
        geography INTEGER,
        total INTEGER,
        percentage REAL
    )
''')

def add_student():
    name = name_entry.get()
    english = int(english_entry.get())
    science = int(science_entry.get())
    math = int(math_entry.get())
    history = int(history_entry.get())
    geography = int(geography_entry.get())
    total = english + science + math + history + geography
    percentage = (total / 500) * 100
    cursor.execute('INSERT INTO student_marks (name, english, science, math, history, geography, total, percentage) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', 
                   (name, english, science, math, history, geography, total, percentage))
    conn.commit()
    messagebox.showinfo("Success", "Student added successfully!")
def view_students():
    cursor.execute('SELECT * FROM student_marks')
    students = cursor.fetchall()
    for student in students:
        student_tree.insert("", tk.END, values=student)



def update_marks():
    id = int(id_entry.get())
    english = int(english_entry.get())
    science = int(science_entry.get())
    math = int(math_entry.get())
    history = int(history_entry.get())
    geography = int(geography_entry.get())
    total = english + science + math + history + geography
    percentage = (total / 500) * 100
    cursor.execute('UPDATE student_marks SET english = ?, science = ?, math = ?, history = ?, geography = ?, total = ?, percentage = ? WHERE id = ?', 
                   (english, science, math, history, geography, total, percentage, id))
    conn.commit()
    messagebox.showinfo("Success", "Marks updated successfully!")

def delete_student():
    id = int(id_entry.get())
    cursor.execute('DELETE FROM student_marks WHERE id = ?', (id,))
    conn.commit()
    messagebox.showinfo("Success", "Student deleted successfully!")

root = tk.Tk()
root.title("Student Mark Tracker")
root.geometry("800x600")

name_label = tk.Label(root, text="Name:", font=("Arial", 16))
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

english_label = tk.Label(root, text="English:", font=("Arial", 16))
english_label.pack()
english_entry = tk.Entry(root)
english_entry.pack()

science_label = tk.Label(root, text="Science:", font=("Arial", 16))
science_label.pack()
science_entry = tk.Entry(root)
science_entry.pack()

math_label = tk.Label(root, text="Math:", font=("Arial", 16))
math_label.pack()
math_entry = tk.Entry(root)
math_entry.pack()

history_label = tk.Label(root, text="History:", font=("Arial", 16))
history_label.pack()
history_entry = tk.Entry(root)
history_entry.pack()

geography_label = tk.Label(root, text="Geography:", font=("Arial", 16))
geography_label.pack()
geography_entry = tk.Entry(root)
geography_entry.pack()

id_label = tk.Label(root, text="ID:", font=("Arial", 16))
id_label.pack()
id_entry = tk.Entry(root)
id_entry.pack()

add_button = tk.Button(root, text="Add Student", command=add_student, font=("Arial", 12), width=15)
add_button.pack()

view_button = tk.Button(root, text="View Students", command=view_students, font=("Arial", 12), width=15)
view_button.pack()

update_button = tk.Button(root, text="Update Marks", command=update_marks, font=("Arial", 12), width=15)
update_button.pack()

delete_button = tk.Button(root, text="Delete Student", command=delete_student, font=("Arial", 12), width=15)
delete_button.pack()

#The code looks good, but there's a small issue. You're packing the student_tree widget inside the view_students function, which means it will only be displayed when you click the "View Students" button. If you want the treeview to be displayed all the time, you should pack it outside of the function, like this:


style = ttk.Style()
style.configure("Treeview.Heading", font=("Arial", 12), width=10)

#Here's the updated code with the column widths adjusted:


student_tree = ttk.Treeview(root, style="Treeview")
student_tree["columns"] = ("ID", "Name", "English", "Science", "Math", "History", "Geography", "Total", "Percentage")

student_tree.column("#0", width=0, stretch=False)
student_tree.column("ID", anchor=tk.W, width=30)
student_tree.column("Name", anchor=tk.W, width=50)
student_tree.column("English", anchor=tk.W, width=70)
student_tree.column("Science", anchor=tk.W, width=70)
student_tree.column("Math", anchor=tk.W, width=50)
student_tree.column("History", anchor=tk.W, width=70)
student_tree.column("Geography", anchor=tk.W, width=88)
student_tree.column("Total", anchor=tk.W, width=70)
student_tree.column("Percentage", anchor=tk.W, width=87)

student_tree.heading("ID", text="ID", anchor=tk.W)
student_tree.heading("Name", text="Name", anchor=tk.W)
student_tree.heading("English", text="English", anchor=tk.W)
student_tree.heading("Science", text="Science", anchor=tk.W)
student_tree.heading("Math", text="Math", anchor=tk.W)
student_tree.heading("History", text="History", anchor=tk.W)
student_tree.heading("Geography", text="Geography", anchor=tk.W)
student_tree.heading("Total", text="Total", anchor=tk.W)
student_tree.heading("Percentage", text="Percentage", anchor=tk.W)

student_tree.pack()
root.mainloop()
