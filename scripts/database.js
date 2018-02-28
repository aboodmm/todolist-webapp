function init() {
	var listvar = new Array();
	let today = '02/19/2018'
	listvar[0] = new Array("Brush teeth", "For good breath", today, today);
	listvar[1] = new Array("Take shower", "To eliminate stank", today, today);
	listvar[2] = new Array("Go to school", "To learn something", today, today);
	localtest = localStorage.getItem("abmmoham_storedlist")
	if (localtest === null || localtest === '[]') {
		localStorage.setItem("abmmoham_storedlist", JSON.stringify(listvar));
	}
 }

function addItem() {
	var task = document.getElementById('formtaskname').value
	var comment = document.getElementById('formcomment').value
	var date = document.getElementById('datepicker').value
	listvar = JSON.parse(localStorage.getItem("abmmoham_storedlist"));
	if (Date.parse(date) < Date.parse(new Date())) {
		alert("Bad date");
		return;
	}
	array = [task, comment, date, date]
	listvar.push(array);
	localStorage.setItem("abmmoham_storedlist", JSON.stringify(listvar));
}
