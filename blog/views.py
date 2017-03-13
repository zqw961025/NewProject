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


