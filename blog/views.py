from django.shortcuts import render, redirect
from urllib import request
from django.http import HttpResponse
from django.template import Context
from django.contrib.auth.models import User
from .forms import UserRegistration #so we can add password to registration field 
from  django.contrib import messages


generic = [{'author':'Reshoketswe','content':'Sample Content', 'date':'20-20-2020' , 'title':'sample tile'}]

def home(request):
	context = {'key_1':generic}
	return render(request, 'blog/home.html',context = context)


def register(request):
	if request.method == 'POST':
		f = UserRegistration(request.POST)
		if f.is_valid():
			f.save()
			messages.success(request,'You have been registered succesfully')
			return redirect('register')


	else:
		f = UserRegistration()

	return render(request,'blog/register.html',{'form':f})

