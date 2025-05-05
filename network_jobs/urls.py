from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('<int:job_id>/', views.get_job_details, name='job_details'),
    path('apply/', views.apply_for_job, name='apply_for_job'),
    path('post/', views.post_job, name='job_posting'),
    path('search/', views.job_searching, name='job_searching'),
]
