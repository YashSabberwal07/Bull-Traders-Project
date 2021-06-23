from django.contrib import admin
from django.urls import path,include
from home import views 

urlpatterns = [
   
    path('',views.home, name='home'),
    path("about",views.about, name='about'),
    path("topGainer",views.topGainer, name='top_gainer'),
    path("topLosers",views.topLosers, name='top_losers'),
    path("indexInfo/",views.indexInfo, name='indexInfo'),
    path("contact",views.contact, name='contact'),
    path("search",views.search, name='Search'),
    path("signup",views.handleSignup, name='handleSignup'),
    path('login',views.handleLogin,name='handleLogin'), 
    path('logout',views.handleLogout,name='handleLogout')
]