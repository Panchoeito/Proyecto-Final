from django import forms

class PosteoForm(forms.Form):
    title = forms.CharField(max_length=50)
    subtitle = forms.CharField(max_length=100)
    body = forms.CharField(max_length=4000)
    author = forms.CharField(max_length=50)
    date = forms.DateTimeField()
    image = forms.ImageField()