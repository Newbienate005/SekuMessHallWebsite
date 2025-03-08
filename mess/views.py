from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    return render(request, 'index.html')

def menu(request):
    return render(request,'menu.html')
def reciept(request):
    return render(request,'reciept.html')

def user_signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        role = request.POST.get("role")
        registration_number = request.POST.get("registration_number", None)

        if role == "Student" and not registration_number:
            return JsonResponse({"error": "Registration number is required for students"}, status=400)

        user = User.objects.create_user(username=username, password=password)
        user.role = role
        user.registration_number = registration_number
        user.save()

        return JsonResponse({"message": "Signup successful"}, status=201)

    return render(request, "signup.html")
def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return JsonResponse({"message": "Login successful"}, status=200)
        else:
            return JsonResponse({"error": "Invalid credentials"}, status=400)

    return render(request, "login.html")

def user_logout(request):
    logout(request)
    return redirect("login")
def user_logout(request):
    logout(request)
    return redirect("login")