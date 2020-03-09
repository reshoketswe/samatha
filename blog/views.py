from django.shortcuts import render, redirect
from urllib import request
from django.http import HttpResponse
from django.template import Context
from django.contrib.auth.models import User
from .forms import UserRegistration #so we can add password to registration field 
from  django.contrib import messages
from .models import Post
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


# generic = [{'author':'Reshoketswe','content':'Sample Content', 'date':'20-20-2020' , 'title':'sample tile'}]

generic = Post.objects.all()


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



class PostCreateView(LoginRequiredMixin,CreateView): #user can only access pages using this if they are logged in
	model = Post

	fields = ['title','content','image']


	def form_valid(self,form):
		form.instance.author = self.request.user #set the author to the current logged in user
		return super().form_valid(form)

