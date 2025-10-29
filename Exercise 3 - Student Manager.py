import tkinter as tk
from tkinter import messagebox, END

# ---------- Load Data ----------
def load_data():
    with open("huh.txt") as f:
        n = int(f.readline())
        students = []
        for line in f:
            id, name, *m = line.strip().split(",")
            m = list(map(int, m))
            cw, exam = sum(m[:-1]), m[-1]
            total = cw + exam
            percent = round(total / 160 * 100, 2)
            grade = "A" if percent>=70 else "B" if percent>=60 else "C" if percent>=50 else "D" if percent>=40 else "F"
            students.append([id, name, cw, exam, percent, grade, total])
    return students

def format_student(s):
    return f"{s[1]} ({s[0]})\nCW: {s[2]} EX: {s[3]} %: {s[4]} Grade: {s[5]}\n\n"

students = load_data()

# ---------- Functions ----------
def view_all():
    t.delete(1.0, END)
    total_percent = 0
    for idx, s in enumerate(students):
        color = "black" if idx % 2 == 0 else "blue"
        t.insert(END, format_student(s), ("color",))
        t.tag_configure("color", foreground=color)
        total_percent += s[4]
    t.insert(END, f"Students: {len(students)}  Average: {round(total_percent/len(students),2)}%\n", "summary")
    t.tag_configure("summary", foreground="green", font=("Arial", 11, "bold"))

def view_one():
    sel = l.curselection()
    if not sel:
        messagebox.showinfo("Info", "Select a student first!")
        return
    s = students[sel[0]]
    t.delete(1.0, END)
    t.insert(END, format_student(s))

def view_highest():
    s = max(students, key=lambda x: x[6])
    t.delete(1.0, END)
    t.insert(END, "Highest Scorer:\n\n", "header")
    t.tag_configure("header", foreground="darkgreen", font=("Arial", 12, "bold"))
    t.insert(END, format_student(s))

def view_lowest():
    s = min(students, key=lambda x: x[6])
    t.delete(1.0, END)
    t.insert(END, "Lowest Scorer:\n\n", "header")
    t.tag_configure("header", foreground="red", font=("Arial", 12, "bold"))
    t.insert(END, format_student(s))

# ---------- GUI ----------
carnage = tk.Tk()
carnage.title("Student Marks Analyzer")
carnage.geometry("600x450")
carnage.config(bg="#f0f4f7")

tk.Label(carnage, text="Student Marks Analyzer", font=("Arial",16,"bold"), bg="#f0f4f7", fg="#333").pack(pady=10)

l = tk.Listbox(carnage, font=("Arial",11), height=6, selectbackground="#a0c4ff")
for s in students: l.insert(END, s[1])
l.pack(fill="x", padx=20)

bf = tk.Frame(carnage, bg="#f0f4f7")
bf.pack(pady=10)

btn_opts = {"width":12, "font":("Arial",10,"bold"), "bg":"#90e0ef", "fg":"#000", "activebackground":"#00b4d8"}
tk.Button(bf, text="View All", command=view_all, **btn_opts).grid(row=0,column=0,padx=5,pady=3)
tk.Button(bf, text="View One", command=view_one, **btn_opts).grid(row=0,column=1,padx=5,pady=3)
tk.Button(bf, text="Highest", command=view_highest, **btn_opts).grid(row=0,column=2,padx=5,pady=3)
tk.Button(bf, text="Lowest", command=view_lowest, **btn_opts).grid(row=0,column=3,padx=5,pady=3)
tk.Button(bf, text="Quit", command=carnage.destroy, **btn_opts).grid(row=0,column=4,padx=5,pady=3)

t = tk.Text(carnage, wrap="word", font=("Arial",11), bg="#e0f7fa")
t.pack(fill="both", expand=True, padx=20, pady=10)

carnage.mainloop()
