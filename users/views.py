import uuid
from django.http.request import HttpRequest
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate

from users.forms import LoginForm, RegisterForm, TestForm


def login_view(request: HttpRequest):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("/")
    else:
        form = LoginForm()
    return render(request, "users/login.html", {"form": form})


def register_view(request):
    # if request.user.is_authenticated:
    #     return redirect("home")
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("/")
    else:
        form = RegisterForm()
    return render(request, "users/register.html", {"form": form})


def test_form_view(request: HttpRequest):
    if request.method == "POST":
        form = TestForm(request.POST, request.FILES)
        f = request.FILES["avatar"]
        with open(f"uploads/{uuid.uuid4().hex}_{f.name}", "wb") as g:
            for chunk in f.chunks(1024):
                g.write(chunk)
    else:
        form = TestForm()
    return render(request, "test/test.html", {"form": form})
