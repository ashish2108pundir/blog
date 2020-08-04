from django.contrib import admin
from django.urls import path
from Blog import views


urlpatterns = [

path("",views.index,name="home"),
path("homestay/",views.homestay,name="homestay"),
path("blog/",views.blog,name="blog"),
path("contact/",views.contact,name="contact"),
path('homestay/<str:slug>',views.homestays,name="homestays"),


]