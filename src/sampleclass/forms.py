from django import forms
from django.contrib.auth import authenticate

from sampleclass.models import AssignmentUploadFile


class AssignmentUploadForm(forms.ModelForm):
    
    file_name               = forms.CharField(max_length=60)
    file                    = forms.FileField()

    class Meta:
        model = AssignmentUploadFile
        fields = ('file_name','file')
    
    def clean(self):
        file_name = self.cleaned_data['file_name']
        #file = self.cleaned_data['file']