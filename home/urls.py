from django.contrib import admin
from django.urls import path,include
from home import views 

urlpatterns = [
   
    path('',views.home, name='home'),
    path("about",views.about, name='about'),
    path("topGainer",views.topGainer, name='top_gainer'),
    path("topLosers",views.topLosers, name='top_losers'),
    path("fnoLotsize",views.fnoLotsize, name='fno_lotsize'),
    path("preopenNifty",views.preopenNifty, name='preopen_nifty'),
    path("preopenNiftybank",views.preopenNiftybank, name='preopen_niftybank'),
    path("preopenFno",views.preopenFno, name='preopen_fno'),
    path("topFnoGainer",views.topFnoGainer, name='top_Fno_gainer'),
    path("topFnoLosers",views.topFnoLosers, name='top_Fno_losers'),
    path("indexList",views.indexList, name='index_list'),
    path("indexInfo/",views.indexInfo, name='indexInfo'),
    path("quote_info/", views.quote_info, name='quote_info'),
    path("contact",views.contact, name='contact'),
    path("search",views.search, name='Search'),
    path("signup",views.handleSignup, name='handleSignup'),
    path('login',views.handleLogin,name='handleLogin'), 
    path('logout',views.handleLogout,name='handleLogout')
]
