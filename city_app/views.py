from django.http.request import HttpRequest
from django.shortcuts import render


def catalog_view(request: HttpRequest):
    return render(request, "city_app/home.html")


def choose_city_view(request: HttpRequest):
    return render(request, "city_app/index.html")


def get_portfolio(request: HttpRequest):
    return render(request, "portfolio/portfolio.html")


def get_portfolio1(request: HttpRequest):
    return render(request, "portfolio/portfolio1.html")


def get_portfolio2(request: HttpRequest):
    return render(request, "portfolio/portfolio2.html")

