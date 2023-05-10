from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django import forms

class EditUserProfileForm(UserChangeForm):
    password = None
    class Meta(object):
        model = User
        # fields = ['username', 'first_name', 'last_name', 'email', 'date_joined', 'last_login', 'is_active']
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'email' : 'Email'}
        error_messages = {
            'first_name' : {'required' : 'Enter Your First Name'},
            'last_name' : {'required' : 'Enter Your Last Name'},
            'email' : {'required' : 'Enter Your Email'},
        }
        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your Username'}),
            'first_name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your FirstName'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your LastName'}),
            'email' : forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter your Valid Email'}),
        }