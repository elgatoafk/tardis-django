# forms.py
from django import forms

class TimeForm(forms.Form):
    time_zone = forms.ChoiceField(choices=[('America/New York', 'EST time zone | New York'),
                                           ('Europe/London', 'UTC time zone | London'),
                                           ('Europe/Kyiv', 'UA Time'),
                                           ('Asia/Calcutta', 'IN Time')])
    contents = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',
                                                             'placeholder': 'Enter date and time from Admin Order List...',
                                                             'required': True}))