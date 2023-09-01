from django.urls import path
from . import views

urlpatterns = [
    path('', views.accordion, name='accordion'),
    path('home', views.home, name='home'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),

]
