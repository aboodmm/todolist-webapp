import sqlite3
from bottle import *

@route('/index')
def serveFile():
  return static_file('index.html', root='./static')

@route('/todolist')
def todo_list():
  conn = sqlite3.connect('todo.db')
  c = conn.cursor()
  c.execute("SELECT * from todo")
  result = c.fetchall()
  c.close()

  output = template('make_table', rows=result)
  return output

run(host='localhost', port=8080, reloader=True)

