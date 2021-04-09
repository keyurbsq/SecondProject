from django import forms
from django.core import validators
import re
from django.forms import ModelForm
from django.core import validators
from .models import Register  # , Login
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Blogger


class Signupform(forms.ModelForm):
    class Meta:
        model = Register
        fields = "__all__"


# class LoginForm(forms.ModelForm):
#     class Meta:
#         model = Login
#         fields = "__all__"


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        # fields = "__all__"

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blogger
        fields = "__all__"
