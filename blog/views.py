from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Category
from blog.models import AdPosition
from blog.models import Article


# Create your views here.
def index(request):
    banner_list = AdPosition.objects.all()
    article_list = Article.objects.all().order_by('-id')

    return render(request, 'index.html',
                  {'banner_list': banner_list, 'article_list': article_list})


def list(request, c_id):
    article_list = Article.objects.filter(category_id=c_id).order_by('-id')

    return render(request, 'list.html', {'article_list': article_list})


def article(request, id):
    article = Article.objects.filter(id=id)[0]
    return render(request, 'detail.html', {'article': article})


def about(request):
    return render(request, 'about.html')
