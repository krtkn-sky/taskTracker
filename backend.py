import sqlite3

def connect():
    conn = sqlite3.connect("tasks.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS task (id INTEGER PRIMARY KEY, task TEXT, description TEXT, duedate DATE, priority INTEGER)")
    conn.commit()
    conn.close()

def insert(task, desc, dueDate, priority):
    conn = sqlite3.connect("tasks.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO task (task, description, duedate, priority) VALUES (?, ?, ?, ?)",
                (task, desc, dueDate, priority))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("tasks.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM task")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(task="", desc="", dueDate="", priority=0):
    conn = sqlite3.connect("tasks.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM task WHERE task=? OR description=? OR duedate=? OR priority=?",(task,desc,dueDate,priority))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("tasks.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM task WHERE id=?",(id,))
    conn.commit()
    conn.close()
    
def update(id,task,desc,dueDate,priority):
    conn = sqlite3.connect("tasks.db")
    cur = conn.cursor()
    cur.execute("UPDATE task SET task=?,description=?,dueDate=?,priority=? WHERE id=?",(task,desc,dueDate,priority,id))
    conn.commit()
    conn.close()

"""
def clear_table():
    conn = sqlite3.connect("tasks.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM task")  # Delete all rows from the table
    conn.commit()
    conn.close()
"""

connect()
#insert("Cook","lunch","2023-08-15",3)
#update(1,"Groceries","lunch","2023-08-15",2)
delete(2)
print(view())