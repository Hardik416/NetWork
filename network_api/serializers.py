from rest_framework import serializers
from network_auth.models import Profile, Experience, Education, Skill
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ['id', 'job_title', 'company', 'start_date', 'end_date', 'currently_working']

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ['id', 'institution', 'degree', 'start_year', 'end_year']

class SkillSerializer(serializers.ModelSerializer):
    level_text = serializers.CharField(read_only=True)
    
    class Meta:
        model = Skill
        fields = ['id', 'name', 'proficiency', 'level_text']

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    experiences = ExperienceSerializer(many=True, read_only=True)
    educations = EducationSerializer(many=True, read_only=True)
    skills = SkillSerializer(many=True, read_only=True)
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = [
            'id', 'user', 'first_name', 'last_name', 'full_name',
            'title', 'location', 'short_bio', 'about',
            'email', 'phone', 'github', 'twitter',
            'profile_image', 'profile_visibility',
            'show_email', 'show_phone',
            'experiences', 'educations', 'skills'
        ]
        read_only_fields = ['user']

    def get_full_name(self, obj):
        return obj.get_full_name() 