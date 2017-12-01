from django.shortcuts import render
from django.http import HttpResponse
from .models import news
# Create your views here.
def index(request):
    allnews=news.objects.all()
    return render(request,'indexnews.html',{'news':allnews})
