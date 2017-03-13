# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
 
from Model.models import Test
from blog.models import Author,Article 
# 数据库操作
def testdb(request):
    # 修改其中一个id=1的name字段，再save，相当于SQL中的UPDATE
    test1 = Article(title='老王的博客',content='这是老王的第一个博客',author_id=1)
    test1.save()
    
    # 另外一种方式
    #Test.objects.filter(id=1).update(name='Google')
    
    # 修改所有的列
    # Test.objects.all().update(name='Google')
    
    return HttpResponse("<p>修改成功</p>")