from tkinter import *
from tkcalendar import Calendar
import backend

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0, END)
    task_text = taskText.get()
    desc_text = descText.get()
    due_date = e3.get()
    priority_int = priorityInt.get()
    for row in backend.search(task_text, desc_text, due_date, priority_int):
        list1.insert(END, row)

def add_command():
    backend.insert(taskText.get(),descText.get(),e3.get(),priorityInt.get())
    list1.delete(0,END)
    list1.insert(END,(taskText.get(),descText.get(),e3.get(),priorityInt.get()))

def delete_command():
    selected_item = list1.curselection()
    if selected_item:
        index = selected_item[0]
        task_id = list1.get(index)[0]  
        backend.delete(task_id)
        view_command()  

def update_command():
    selected_item = list1.curselection()
    if selected_item:
        index = selected_item[0]
        task_id = list1.get(index)[0]  
        backend.update(task_id, taskText.get(), descText.get(), e3.get(), priorityInt.get())
        view_command()  
        
def get_selected_date():
    selected_date = cal.get_date()
    e3.delete(0, "end")
    e3.insert(0, selected_date)

window = Tk()
window.title("Task Tracker")

l1 = Label(window, text="Task")
l1.grid(row=0, column=0)

l2 = Label(window, text="Description")
l2.grid(row=0, column=2)

l3 = Label(window, text="Due date")
l3.grid(row=1, column=0)

l4 = Label(window, text="Priority")
l4.grid(row=1, column=2)


taskText = StringVar()
e1 = Entry(window, textvariable=taskText)
e1.grid(row=0, column=1)

descText = StringVar()
e2 = Entry(window, textvariable=descText)
e2.grid(row=0, column=3)

priorityInt = IntVar()
e4 = Entry(window, textvariable=priorityInt)
e4.grid(row=1, column=3)

e3 = Entry(window)
e3.grid(row=1, column=1)


cal = Calendar(window, selectmode="day")
cal.grid(row=2, column=0, pady=10, columnspan=3)

button = Button(window, text="Get Date", command=get_selected_date)
button.grid(row=3, column=0, columnspan=3)


list1 = Listbox(window,height=6,width=35)
list1.grid(row=4,column=0,rowspan=6,columnspan=2,padx=10,pady=10)

sb1 = Scrollbar(window)
sb1.grid(row=4,column=2,rowspan=6,sticky="ns",pady=10)


list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)


b1 = Button(window,text="Add task",width=12,command=add_command)
b1.grid(row=5,column=3)

b2 = Button(window, text="Update task", width=12, command=update_command)
b2.grid(row=6, column=3)

b3 = Button(window, text="Delete task", width=12, command=delete_command)
b3.grid(row=7, column=3)

b4 = Button(window, text="Search task", width=12, command=search_command)
b4.grid(row=8, column=3)

b5 = Button(window, text="View tasks", width=12, command=view_command)
b5.grid(row=9, column=3)

#print(window.grid_size())

window.mainloop()
