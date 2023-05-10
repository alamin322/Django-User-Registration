from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('userprofile/', views.user_profile, name='user_profile_page'),
    path('login/', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]
