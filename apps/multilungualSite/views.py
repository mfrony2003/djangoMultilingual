from .models.model import Menu, Blog
from django.shortcuts import render
from django.conf import settings


# Create your views here.
def Home(request):
     
     lang= settings.LANGUAGE_CODE
    
     return render(request,'blog.html',{'menus': Menu.objects.all(),'Blogs': Blog.objects.all(),'lang':lang})

def Single(request):
    
     return render(request,'test.html',{'menus': Menu.objects.all(),'Blogs': Blog.objects.all()})

