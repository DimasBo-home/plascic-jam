from django.shortcuts import render

def index(request):
	return render(request,"index.html")

def page_user(request,id):
	return render(request,"page_user.html", {"id":id})
