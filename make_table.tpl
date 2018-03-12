<head>
  <link rel="stylesheet" type="text/css" href="/static/styles.css">
</head>
<div class="myheader">
<h1>cmps183: Homework 4</h1>
</div>
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

<h3>Create new task</h3>
<form action="/new" method="POST">
Task <input type="text" name="task"><br>
Description <input type="text" name="descr"><br>
Due date <input type="text" id="due" name="due"><br>
Format - please use this - YYYY-MM-DD<br>
<button type="submit">Add Task</button>
</form>

<div class="footer">
  <h2>This is my beautiful footer. Admire the brilliant green
      color.</h2>
</div>
