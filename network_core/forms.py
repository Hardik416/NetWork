
from django import forms
from network_auth.models import Profile, Experience, Education, Skill
from django.forms import inlineformset_factory

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'first_name', 'last_name', 'title', 'location', 'short_bio', 'about',
            'profile_image', 'phone', 'github', 'twitter', 'show_email', 'show_phone'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Last Name'}),
            'title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Professional Title'}),
            'location': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Location'}),
            'short_bio': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 3, 'placeholder': 'Short Bio'}),
            'about': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 5, 'placeholder': 'About Me'}),
            'profile_image': forms.FileInput(attrs={'class': 'form-input'}),
            'phone': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Phone Number'}),
            'github': forms.URLInput(attrs={'class': 'form-input', 'placeholder': 'GitHub Profile URL'}),
            'twitter': forms.URLInput(attrs={'class': 'form-input', 'placeholder': 'Twitter Profile URL'}),
            'show_email': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'show_phone': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['job_title', 'company', 'start_date', 'end_date', 'currently_working']
        widgets = {
            'job_title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Job Title'}),
            'company': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Company'}),
            'start_date': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'currently_working': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['institution', 'degree', 'start_year', 'end_year']
        widgets = {
            'institution': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Institution'}),
            'degree': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Degree'}),
            'start_year': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'end_year': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'})
        }

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        exclude = ('profile',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Skill Name'}),
            'proficiency': forms.Select(attrs={'class': 'form-select'})
        }

ExperienceFormSet = inlineformset_factory(
    Profile, Experience,
    form=ExperienceForm,
    extra=1,
    can_delete=True,
    min_num=0,
    validate_min=False
)

EducationFormSet = inlineformset_factory(
    Profile, Education,
    form=EducationForm,
    extra=1,
    can_delete=True,
    min_num=0,
    validate_min=False
)

SkillFormSet = inlineformset_factory(Profile, Skill, form=SkillForm, extra=1, can_delete=True)
