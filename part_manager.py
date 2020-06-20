from tkinter import *
from tkinter import messagebox
from partsdb import Database

db = Database('store.db')

root = Tk()
root.title("Part Manager")
root.geometry( "750x350" )

def populate_list():
    parts_list.delete(0,END)
    for row in db.fetch():
        parts_list.insert(END,row)


def add_item():
    if part_text.get() == '' or customer_text.get() == '' or retailer_text.get() == '' or price_text.get() == '':
        messagebox.showerror("Required Fields","Please include all fields")
        return

    db.insert(part_text.get(),customer_text.get(),retailer_text.get(),price_text.get())
    parts_list.delete(0,END)
    parts_list.insert(END,(part_text.get(),customer_text.get(),retailer_text.get(),price_text.get()))
    clear_text()
    populate_list()


def select_item(event):
    try:
        global selected_item
        index = parts_list.curselection()[0]
        selected_item = parts_list.get(index)
        part_entry.delete(0,END)
        part_entry.insert(END,selected_item[1])
        customer_entry.delete(0,END)
        customer_entry.insert(END,selected_item[2])
        retailer_entry.delete(0,END)
        retailer_entry.insert(END,selected_item[3])
        price_entry.delete(0,END)
        price_entry.insert(END,selected_item[4])
    except IndexError:
        pass




def remove_item():
    db.remove(selected_item[0])
    clear_text()
    populate_list()


def update_item():
    db.update(selected_item[0],part_text.get(),customer_text.get(),retailer_text.get(),price_text.get())
    populate_list()
    

def clear_text():
    part_entry.delete(0,END)
    customer_entry.delete(0,END)
    retailer_entry.delete(0,END)
    price_entry.delete(0,END)


part_text = StringVar()
part_label = Label(root,text="Part Name",font=('bold',14),pady=20)
part_label.grid(row=0,column=0,sticky=W)
part_entry = Entry(root,textvariable=part_text)
part_entry.grid(row=0,column=1)

customer_text = StringVar()
customer_label = Label(root,text="Customer",font=('bold',14))
customer_label.grid(row=0,column=2,sticky=W)
customer_entry = Entry(root,textvariable=customer_text)
customer_entry.grid(row=0,column=3)

retailer_text = StringVar()
retailer_label = Label(root,text="Retailer",font=('bold',14))
retailer_label.grid(row=1,column=0,sticky=W)
retailer_entry = Entry(root,textvariable=retailer_text)
retailer_entry.grid(row=1,column=1)

price_text = StringVar()
price_label = Label(root,text="Price",font=('bold',14))
price_label.grid(row=1,column=2,sticky=W)
price_entry = Entry(root,textvariable=price_text)
price_entry.grid(row=1,column=3)

parts_list = Listbox(root,height=8,width=60,border=0)
parts_list.grid(row=3,column=0,columnspan=3,rowspan=6,pady=20,padx=20)

scrollbar = Scrollbar(root)
scrollbar.grid(row=3,column=3)

parts_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=parts_list.yview)

parts_list.bind('<<ListboxSelect>>',select_item)
 
add_btn = Button(root,text="Add Part",width=12,command=add_item,bg="dodgerblue")
add_btn.grid(row=2,column=0,pady=20)

remove_btn = Button(root,text="Remove Part",width=12,command=remove_item,bg="dodgerblue")
remove_btn.grid(row=2,column=1)

update_btn = Button(root,text="Update Part",width=12,command=update_item,bg="dodgerblue")
update_btn.grid(row=2,column=2)

clear_btn = Button(root,text="Clear Entry",width=12,command=clear_text,bg="dodgerblue")
clear_btn.grid(row=2,column=3)

populate_list()

 
root.mainloop()