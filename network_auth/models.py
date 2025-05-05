from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

PROFILE_VISIBILITY_CHOICES = [
    ('public', 'Public'),
    ('connections', 'Connections Only'),
    ('private', 'Private'),
]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    short_bio = models.TextField()
    about = models.TextField()
    
    email = models.EmailField(max_length=255, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    
    github = models.URLField(max_length=255, blank=True)
    twitter = models.URLField(max_length=255, blank=True)
    
    profile_image = models.ImageField(upload_to='profile_pics/', default='profile_pics/default.jpg')
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    profile_visibility = models.CharField(max_length=20, choices=PROFILE_VISIBILITY_CHOICES, default='public')
    show_email = models.BooleanField(default=True)
    show_phone = models.BooleanField(default=False)


class Experience(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='experiences')
    job_title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    currently_working = models.BooleanField(default=False)

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.job_title} at {self.company}"


class Education(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='educations')
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    start_year = models.DateField()
    end_year = models.DateField()

    class Meta:
        ordering = ['-end_year']
        verbose_name_plural = "Education"

    def __str__(self):
        return f"{self.degree} at {self.institution}"


class Skill(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(choices=[(i, str(i)) for i in range(1, 101)], default=50)
    
    @property
    def level_text(self):
        try:
            prof = int(self.proficiency)
            if prof <= 33:
                return "Beginner"
            elif prof <= 66:
                return "Intermediate"
            else:
                return "Advanced"
        except (ValueError, TypeError):
            return "Not Specified"

    def __str__(self):
        return f"{self.name} ({self.proficiency})"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Create a Profile instance whenever a new User is created."""
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """Ensure the Profile is saved whenever the User is saved."""
    instance.profile.save()
