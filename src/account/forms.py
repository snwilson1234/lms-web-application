from django import forms
from django.contrib.auth.forms import UserCreationForm

from account.models import StudentAccount

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Email is required.')

    class Meta:
        model = StudentAccount
        fields = ("email","username","password1","password2","major","year")