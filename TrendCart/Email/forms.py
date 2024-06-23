# forms.py
from django import forms

class EmailForm(forms.Form):
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    recipient = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
