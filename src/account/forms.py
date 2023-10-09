from django import forms
from django.contrib.auth.forms import UserCreationForm

from account.models import StudentAccount

class RegistrationForm(UserCreationForm):
    username            = forms.CharField(max_length=30, help_text='Username is Required',label="Username")
    firstname           = forms.CharField(max_length=60, help_text="", label="First Name")
    lastname            = forms.CharField(max_length=60, help_text="", label="Last Name")
    major               = forms.CharField(max_length=100, help_text="", label="Major")
    year                = forms.DecimalField(max_digits=2, help_text="", label="Year")

    class Meta:
        model = StudentAccount
        fields = ("username","firstname","lastname","password1","password2","major","year")