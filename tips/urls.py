from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('home/', views.home, name = "home"),
    path('results/', views.results, name = "results"),
    path('subscribe/', views.subscribe, name = "subscribe"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name = "register"),
    path('information/', views.information, name = "information"),
    path('homeVip/', views.viphome, name = "home/vip"),
    path('vipTips/', views.vipTips, name = "vip/Tips"),
    path('punter/', views.punter, name = "vip/Tips"),
    path('roll/', views.roll, name = "vip/Tips"),
    path('play/', views.play, name = "play"),
]
