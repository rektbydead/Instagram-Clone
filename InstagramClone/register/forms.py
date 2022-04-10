from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(blank=False, null=False)
    name = forms.CharField(max_length=16, blank=False, null=False)

    class Meta:
        model = User
        fields = ["email", "name", "username", "password1", "password2"]


