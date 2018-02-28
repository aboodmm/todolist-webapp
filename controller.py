from bottle import *

@route('/index')
def serveFile():
  return static_file('index.html', root='./')

@route('/<filename>')
def serveFile(filename):
    return static_file(filename, root='./')

run(host='localhost', port=8080, reloader=True)
