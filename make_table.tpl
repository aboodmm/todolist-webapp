<table>
%for row in rows:
  <tr>
    <td>Id</td>
    <td>Task</td>
    <td>Description</td>
    <td>Date posted</td>
    <td>Date due</td>
    <td>Date updated</td>
    <td>Done?</td>
  </tr>
  %for col in row:
    <td>{{col}} </td>
  %end
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
