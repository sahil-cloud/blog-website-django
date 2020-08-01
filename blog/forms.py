from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User,models
from .models import Post

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control formbg','placeholder':'password'}))
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control formbg','placeholder':'confirm password'}))
    class Meta:
        model = User
        fields = ['username','email']
        labels = {'username':'UserName' , 'email':'Email'}
        widgets = {'username':forms.TextInput(attrs={'class':'form-control formbg','placeholder':'Username'}),
        
                   'email': forms.TextInput(attrs={'class': 'form-control formbg','placeholder':'Email'}),
        
        }


class LoginUser(AuthenticationForm):
    username = UsernameField(widget=forms.TimeInput(
        attrs={'class': 'form-control formbg', 'autofocus': True, 'placeholder': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control formbg",'placeholder':'Password'
                                                                 , 'autocomplete': 'current-password'}),label='Password', strip=False)

class AddPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','desc']
        labels = {'title':'Title' , 'desc':'Description'}
        widgets = {'title':forms.TextInput(attrs={'class':'form-control formbg'}),
            'desc':forms.Textarea(attrs={'class':'form-control formbg'})
        }


class UpdatePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author','title', 'desc']
        labels = {'author':'Author','title': 'Title', 'desc': 'Description'}
        widgets = {'title': forms.TextInput(attrs={'class': 'form-control'}),
                   'desc': forms.Textarea(attrs={'class': 'form-control'}),
                   'author':forms.TextInput(attrs={'class':'form-control'})
                   }
