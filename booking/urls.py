from . import views
from django.urls import path

urlpatterns = [
    path('', 
        views.HomePage.as_view(), name='home'),
        path('login/', views.login_view, name='login'),
        path('register/', views.register_view, name='register'),
]
