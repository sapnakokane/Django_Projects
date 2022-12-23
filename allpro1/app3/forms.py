from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        widgets={
            'password':forms.PasswordInput()
        }
        fields=['username','password','email','first_name','last_name']