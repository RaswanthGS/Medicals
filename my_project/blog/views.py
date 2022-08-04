from django.shortcuts import render


def home(request):
    return render(request, 'base/main.html')
