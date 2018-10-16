from django.urls import path
from . import views


urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('profile/', views.profile, name='profile'),
    path('signout/', views.signout, name='signout'),
]
