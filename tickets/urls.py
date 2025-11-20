from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('login/', views.login_page, name='login'),
    path('create_profile/', views.create_profile, name='create_profile'),
    path('home/', views.home, name='home'),
    path('my_passes/', views.my_passes, name='my_passes'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_user, name='logout'),
    path('api/stations/', views.station_suggestions, name='station_suggestions'),
    path('fare/', views.show_fare, name='show_fare'),
    path('booking-success/', views.booking_success, name='booking_success'),

]
