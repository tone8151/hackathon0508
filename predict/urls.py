from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'predict'
urlpatterns = [
    path('<int:pk>/', views.index, name='index'),
]