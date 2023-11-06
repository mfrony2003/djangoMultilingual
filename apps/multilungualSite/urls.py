from django.urls import path
from apps.multilungualSite import views


urlpatterns = [    
      path('',views.Home, name='Home'), 
      path('blog-single',views.Single, name='Single'), 
      
]