from django.urls import path
from . import views


app_name = "render"

urlpatterns = [
    path('', views.index, name='index'),
    path('next', views.next, name='next')
]