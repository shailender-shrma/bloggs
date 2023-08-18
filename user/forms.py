from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserDetail(UserCreationForm):
    email = forms.CharField(max_length=10)
    class Meta:
        model = User

        fields = ("username", 'email', "password1", "password2")