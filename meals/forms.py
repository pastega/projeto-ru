from django import forms
from django.db import models

class RAForm(forms.Form):
    ra = forms.IntegerField(label='RA: ')
