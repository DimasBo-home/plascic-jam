alert("main.js");
function append_tr(data){
	tr = document.createElement("tr");

	id = document.createElement("td");
	first_name = document.createElement("td");
	last_name = document.createElement("td");
	email = document.createElement("td");
	gender = document.createElement("td");
	ip = document.createElement("td");
	total_clicks = document.createElement("td");
	total_page_views = document.createElement("td");

	id.innerHTML = data["id"]
	first_name.innerHTML = data["first_name"]
	last_name.innerHTML = data["last_name"]
	email.innerHTML = data["email"]
	gender.innerHTML = data["gender"]
	ip.innerHTML = data["ip"]
	total_clicks.innerHTML = data["total_clicks"]
	total_page_views.innerHTML = data["total_page_views"]

	tr.appendChild(id);
	tr.appendChild(first_name);
	tr.appendChild(last_name);
	tr.appendChild(email);
	tr.appendChild(gender);
	tr.appendChild(ip);
	tr.appendChild(total_clicks);
	tr.appendChild(total_page_views);

	document.querySelector("tbody").appendChild(tr);
}

append_tr({"id":1,"last_name":"test","first_name":"name"});
const paginate_by = 50;

$(document).ready( function() {
	$.ajax("http://127.0.0.1:8000/users/",
		success: function(data){
			console.log(data);
		}
		);
});