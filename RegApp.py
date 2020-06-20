import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar,DateEntry
from tkinter.scrolledtext import *
from tkinter import messagebox

#database
import sqlite3
import csv

conn = sqlite3.connect("data.db")
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS usersdata(firstname TEXT,lastname TEXT,email TEXT,age TEXT,date_of_birth TEXT,address TEXT,phonenumber REAL)")

def add_data(firstname ,lastname ,email ,age ,date_of_birth ,address ,phonenumber ):
    c.execute("INSERT INTO usersdata(firstname ,lastname ,email ,age ,date_of_birth ,address ,phonenumber) VALUES (?,?,?,?,?,?,?)",(firstname ,lastname ,email ,age ,date_of_birth ,address ,phonenumber))
    conn.commit()

def View_all_users():
    c.execute("SELECT * FROM usersdata")
    data = c.fetchall()
    for row in data:
        tree.insert("",tk.END,values=row)

def get_single_user(firstname):
    c.execute('SELECT * FROM usersdata WHERE firstname = "{}"'.format(firstname))
    data = c.fetchall()
    return data

def clear_display_result():
    tab1_display.delete('1.0',END)

def clear_text():
    fname_entry.delete('0',END)
    lname_entry.delete('0',END)
    email_entry.delete('0',END)
    age_entry.delete('0',END)
    address_entry.delete('0',END)
    phone_entry.delete('0',END)


def search_user_by_name():
    firstname = str(entry_search.get())
    result = get_single_user(firstname)
    #c.execute('SELECT * FROM usersdata WHERE firstname = "{}"'.format(firstname))
    #data = c.fetchall()
    #print(result)
    tab2_display.insert(tk.END,result)

def clear_display_view():
    tab2_display.delete('1.0',END)

def clear_entered_search():
    entry_search.delete('0',END)

def add_details():
    firstname = str(fname_entry.get())
    lastname = str(lname_entry.get())
    email = str(email_entry.get())
    age = str(age_entry.get())
    date_of_birth = str(cal_entry.get())
    phonenumber=str(phone_entry.get())
    address = str(address_entry.get())
    add_data(firstname ,lastname ,email ,age ,date_of_birth ,address ,phonenumber )
    result = '\First Name:{},\nLast Name:{},\nEmail:{},\nAge:{},\nDate of Birth:{},\nPhone Number:{}'.format(firstname ,lastname ,email ,age ,date_of_birth ,address ,phonenumber )
    tab1_display.insert(tk.END,result)
    messagebox.showinfo(title="Success!",message="Submitted to database")


def export_to_csv():
    filename = str(filename_entry.get())
    myfilename = filename + '.csv'
    with open(myfilename,'w') as f:
        writer = csv.writer(f)
        c.execute("SELECT *  FROM usersdata")
        data = c.fetchall()
        writer.writerow(['firstname','lastname','email','age','date_of_birth','address','phonenumber'])
        writer.writerows(data)
        messagebox.showinfo(title="Success!!",message='"Exported As {}"'.format(myfilename))

def export_to_xls():
    pass



root = Tk()
root.title("Registration")
root.geometry( "750x450" )

style = ttk.Style(root)
style.configure("lefttab.TNotebook",tabposition='wn')

tab_control = ttk.Notebook(root,style="lefttab.TNotebook")

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
tab5 = ttk.Frame(tab_control)

tab_control.add(tab1,text=f'{"Home":^20s}')
tab_control.add(tab2,text=f'{"View":^20s}')
tab_control.add(tab3,text=f'{"Search":^20s}')
tab_control.add(tab4,text=f'{"Export":^20s}')
tab_control.add(tab5,text=f'{"About":^20s}')

tab_control.pack(expand=1,fill="both")

create_table()

label1 = Label(tab1,text="Registration Form",padx=5,pady=5)
label1.grid(row=0,column=0)
label2 = Label(tab2,text="View",padx=5,pady=5)
label2.grid(row=0,column=0)
label3 = Label(tab3,text="Search",padx=5,pady=5)
label3.grid(row=0,column=0)
label4 = Label(tab4,text="Export",padx=5,pady=5)
label4.grid(row=0,column=0)
label5 = Label(tab5,text="About",padx=5,pady=5)
label5.grid(row=0,column=0)

l1 = Label(tab1,text="First Name",padx=5,pady=5)
l1.grid(row=1,column=0)
fname_raw_entry = StringVar()
fname_entry = Entry(tab1,textvariable=fname_raw_entry,width=50)
fname_entry.grid(row=1,column=1)

l2 = Label(tab1,text="Last Name",padx=5,pady=5)
l2.grid(row=2,column=0)
lname_raw_entry = StringVar()
lname_entry = Entry(tab1,textvariable=lname_raw_entry,width=50)
lname_entry.grid(row=2,column=1)

