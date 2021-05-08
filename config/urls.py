from django.contrib import admin
from django.urls import path, include #追加（アプリ）
from django.conf import settings  #追加（静的ファイル）
from django.conf.urls.static import static  #追加（静的ファイル）
from .views import toppage, main

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', toppage, name='toppage'),  
    path('main/', main, name='main'),                 
    path('accounts/', include('accounts.urls')),       
    path('predict/', include('predict.urls')), 
    path('matches/', include('matches.urls')), 
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 

