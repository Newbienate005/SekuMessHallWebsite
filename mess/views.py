from django.shortcuts import redirect, render
from django.contrib.auth.models import User

from mess.forms import  UserForm


# Create your views here.
def index(request):
    return render(request, 'index.html')

def menu(request):
    return render(request,'menu.html')
def reciept(request):
    return render(request,'reciept.html')

def signup(request):
    form=UserForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect ('index')
        
        else: form = UserForm()



    return render(request,'signup.html', {'form': form})
   