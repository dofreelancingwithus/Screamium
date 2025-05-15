from django.urls import path
from . import views
from django.contrib import admin

admin.site.site_header = 'Screamium Ice Creams Admin'
admin.site.site_title = 'admin'
admin.site.index_title = 'Welcome to Screamium Ice Creams'


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('servicescopy/', views.servicescopy, name='servicescopy'),
    path('otherservices/', views.otherservices, name='otherservices'),
    path('order/', views.order, name='order'),
    
]
