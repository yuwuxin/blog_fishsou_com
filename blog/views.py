from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Category
from blog.models import AdPosition
from blog.models import Article


# Create your views here.
def index(request):
    nav_list = Category.objects.all()
    banner_list = AdPosition.objects.all()
    article_list = Article.objects.all()

    return render(request, 'index.html',
                  {'nav_list': nav_list, 'banner_list': banner_list, 'article_list': article_list})


def list(request, c_id):
    nav_list = Category.objects.all()
    article_list = Article.objects.filter(category_id=c_id)

    return render(request, 'list.html', {'nav_list': nav_list, 'article_list': article_list})


def article(request, id):
    print(id)
    nav_list = Category.objects.all()
    return render(request, 'detail.html', {'nav_list': nav_list})


def about(request):
    nav_list = Category.objects.all()
    return render(request, 'about.html', {'nav_list': nav_list})
