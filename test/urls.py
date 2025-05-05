from django.urls import path
from . import views

urlpatterns = [
    # ... existing urls ...
    path('jobs/', views.job_list, name='job_list'),
    path('jobs/<int:job_id>/', views.get_job_details, name='job_details'),
    path('jobs/apply/', views.apply_for_job, name='apply_for_job'),
    path('jobs/post/', views.post_job, name='post_job'),
] 