from django.shortcuts import render
from .models import *


def index(request):
    news = News.objects.all()
    categories = Categories.objects.all()
    context = {
        'news': news,
        'categories': categories,
    }
    return render(request, 'news/index.html', context=context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    categories = Categories.objects.all()
    category = Categories.objects.get(pk=category_id)
    return render(request, 'news/category.html', {'news': news, 'categories': categories, 'category': category})
