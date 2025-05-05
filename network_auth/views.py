from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from network_auth.models import Profile
from django.core.exceptions import ObjectDoesNotExist


def login_register(request):
    return render(request, 'auth/login_register.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user_qs = User.objects.filter(email=email)
        if user_qs.exists():
            user = user_qs.first()
            user = authenticate(request, username=user.username, password=password)
            if user is not None:
                if not Profile.objects.filter(user=user).exists():
                    Profile.objects.create(
                        user=user,
                        first_name=user.first_name,
                        last_name=user.last_name,
                        title='',
                        location='',
                        short_bio='',
                        about=''
                    )
                
                login(request, user)

                if user.profile.short_bio:
                    return redirect('my_profile')
                else:
                    return redirect('create_profile')
            else:
                messages.error(request, 'Invalid credentials.')
        else:
            messages.error(request, 'Email not found.')
    return redirect('login_register')


def signup_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already registered.')
            return redirect('login_register')

        username = email.split('@')[0]
        counter = 1
        base_username = username
        while User.objects.filter(username=username).exists():
            username = f"{base_username}{counter}"
            counter += 1

        name_parts = name.split(' ', 1)
        first_name = name_parts[0]
        last_name = name_parts[1] if len(name_parts) > 1 else ''

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )

        profile = Profile.objects.get(user=user)
        profile.first_name = first_name
        profile.last_name = last_name
        profile.save()

        login(request, user)
        return redirect('create_profile')
    
    return redirect('login_register')


def logout_view(request):
    logout(request)
    return redirect('login_register')
