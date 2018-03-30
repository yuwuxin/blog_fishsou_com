from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article


# Create your views here.
def index(request):
    title = Article.objects.get(id='')
    return render(request, 'index.html', {'title': title})


def list(request):
    return render(request, 'list.html')


def article(request, id):
    print(id)
    return render(request, 'detail.html')


def about(request):
    return render(request, 'about.html')
