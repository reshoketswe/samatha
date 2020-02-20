from django.shortcuts import render
from urllib import request
from django.http import HttpResponse


def home(request):
	return HttpResponse("<h1> Hello world</h1>")