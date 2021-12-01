from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class SetupForm(forms.Form):
    aparts = forms.IntegerField()#widget = forms.TextInput(attrs={'placeholder':'How many apartments do you have'}))

    class Meta:
        model = User
        fields = []

# class LoginForm(forms.Form):
#     username = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)