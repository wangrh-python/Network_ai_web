from django.shortcuts import render, redirect


def index(request):
    return render(request, "curd/index.html")


def login(request):
    return render(request, "curd/login.html")

