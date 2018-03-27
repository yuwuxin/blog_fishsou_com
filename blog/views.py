from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'index.html')


def list(request):
    return render(request, 'list.html')


def article(request, id):
    print(id)
    return render(request, 'detail.html')


def about(request):
    return render(request, 'about.html')