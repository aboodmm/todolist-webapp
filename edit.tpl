<!DOCTYPE html>
<html>
<body>
<h3>Modify Task id {{item}}</h3>
<form action="/modify/{{item}}" method="POST">
Task <input type="text" name="task"><br>
Description <input type="text" name="descr"><br>
Due date <input type="text" id="due" name="due"><br>
Format - please use this - YYYY-MM-DD<br>
<button type="submit">Edit Task number {{item}}</button>
</form>
</body>
</html>
