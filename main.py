from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from model import submitDB, intializeDB

root = Tk()
root.geometry("1350x700")
root.title('Student Registration System')

#=========== LABEL ==================
title_label = Label(root, text="Student Registration System", font=("Ariel", 30, "bold"), border=12, relief=GROOVE, bg="lightgrey")
title_label.pack(side=TOP, fill=X)

#=========== Database functions =======
intializeDB()

def get_data():
    try:
        roll = int(rollno_ent.get())
        name = name_ent.get().lower()
        class_var = class_ent.get().lower()
        section = section_ent.get().lower()
        contact = int(contact_ent.get())
        father = father_ent.get().lower()
        address = address_ent.get().lower()
        gender = gender_ent.get().lower()
        date = dob_ent.get().lower()
        
        return roll, name, class_var, section, contact, father, address, gender, date

    except ValueError:
        messagebox.showwarning("Warning", "Invalid input for roll number or contact")
        return None


def insert():
    user_info = get_data()

    if user_info is None:
        return

    try:
        roll, name, class_var, section, contact, father, address, gender, date = user_info

        # Check if any required field is empty
        if not name or not class_var or not section or not father or not address or not gender or not date:
            raise ValueError("Please fill in all fields")

        # validation for contact number
        if not len(contact_ent.get()) == 10:
            raise ValueError("Contact number is not valid")

    except ValueError as e:
        messagebox.showwarning("Warning", str(e))

    else:
        data = (roll, name, class_var, section, contact, father, address, gender, date)
        submitDB(data)

def delete():
    user_info = get_data()

    try:
        roll = user_info[0]

        # Check if any required field is empty
        if not roll:
            raise ValueError("Enter roll number")

        # validation for contact number
        if not contact_ent.get().isdigit() and len(contact_ent.get()) == 10:
            raise ValueError("Contact number is not valid")

    except ValueError as e:
        messagebox.showwarning("Warning", str(e))

    else:
        deleteDB(str(roll))

def update():
    return

def clear():
    return
        
#=========== Frames =================
detail_frame = LabelFrame(root, text="Enter Details", font=("Ariel", 20), bd=12, relief=GROOVE, bg="lightgrey")
detail_frame.place(x=20, y=90, width=420, height=575)

data_frame = Frame(root, bd=12, bg="lightgrey", relief=GROOVE)
data_frame.place(x=460, y=90, width=870, height=575 )

#=========== Entry ==================
rollno_lbl = Label(detail_frame, text="Roll No", font=("Ariel", 15), bg="lightgrey")
rollno_lbl.grid(row=0, column=0, padx=2, pady=2)

rollno_ent = Entry(detail_frame, bd=7, font=("Ariel", 15))
rollno_ent.grid(row=0, column=1, padx=2, pady=2)

name_lbl = Label(detail_frame, text="Name", font=("Ariel", 15), bg="lightgrey")
name_lbl.grid(row=1, column=0, padx=2, pady=2)

name_ent = Entry(detail_frame, bd=7, font=("Ariel", 15))
name_ent.grid(row=1, column=1, padx=2, pady=2)

class_lbl = Label(detail_frame, text="Class", font=("Ariel", 15), bg="lightgrey")
class_lbl.grid(row=2, column=0, padx=2, pady=2)

class_ent = Entry(detail_frame, bd=7, font=("Ariel", 15))
class_ent.grid(row=2, column=1, padx=2, pady=2)

section_lbl = Label(detail_frame, text="Section", font=("Ariel", 15), bg="lightgrey")
section_lbl.grid(row=3, column=0, padx=2, pady=2)

section_ent = Entry(detail_frame, bd=7, font=("Ariel", 15))
section_ent.grid(row=3, column=1, padx=2, pady=2)

contact_lbl = Label(detail_frame, text="Contact", font=("Ariel", 15), bg="lightgrey")
contact_lbl.grid(row=4, column=0, padx=2, pady=2)

contact_ent = Entry(detail_frame, bd=7, font=("Ariel", 15))
contact_ent.grid(row=4, column=1, padx=2, pady=2)

father_lbl = Label(detail_frame, text="Father's Name", font=("Ariel", 15), bg="lightgrey")
father_lbl.grid(row=5, column=0, padx=2, pady=2)

father_ent = Entry(detail_frame, bd=7, font=("Ariel", 15))
father_ent.grid(row=5, column=1, padx=2, pady=2)

