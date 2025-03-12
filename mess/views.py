from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm

from mess.models import ROLE_CHOICES, CustomUser
from .forms import  SignupForm
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages
from django.contrib.auth.hashers import make_password  # Import make_password



# Create your views here.
def index(request):
    return render(request, 'index.html')

def menu(request):
    return render(request,'menu.html')
def reciept(request):
    return render(request,'reciept.html')
def signupPage(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # Manually create and save a CustomUser instance
            user = CustomUser(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],  # Hash the password in production
                role=form.cleaned_data['role'],
                registration_number=form.cleaned_data['registration_number']
            )
            user.save()
            messages.success(request, 'Account created successfully!')
            return redirect('loginPage')  # Redirect to the login page or another view
    else:
        form = SignupForm()
    
    return render(request, 'signup.html', {'form': form})
def signupPage(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # Manually create and save a CustomUser instance
            user = CustomUser(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=make_password(form.cleaned_data['password1']),  # Use 'password1' here
                role=form.cleaned_data['role'],
                registration_number=form.cleaned_data['registration_number']
            )
            user.save()
            messages.success(request, 'Account created successfully!')
            return redirect('index')  # Redirect to the login page or another view
    else:
        form = SignupForm()
    
    return render(request, 'signup.html', {'form': form})
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Log the user in
            login(request, user)
            messages.success(request, f'Welcome back, {username}!')
            return redirect('index')  # Redirect to the home page or dashboard
        else:
            # Show an error message if authentication fails
            messages.error(request, 'Invalid username or password. Please try again.')
    context = {'ROLE_CHOICES': ROLE_CHOICES}
    # Render the login page
    return render(request, 'login.html', context)

def logoutPage(request):
    # Log the user out
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('loginPage')  # Redirect to the login page or home page
