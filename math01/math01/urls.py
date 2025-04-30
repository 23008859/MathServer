from django.contrib import admin
from django.urls import path
from mathapp1 import views

urlpatterns = [
     path('admin/', admin.site.urls),
    path('',views.power,name='home'),


]
