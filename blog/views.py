# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse 
from . import models
# Create your views here.
def hellos(request):
	data = '帅吧'
	return render(request,'blog/blog.html',{'hello' : data})
def index(request):
	articles = models.Article.objects.all()
	return render(request,'blog/index.html',{'articles' : articles})


def article(request,article_id):
	article = models.Article.objects.get(pk=article_id)
	return render(request,'blog/article_page.html',{'article' : article})