address_lbl = Label(detail_frame, text="Address", font=("Ariel", 15), bg="lightgrey")
address_lbl.grid(row=6, column=0, padx=2, pady=2)

address_ent = Entry(detail_frame, bd=7, font=("Ariel", 15))
address_ent.grid(row=6, column=1, padx=2, pady=2)

gender_lbl = Label(detail_frame, text="Gender", font=("Ariel", 15), bg="lightgrey")
gender_lbl.grid(row=7, column=0, padx=2, pady=2)

gender_ent = Entry(detail_frame, bd=7, font=("Ariel", 15))
gender_ent.grid(row=7, column=1, padx=2, pady=2)

dob_lbl = Label(detail_frame, text="date", font=("Ariel", 15), bg="lightgrey")
dob_lbl.grid(row=8, column=0, padx=2, pady=2)

dob_ent = Entry(detail_frame, bd=7, font=("Ariel", 15))
dob_ent.grid(row=8, column=1, padx=2, pady=2)

#===============Buttons=======================

btn_frame = Frame(detail_frame, bg="lightgrey", bd=10, relief=GROOVE)
btn_frame.place(x=20, y=400, width=340, height=100)

submit_btn = Button(btn_frame, text="Submit", font=("Ariel, 12"), command=insert)
submit_btn.grid(row=2, column=0, padx=10, pady=10)

update_btn = Button(btn_frame, text="Update", font=("Ariel, 12"), command=update)
update_btn.grid(row=2, column=1, padx=10, pady=10)

delete_btn = Button(btn_frame, text="Delete", font=("Ariel, 12"), command=delete)
delete_btn.grid(row=2, column=2, padx=10, pady=10)

clear_btn = Button(btn_frame, text="Clear", font=("Ariel, 12"), command=clear)
clear_btn.grid(row=2, column=3, padx=10, pady=10)

#==============Search=========================

search_frame = Frame(data_frame, bg="lightgrey", bd=10, relief=GROOVE)
search_frame.place(x=20, y=20, width=800, height=60)

search_lbl = Label(search_frame, text="Search", font=("Ariel", 15), bg="lightgrey")
search_lbl.grid(row=0, column=0, padx=2, pady=2)

search_by = StringVar()
search_for = ttk.Combobox(search_frame, font=("Ariel", 12), width=65, textvariable=search_by)
search_for.grid(row=0, column=1, columnspan=3, padx=2, pady=2)

search_for['values'] = ("Name",
                        "Roll no",
                        "Contact", 
                        "Class",
                        "Section",
                        "Gender",
                        "Date of Birth") 

search_btn= Button(search_frame, text="Search", font=("Ariel", 12))
search_btn.grid(row=0, column=4, padx=2, pady=2)

#===============Result and tree views=====================

main_frame = Frame(data_frame, bg="lightgrey", bd=10, relief=GROOVE)
main_frame.place(x=20, y=90, width=800, height=450)

y_scroll = Scrollbar(data_frame, orient=VERTICAL)
x_scroll = Scrollbar(data_frame, orient=HORIZONTAL)

student_table = ttk.Treeview(main_frame, columns=("Roll no", "Name", "Class", "Section", "Contact", "Father Name", "gender", "D.O.B", "Address"), yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

y_scroll.config(command=student_table.yview)
x_scroll.config(command=student_table.xview)

y_scroll.pack(side=RIGHT, fill=Y)
x_scroll.pack(side=BOTTOM, fill=X)

student_table.heading("Roll no", text="Roll no")
student_table.heading("Name", text="Name")
student_table.heading("Class", text="Class")
student_table.heading("Section", text="Section")
student_table.heading("Contact", text="Contact")
student_table.heading("Father Name", text="Father's Name")
student_table.heading("gender", text="Gender")
student_table.heading("D.O.B", text="D.O.B")
student_table.heading("Address", text="Address")

student_table['show'] = 'headings'

student_table.column("Roll no", width=100)
student_table.column("Name", width=100)
student_table.column("Class", width=100)
student_table.column("Section", width=100)
student_table.column("Contact", width=100)
student_table.column("Father Name", width=100)
student_table.column("gender", width=100)
student_table.column("D.O.B", width=100)
student_table.column("Address", width=100)

student_table.pack(fill=BOTH, expand=True)

#======================================================
#================= get all values =====================

if __name__ == '__main__':
    root.mainloop()