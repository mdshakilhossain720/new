from django import forms

class StudentRegestions(forms.Form):
    name=forms.CharField(max_length=50)
    email=forms.EmailField()
    first_name=forms.CharField(max_length=50)