from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from .models import news
# Create your views here.
def index(request):
    allnews=news.objects.all()
    agnecies=news.objects.values_list('Agency',flat=True).distinct()
    return render(request,'indexnews.html',{'news':allnews,'agencies':agnecies})
def type(request,type):
    allnews=news.objects.filter(category=type)
    return render(request,'indexnews.html',{'news':allnews})


