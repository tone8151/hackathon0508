from django.conf.urls import url
from django.contrib.auth.views import LogoutView
from . import views
from django.urls import path

urlpatterns = [
    path('create/', views.create_account, name='create_account'),
    path('login/', views.account_login, name='login'),
    path('logout/', LogoutView.as_view(template_name='predict/mainpage.html'), name='logout'),
]