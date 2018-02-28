function showtodo() {
	var mumbo = document.getElementById("mytodolist").childNodes;
	for (var i =1; i < mumbo.length; i++) {
		if (mumbo[i].firstChild.checked === false) {
			mumbo[i].hidden = false;
		}
		else {
			mumbo[i].hidden = true;
		}
	}
}

function showcompleted() {
	var mumbo = document.getElementById("mytodolist").childNodes;
	for (var i =1; i < mumbo.length; i++) {
		if (mumbo[i].firstChild.checked === false) {
			mumbo[i].hidden = true;
		}
		else {
			mumbo[i].hidden = false;
		}
	}
}

function showall() {
	var mumbo = document.getElementById("mytodolist").childNodes;
	for (var i =1; i < mumbo.length; i++) {
		if (mumbo[i].hidden === true) {
			mumbo[i].hidden = false;
		}
	}
}

function sortdue() {
	var ul = document.getElementById("mytodolist");
	var mumbo = document.getElementById("mytodolist").childNodes;
	var templist = [];
	var newul = ul.cloneNode(false);
	for (var i = 0; i < mumbo.length; i++) {
		if (mumbo[i].nodeName === 'LI') {
			templist.push(mumbo[i]);
			//var inner = mumbo[i].innerText.split(',');
			//console.log(inner);
			//templist.push(inner[2]);
		}
	}
	templist.sort(function(a, b) {
		return new Date(b.innerText.split(',')[2]) - new Date(a.innerText.split(',')[2])
	});
	for (var i = 0; i < templist.length; i++) {
		newul.appendChild(templist[i]);
	}
	ul.parentNode.replaceChild(newul, ul);
}
