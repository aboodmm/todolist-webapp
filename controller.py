import sqlite3
from bottle import *

dueasc = True
postedasc = True
updatedasc = True

@route("/static/styles.css")
def serveIndex():
  return static_file("styles.css", root="./static")

@route("/")
def todo_list():
  conn = sqlite3.connect("todo.db")
  c = conn.cursor()
  c.execute("SELECT * FROM todo")
  result = c.fetchall()
  c.close()

  output = template("make_table", rows=result)
  return output

@route("/todolist/<filters>")
def todo_list(filters):
  conn = sqlite3.connect("todo.db")
  c = conn.cursor()
  global dueasc, postedasc, updatedasc
  if filters == "due":
    if dueasc:
      c.execute("SELECT * FROM todo ORDER BY due ASC")
      dueasc = False
    else:
      c.execute("SELECT * FROM todo ORDER BY due DESC")
      dueasc = True
  if filters == "posted":
    if postedasc:
      c.execute("SELECT * FROM todo ORDER BY posted ASC")
      postedasc = False
    else:
      c.execute("SELECT * FROM todo ORDER BY posted DESC")
      postedasc = True
  if filters == "updated":
    if updatedasc:
      c.execute("SELECT * FROM todo ORDER BY updated ASC")
      updatedasc = False
    else:
      c.execute("SELECT * FROM todo ORDER BY updated DESC")
      updatedasc = True
  if filters == "done":
    c.execute("SELECT * FROM todo WHERE status = 1")
  if filters == "notdone":
    c.execute("SELECT * FROM todo WHERE status = 0")
  result = c.fetchall()
  c.close()
  
  output = template("make_table", rows=result)
  return output

@route("/delete/<item_id>")
def delete_item(item_id):
  conn = sqlite3.connect("todo.db")
  c = conn.cursor()
  c.execute("DELETE from todo WHERE id = ?", (item_id))
  conn.commit()
  c.close()
  redirect("/")

@route("/update/<item_id>")
def update_item(item_id):
  conn = sqlite3.connect("todo.db")
  c = conn.cursor()
  c.execute("UPDATE todo set status = 1 WHERE id = ?", (item_id))
  conn.commit()
  c.close()
  redirect("/")

@route("/edit/<item_id>")
def update_item(item_id):
  redirect("/modify" + "/" + item_id)

@route("/modify/<item_id>", method=["GET", "POST"])
def modify_item(item_id):
  if request.POST:
    task = request.POST.get('task')
    descr = request.POST.get('descr')
    due = request.POST.get('due')
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()  
    c.execute("UPDATE todo SET title=?, description=?, due=?, \
              updated=date('now') \
              WHERE id LIKE ?", (task, descr, due, item_id))
    conn.commit()
    redirect("/")
  else:
    output = template("edit", item = item_id)
    return output
    
@route('/new', method=['POST'])
def new_item():
  task = request.POST.get('task')
  descr = request.POST.get('descr')
  due = request.POST.get('due')
  conn = sqlite3.connect('todo.db')
  c = conn.cursor()  
  c.execute("INSERT into todo VALUES (NULL, ?, ?, date('now'), \
             ?, date('now'), 0)", (task, descr, due))
  conn.commit()
             
  return redirect('/')

run(host="localhost", port=8080, reloader=True)

