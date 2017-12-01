from django.http import HttpResponse
from django.shortcuts import render
from news.models import news
def index(request):

    return render(request,'index.html')
