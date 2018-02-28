import sqlite3
from bottle import *
conn = sqlite3.connect('todo.db')
c = conn.cursor()

@route('/index')
def serveFile():
  return static_file('index.html', root='./static')

@route('/<filename>')
def serveFile(filename):
    return static_file(filename, root='./static')


c.execute('''CREATE TABLE IF NOT EXISTS todo
            (id integer PRIMARY KEY,
            task text, description text, due text)''')
conn.commit()
run(host='localhost', port=8080, reloader=True)

