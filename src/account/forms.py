from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from account.models import StudentAccount

class RegistrationForm(UserCreationForm):
    username            = forms.CharField(max_length=30, help_text='Username is Required',label="Username")
    firstname           = forms.CharField(max_length=60, help_text="", label="First Name")
    lastname            = forms.CharField(max_length=60, help_text="", label="Last Name")
    major               = forms.CharField(max_length=100, help_text="", label="Major")
    year                = forms.DecimalField(max_digits=2, help_text="", label="Year")
    password1           = forms.CharField(max_length=60, help_text="", label="Password", widget=forms.PasswordInput)
    password2           = forms.CharField(max_length=60, help_text="", label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = StudentAccount
        fields = ("username","firstname","lastname","password1","password2","major","year")


class LoginForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = StudentAccount
        fields = ('username','password')
    
    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if not authenticate(username=username, password=password):
            raise forms.ValidationError("Invalid login")