from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings 
from django.conf.urls.static import static  
urlpatterns = [
    path('', 
        views.HomePage.as_view(), name='home'),
        path('login/', views.login_view, name='login'),
        path('register/', views.register_view, name='register'),
        path('logout/', auth_views.LogoutView.as_view(), name='logout'),
        path('services/', views.services_page, name='services_page'),
        path('book/<int:service_id>/', views.book_service, name='book_service'),
        path('profile/', views.profile, name='profile'),
        path('update/<int:booking_id>/', views.update_booking, name='update_booking'),
        path('delete/<int:booking_id>/', views.delete_booking, name='delete_booking'),
        path('about_us/', views.about_us, name='about'),
]
