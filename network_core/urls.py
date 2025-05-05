from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_profile, name='create_profile'),
    path('edit/', views.create_profile, name='edit_profile'),  # Using create_profile view for editing
    path('', views.profile_view, name='my_profile'),  # Current user's profile
    path('<str:username>/', views.profile_view, name='profile'),  # Another user's profile
    path('logout/', views.logout_view, name='logout'),
]