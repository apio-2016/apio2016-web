# -*- coding: utf-8 -*-

from django.shortcuts import render

from .models import News

def news(request):
    news = News.objects.filter(disabled=False).order_by('-created_datetime')
    return render(request, 'news.html', {'news': news})