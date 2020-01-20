function append_tr(data){
	tr = document.createElement("tr");
	tr.classList.add("user-item");

	id = document.createElement("td");
	first_name = document.createElement("td");
	last_name = document.createElement("td");
	email = document.createElement("td");
	gender = document.createElement("td");
	ip = document.createElement("td");
	total_clicks = document.createElement("td");
	total_page_views = document.createElement("td");

	id.innerHTML ="<a href='/users/" + data["id"] +"' >" + data["id"] + "</a>"
	first_name.innerHTML ="<a href='/users/" + data["id"] +"' >" + data["first_name"] + "</a>"
	last_name.innerHTML ="<a href='/users/" + data["id"] +"' >" + data["last_name"] + "</a>"
	email.innerHTML ="<a href='/users/" + data["id"] +"' >" + data["email"] + "</a>"
	g = (data["gender"] == "M") ? "Male" : "Female";
	gender.innerHTML = "<a href='/users/" + data["id"] +"' >" + g + "</a>";
	ip.innerHTML = "<a href='/users/" + data["id"] +"' >"+ data["ip_address"] + "</a>"
	total_clicks.innerHTML ="<a href='/users/" + data["id"] +"' >" + data["total_clicks"] + "</a>"
	total_page_views.innerHTML ="<a href='/users/" + data["id"] +"' >" + data["total_page_views"] + "</a>"

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

function clearTable(){
	trs = document.querySelectorAll(".user-item");
	for(var i = 0;i<trs.length;i++)
	    trs[i].remove();
	loading.style.display ="table-row";
}
const paginate_by = 50;

function add_content(data, start=0,end = 0){
	var i;
	if (end > data.length)
		end = end - data.length;
	while(start < end){
		
		append_tr(data[start]);
		start++;
	}
  	loading.style.display = "none";
}

function disabel_padding(count){
	disableds = document.querySelectorAll(".page-item");
	for(var i = 0;i<disableds.length;i++)
	    disableds[i].classList.remove("disabled");
	disableds[count].classList.add("disabled");
}

loading = document.querySelector(".loading");
list_user = []
$(".page-1").click( function(){
	clearTable();
	add_content(list_user,0,paginate_by);
	disabel_padding(0);
});
$(".page-2").click( function(){
	clearTable();
	add_content(list_user,paginate_by,paginate_by*2);
	disabel_padding(1);
});
$(".page-3").click( function(){
	clearTable();
	add_content(list_user,paginate_by*2,paginate_by*3);
	disabel_padding(2);
});
$(".page-4").click( function(){
	clearTable();
	add_content(list_user,paginate_by*3,paginate_by*4);
	disabel_padding(3);
});
$(".page-5").click( function(){
	clearTable();
	add_content(list_user,paginate_by*4,paginate_by*5);
	disabel_padding(4);
});
$(".page-6").click( function(){
	clearTable();
	add_content(list_user,paginate_by*5,paginate_by*6);
	disabel_padding(5);
});
$(".page-7").click( function(){
	clearTable();
	add_content(list_user,paginate_by*6,paginate_by*7);
	disabel_padding(6);
});
$(".page-8").click( function(){
	clearTable();
	add_content(list_user,paginate_by*7,paginate_by*8);
	disabel_padding(7);
});
$(".page-9").click( function(){
	clearTable();
	add_content(list_user,paginate_by*8,paginate_by*9);
	disabel_padding(8);
});
$(".page-10").click( function(){
	clearTable();
	add_content(list_user,paginate_by*9,paginate_by*10);
	disabel_padding(9);
});
$(".page-11").click( function(){
	clearTable();
	add_content(list_user,paginate_by*10,paginate_by*11);
	disabel_padding(10);
});
$(".page-12").click( function(){
	clearTable();
	add_content(list_user,paginate_by*11,paginate_by*12);
	disabel_padding(11);
});
$(".page-13").click( function(){
	clearTable();
	add_content(list_user,paginate_by*12,paginate_by*13);
	disabel_padding(12);
});
$(".page-14").click( function(){
	clearTable();
	add_content(list_user,paginate_by*13,paginate_by*14);
	disabel_padding(13);
});
$(".page-15").click( function(){
	clearTable();
	add_content(list_user,paginate_by*14,paginate_by*15);
	disabel_padding(14);
});
$(".page-16").click( function(){
	clearTable();
	add_content(list_user,paginate_by*15,paginate_by*16);
	disabel_padding(15);
});
$(".page-17").click( function(){
	clearTable();
	add_content(list_user,paginate_by*16,paginate_by*17);
	disabel_padding(16);
});
$(".page-18").click( function(){
	clearTable();
	add_content(list_user,paginate_by*17,paginate_by*18);
	disabel_padding(17);
});
$(".page-19").click( function(){
	clearTable();
	add_content(list_user,paginate_by*18,paginate_by*19);
	disabel_padding(18);
});
$(".page-20").click( function(){
	clearTable();
	add_content(list_user,paginate_by*19,list_user.length);
	disabel_padding(19);
});

$(document).ready( function() {
	$.ajax({

		url: 'http://localhost:8000/users/',
	    type: 'GET',
	    crossDomain: true,
	    success: function(data) {
			list_user = data;
	    	add_content(data,0,paginate_by);
	    	document.querySelector(".pagination").classList.remove("d-none");
	    },
	    error: function() { alert('Failed!'); },
	});
});