# Create your views here.
from pages.models import Page
from django.shortcuts import render

def index(request):
    words = Page.objects.all()
    return render(request , 'pages/page_list.html' ,{'words':words} )
