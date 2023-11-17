from django import forms
from django.contrib.auth import authenticate

from home.models import CalendarEvent


class CalendarEventForm(forms.ModelForm):

    title           = forms.CharField(max_length=100, help_text="req", label="Event Title", widget=forms.TextInput(attrs={'placeholder': 'Input Event Title...'}))
    date            = forms.CharField(label="Event Date")
    from_time       = forms.CharField(label="Event Start Time", widget=forms.TextInput(attrs={'placeholder': 'From Time'}))
    to_time         = forms.CharField(label="Event End Time",  widget=forms.TextInput(attrs={'placeholder': 'To Time'}))
    frequency       = forms.ChoiceField(label='Frequency', choices=[
                        ('no-repeat', 'Does not repeat'),
                        ('daily', 'Daily'),
                        ('weekly-today', ''),
                        ('monthly-today', ''),
                        ('annually-today', ''),
                        # ('weekdays', ''),
                        # ('custom', ''),
                    ], widget=forms.Select(attrs={'class': 'form-control'}))
    location        = forms.CharField(max_length=60, help_text="", label="Event Location", widget=forms.TextInput(attrs={'placeholder': 'Input Event Location...'}))

    class Meta:
        model = CalendarEvent
        fields = ("title","date","from_time","to_time","frequency","location")
