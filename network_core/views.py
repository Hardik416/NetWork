# views.py

from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.forms import modelformset_factory
from django.contrib import messages
from .forms import ProfileForm, ExperienceForm, EducationForm, SkillForm
from network_auth.models import Profile, Experience, Education, Skill

@login_required
def create_profile(request):
    """View to create or edit a user's profile."""
    profile, created = Profile.objects.get_or_create(user=request.user)

    ExperienceFormSet = modelformset_factory(
        Experience, 
        form=ExperienceForm, 
        extra=1, 
        can_delete=True
    )
    EducationFormSet = modelformset_factory(
        Education, 
        form=EducationForm, 
        extra=1, 
        can_delete=True
    )
    SkillFormSet = modelformset_factory(
        Skill,
        form=SkillForm,
        extra=1,
        can_delete=True
    )

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        experience_formset = ExperienceFormSet(
            request.POST, 
            queryset=Experience.objects.filter(profile=profile),
            prefix='experience'
        )
        education_formset = EducationFormSet(
            request.POST, 
            queryset=Education.objects.filter(profile=profile),
            prefix='education'
        )
        skill_formset = SkillFormSet(
            request.POST,
            queryset=Skill.objects.filter(profile=profile),
            prefix='skill'
        )

        if (profile_form.is_valid() and experience_formset.is_valid() and 
            education_formset.is_valid() and skill_formset.is_valid()):
            profile = profile_form.save()

            experiences = experience_formset.save(commit=False)
            for exp in experiences:
                exp.profile = profile
                exp.save()
            for obj in experience_formset.deleted_objects:
                obj.delete()

            educations = education_formset.save(commit=False)
            for edu in educations:
                edu.profile = profile
                edu.save()
            for obj in education_formset.deleted_objects:
                obj.delete()

            skills = skill_formset.save(commit=False)
            for skill in skills:
                skill.profile = profile
                skill.save()
            for obj in skill_formset.deleted_objects:
                obj.delete()

            messages.success(request, 'Profile updated successfully!')
            return redirect('my_profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        profile_form = ProfileForm(instance=profile)
        experience_formset = ExperienceFormSet(
            queryset=Experience.objects.filter(profile=profile),
            prefix='experience'
        )
        education_formset = EducationFormSet(
            queryset=Education.objects.filter(profile=profile),
            prefix='education'
        )
        skill_formset = SkillFormSet(
            queryset=Skill.objects.filter(profile=profile),
            prefix='skill'
        )

    context = {
        'profile_form': profile_form,
        'experience_formset': experience_formset,
        'education_formset': education_formset,
        'skill_formset': skill_formset,
        'is_edit': not created,
    }
    
    return render(request, 'network_core/create_profile.html', context)

@login_required
def profile_view(request, username=None):
    """
    View to display a user's profile.
    If username is provided, show that user's profile.
    If no username, show the logged-in user's profile.
    """
    try:
        if username:
            profile = get_object_or_404(Profile, user__username=username)
        else:
            profile = get_object_or_404(Profile, user=request.user)
            
        experiences = Experience.objects.filter(profile=profile).order_by('-start_date')
        education = Education.objects.filter(profile=profile).order_by('-end_year')
        skills = profile.skills.all()
        
        context = {
            'profile': profile,
            'experiences': experiences,
            'education': education,
            'skills': skills,
            'is_own_profile': request.user == profile.user
        }
        
        return render(request, 'network_core/profile.html', context)
        
    except Profile.DoesNotExist:
        if username:
            messages.error(request, f"Profile for user {username} does not exist.")
            return redirect('login_register')
        else:
            messages.info(request, "Please create your profile first.")
            return redirect('create_profile')

def logout_view(request):
    """View to handle user logout."""
    logout(request)
    messages.info(request, "You have been logged out successfully.")
    return redirect('login_register')