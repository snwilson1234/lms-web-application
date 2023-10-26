from django import forms
from django.contrib.auth import authenticate

from sampleclass.models import AssignmentUploadFile


class AssignmentUploadForm(forms.ModelForm):
    
    file                    = forms.FileField()

    class Meta:
        model = AssignmentUploadFile
        fields = ('file',)