l3 = Label(tab1,text="Email",padx=5,pady=5)
l3.grid(row=3,column=0)
email_raw_entry = StringVar()
email_entry = Entry(tab1,textvariable=email_raw_entry,width=50)
email_entry.grid(row=3,column=1)

l4 = Label(tab1,text="Age",padx=5,pady=5)
l4.grid(row=4,column=0)
raw_entry = IntVar()
age_entry = Entry(tab1,textvariable=raw_entry,width=50)
age_entry.grid(row=4,column=1)

l5 = Label(tab1,text="Date of Birth",padx=5,pady=5)
l5.grid(row=5,column=0)
dob_raw_entry = StringVar()
cal_entry = DateEntry(tab1,width=50,textvariable=dob_raw_entry,background='dodgerblue',foreground='white',borderwidth=2,year=2000)
cal_entry.grid(row=5,column=1,padx=10,pady=10)

l6 = Label(tab1,text="Address",padx=5,pady=5)
l6.grid(row=6,column=0)
address_raw_entry = StringVar()
address_entry = Entry(tab1,textvariable=address_raw_entry,width=50)
address_entry.grid(row=6,column=1)

l7 = Label(tab1,text="Phone Number",padx=5,pady=5)
l7.grid(row=7,column=0)
phone_raw_entry = StringVar()
phone_entry = Entry(tab1,textvariable=phone_raw_entry,width=50)
phone_entry.grid(row=7,column=1)

button1 = Button(tab1,text="Add",width=12,background="#03A9F4",fg="#fff",command=add_details)
button1.grid(row=8,column=0,padx=5,pady=5)

button2 = Button(tab1,text="Clear",width=12,background="#03A9F4",fg="#fff",command=clear_text)
button2.grid(row=8,column=1,padx=5,pady=5)
#display screen
tab1_display = ScrolledText(tab1,height=5)
tab1_display.grid(row=10,column=1,padx=5,pady=5,columnspan=3)

button3 = Button(tab1,text="Clear Result",width=12,background="#03A9F4",fg="#fff",command=clear_display_result)
button3.grid(row=12,column=1,padx=10,pady=10)

label_search1 = Label(tab3,text="Search Name",padx=5,pady=5)
label_search1.grid(row=1,column=0)
Search_raw_entry = StringVar()
entry_search = Entry(tab3,textvariable=Search_raw_entry,width=30)
entry_search.grid(row=1,column=1)

button_view3 = Button(tab3,text="Clear Search",width=12,background="#03A9F4",fg="#fff",command=clear_entered_search)
button_view3.grid(row=2,column=1,padx=10,pady=10)

button_view4 = Button(tab3,text="Clear Result",width=12,background="#03A9F4",fg="#fff",command=clear_display_view)
button_view4.grid(row=1,column=2,padx=10,pady=10)

button_view5 = Button(tab3,text="Search",width=12,background="#03A9F4",fg="#fff",command=search_user_by_name)
button_view5.grid(row=1,column=2,padx=10,pady=10)

tab2_display = ScrolledText(tab3,height=5)
#tab2_display = Listbox(tab2,height=5,width=60)

tab2_display.grid(row=10,column=0,columnspan=3,padx=5,pady=5)

button_view2 = Button(tab2,text="View All",width=12,bg="#03A9F4",fg="#fff",command=View_all_users)
button_view2.grid(row=1,column=0,padx=10,pady=10)

tree = ttk.Treeview(tab2,column=("column1","column2","column3","column4","column5","column6","column7"),show='headings')
tree.heading("#1",text="First Name")
tree.heading("#2",text="Last Name")
tree.heading("#3",text="Email")
tree.heading("#4",text="Age")
tree.heading("#5",text="DOB")
tree.heading("#6",text="Address")
tree.heading("#7",text="Phone Number")
tree.grid(row=10,column=0,columnspan=3,padx=5,pady=5)


#Export database
label_export1 = Label(tab4,text="File Name",padx=5,pady=5)
label_export1.grid(row=2,column=0)
filename_raw_entry= StringVar()
filename_entry = Entry(tab4,textvariable=filename_raw_entry,width=30)
filename_entry.grid(row=2,column=1)

button_export3 = Button(tab4,text="To CSV",width=12,bg="dodgerblue",fg="#fff",command=export_to_csv)
button_export3.grid(row=3,column=1,padx=10,pady=10)

button_export3 = Button(tab4,text="To XLS",width=12,bg="dodgerblue",fg="#fff",command=export_to_xls)
button_export3.grid(row=3,column=2,padx=10,pady=10)


about_label = Label(tab5,text="Registration GUI version 0.0.0.1\nMasake calebmasake@gmail.com",padx=5,pady=5)
about_label.grid(row=1,column=0)



root.mainloop()