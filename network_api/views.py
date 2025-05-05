from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from network_auth.models import Profile, Experience, Education, Skill
from .serializers import (
    ProfileSerializer, ExperienceSerializer,
    EducationSerializer, SkillSerializer
)

# Create your views here.

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Profile.objects.all()
        # Filter by visibility
        if not self.request.user.is_staff:
            queryset = queryset.filter(profile_visibility='public')
        return queryset

    @action(detail=True, methods=['get'])
    def experiences(self, request, pk=None):
        profile = self.get_object()
        experiences = profile.experiences.all()
        serializer = ExperienceSerializer(experiences, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def educations(self, request, pk=None):
        profile = self.get_object()
        educations = profile.educations.all()
        serializer = EducationSerializer(educations, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def skills(self, request, pk=None):
        profile = self.get_object()
        skills = profile.skills.all()
        serializer = SkillSerializer(skills, many=True)
        return Response(serializer.data)

class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [permissions.IsAuthenticated]

class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = [permissions.IsAuthenticated]

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [permissions.IsAuthenticated]
