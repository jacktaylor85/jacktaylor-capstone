from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', 
        views.HomePage.as_view(), name='home'),
        path('login/', views.login_view, name='login'),
        path('register/', views.register_view, name='register'),
        path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
