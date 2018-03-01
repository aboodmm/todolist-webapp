import sqlite3
from bottle import *

@route("/index")
def serveFile():
  return static_file("index.html", root="./static")

@route("/todolist")
def todo_list():
  conn = sqlite3.connect("todo.db")
  c = conn.cursor()
  c.execute("SELECT * from todo")
  result = c.fetchall()
  c.close()

  output = template("make_table", rows=result)
  return output

@route("/delete/<item_id>")
def delete_item(item_id):
  conn = sqlite3.connect("todo.db")
  c = conn.cursor()
  c.execute("DELETE from todo WHERE id = ?", (item_id,))
  conn.commit()
  c.close()
  redirect("/todolist")
  

run(host="localhost", port=8080, reloader=True)

