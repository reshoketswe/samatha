from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
import datetime
from .models import Post

class UserRegistration(UserCreationForm):
	email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

	class meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2' )



class PostForm(forms.ModelForm):
    
    
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        ## add a "form-control" class to each form input
        ## for enabling bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
        model = Post
        fields = ("__all__")