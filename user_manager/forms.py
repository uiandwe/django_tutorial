from django import forms

class LoginForm(forms.Form):
    id = forms.CharField(label="id", max_length=12)
    password = forms.CharField(label="password", max_length=12)
    pass

