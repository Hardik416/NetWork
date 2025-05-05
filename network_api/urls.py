from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'profiles', views.ProfileViewSet)
router.register(r'experiences', views.ExperienceViewSet)
router.register(r'educations', views.EducationViewSet)
router.register(r'skills', views.SkillViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
] 