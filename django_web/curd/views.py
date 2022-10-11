from django.shortcuts import render, redirect


def index(request):

    return render(request, "curd/index.html")


def login(request):

    return render(request, "curd/login.html")


def chronos_performance(request):

    return render(request, "curd/chronos_perf.html")


def chronos_performance_view(request):
    platform = request.GET.get("platform")
    models = request.GET.getlist("models")
    framework = request.GET.get("framework")
    date = request.GET.get("date")
    print("performance", platform, models, framework, date)
    return redirect("chronos_performance")


def chronos_accuracy(request):

    return render(request, "curd/chronos_acc.html")


def chronos_accuracy_view(request):
    platform = request.GET.get("platform")
    models = request.GET.getlist("models")
    framework = request.GET.get("framework")
    date = request.GET.get("date")
    print("accuracy", platform, models, framework, date)
    return redirect("chronos_accuracy")

