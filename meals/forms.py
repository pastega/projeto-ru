from django import forms

class TestForm(forms.Form):
    ra = forms.IntegerField()
    
    
    