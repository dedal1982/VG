from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from users.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Имя пользователя")
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    city = forms.CharField(label="Город", max_length=100)

    class Meta:
        model = User
        fields = ("username", "email", "city", "password1", "password2")


class TestForm(forms.Form):
    name = forms.CharField(label="Имя", min_length=8, required=True)
    birthday = forms.DateTimeField(
        label="Время рождения", required=True, widget=forms.DateTimeInput, help_text=""
    )
    avatar = forms.FileField(label="Аватар", required=True)
