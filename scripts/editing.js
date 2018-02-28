function createbox() {
    var checkbox = document.createElement('input');
    checkbox.type= 'checkbox';
	checkbox.name= 'wumpus';
    return checkbox;
}
function createbutton(itemnum) {
    var button = document.createElement('button');
	button.innerHTML = "Delete";
	button.addEventListener ("click", function() {
		var ul = document.getElementById("mytodolist");
		while(ul.firstChild) {
 			ul.removeChild(ul.firstChild);
		}
		listvar = JSON.parse(localStorage.getItem("abmmoham_storedlist"));
		listvar.splice(itemnum, 1);
		localStorage.setItem("abmmoham_storedlist", JSON.stringify(listvar));
		populate();
	});
    return button;
}

function populate() {
	listvar = JSON.parse(localStorage.getItem("abmmoham_storedlist"));
	var ul = document.getElementById("mytodolist");
	for (var i = 0; i < listvar.length; i++) {
		var li = document.createElement("li");
		var mission = listvar[i][0];
		var descript = listvar[i][1];
		var due = listvar[i][2];
		var updated = listvar[i][3];
		var finalstring = listvar[i].join();
		//finalstring = mission + descript + posted + updated;
		li.appendChild(createbox())
		li.appendChild(document.createTextNode(finalstring));
		li.appendChild(createbutton(i));
		ul.appendChild(li);
	}
}
