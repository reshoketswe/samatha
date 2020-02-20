from django.shortcuts import render
from urllib import request
from django.http import HttpResponse
from django.template import Context


generic = [{'author':'Reshoketswe','content':'Sample Content', 'date':'20-20-2020' , 'title':'sample tile'}]

def home(request):
	context = {'key_1':generic}
	return render(request, 'blog/home.html',context = context)