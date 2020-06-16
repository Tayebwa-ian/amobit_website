# Use include() to add paths from the catalog application 
from django.urls import path
from django.conf import settings
from django.conf.urls import include, url
from .import views


app_name='oursite'
urlpatterns = [    
    path('index/',views.index,name='index'),
    path('index/contact-us', views.contact ,name='contact'),
    path('index/register',views.register, name='register'),
    path('index/about-us',views.about_us, name='about_us'),
    path('index/services',views.services, name='services'),
    path('index/products',views.products,name='products'),
]
