from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from .forms import RegistrationForm, LoginForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if User.objects.filter(email=email).exists():
                messages.error(request, "Email already registered.")
                return redirect('register')
            form.save()
            return redirect('welcome', email=email)
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(email=email, password=password)
                return redirect('welcome', email=user.email)
            except User.DoesNotExist:
                messages.error(request, "Invalid credentials.")
                return redirect('login')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def welcome(request, email):
    user = User.objects.get(email=email)
    return render(request, 'welcome.html', {'user': user})
