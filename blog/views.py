from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article

# Create your views here.

def Test(request):
    post = Article.objects.all()
    return HttpResponse(post[0].content)
