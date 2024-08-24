from django.urls import path,include
from . import views




urlpatterns = [
    
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('registration', views.registration, name='registration'),
    path('loginPage', views.loginPage, name='loginPage'),
    path('home', views.home, name='home'),
    path('dashbord', views.dashbord, name='dashbord'),
    path('api/get_countries/', views.get_countries, name='get_countries'),
    path('api/get_states/', views.get_states, name='get_states'),
    path('api/get_cities/', views.get_cities, name='get_cities'),
   
]
