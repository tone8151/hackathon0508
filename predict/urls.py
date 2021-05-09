from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'predict'
urlpatterns = [
    path('<int:match_pk>/', views.predict, name='predict'),
    path('mypage/', views.mypage, name='mypage'),
    # path('<int:pk>/', views.Index.as_view(), name='index'),
    # path('', views.predict, name='predict'),
]