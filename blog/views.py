from django.shortcuts import render

from django.http import HttpResponse

def index(request):
	return HttpResponse(" Hello World! this is from blog/views.py")
