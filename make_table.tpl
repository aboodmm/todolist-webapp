<h1>cmps183: Homework 3</h1>
<h2><a href="/">Home</a> <a href="/todolist">To Do List</a>
<a href="/todoform">To Do Form</a></h2>

<table>
  <tr>
    <td>Id</td>
    <td>Task</td>
    <td>Description</td>
    <td>Date posted</td>
    <td>Date due</td>
    <td>Date updated</td>
    <td>Done?</td>
  </tr>
%for row in rows:
  %for col in row:
    <td>{{col}} </td>
  %end
  <td>
    <button onclick="parent.location.href=
    'http://localhost:8080/update/{{row[0]}}'"
    type="button">Mark done</button>
  </td>
  <td>
    <button onclick="parent.location.href=
    'http://localhost:8080/edit/{{row[0]}}'"
    type="button">Edit</button>
  </td>
  <td>
    <button onclick="parent.location.href=
    'http://localhost:8080/delete/{{row[0]}}'"
    type="button">Delete</button>
  </td>
  </tr>
%end
</table>

<button onclick="parent.location.href=
'http://localhost:8080/todolist'"
type="button">Show all</button>

<button onclick="parent.location.href=
'http://localhost:8080/todolist/done'"
type="button">Show completed</button>

<button onclick="parent.location.href=
'http://localhost:8080/todolist/notdone'"
type="button">Show todo</button>

<button onclick="parent.location.href=
'http://localhost:8080/todolist/due'"
type="button">Sort by due date</button>

<button onclick="parent.location.href=
'http://localhost:8080/todolist/posted'"
type="button">Sort by posted date</button>

<button onclick="parent.location.href=
'http://localhost:8080/todolist/updated'"
type="button">Sort by updated date</button>

