from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Category
from blog.models import AdPosition


# Create your views here.
def index(request):
    nav_list = Category.objects.all()
    banner_list = AdPosition.objects.all()
    return render(request, 'index.html', {'nav_list': nav_list, 'banner_list': banner_list})


def list(request):
    nav_list = Category.objects.all()
    return render(request, 'list.html', {'nav_list': nav_list})


def article(request, id):
    print(id)
    nav_list = Category.objects.all()
    return render(request, 'detail.html', {'nav_list': nav_list})


def about(request):
    nav_list = Category.objects.all()
    return render(request, 'about.html', {'nav_list': nav_list})
