from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from mess.forms import  MenuItemForm, SignupForm
from mess.models import MenuItem, User


# Create your views here.
def index(request):
    return render(request, 'index.html')

def menu(request):
    return render(request,'menu.html')
def reciept(request):
    return render(request,'reciept.html')

def signup(request):
    if request.method == 'POST':
        form =  SignupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'User record has been added successfully.')
            return redirect('index')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})
            
def login(request):
    return  render(request, 'login.html')
def menu_view(request):
    menu_items = MenuItem.objects.all()
    return render(request, "menu.html", {"menu_items": menu_items})
def edit(request, id):
    menuitem = get_object_or_404(MenuItem, id=id)  # Ensure instance retrieval

    if request.method == 'POST':
        form = MenuItemForm(request.POST, request.FILES, instance=menuitem)  # Correct form usage
        if form.is_valid():
            form.save()
            messages.success(request, 'Your changes have been saved.')
            return redirect('menusitem')  # Ensure 'menusitem' is a valid URL name
        else:
            messages.error(request, 'Something went wrong.')
    else:
        form = MenuItemForm(instance=menuitem)

    return render(request, 'mess/edit.html', {'form': form, 'menuitem': menuitem})

def delete(request, id):
    menuitem = get_object_or_404(MenuItem, id=id)

    try:
        menuitem.delete()
    except Exception as e:
        messages.error(request, "Something went wrong.")

    return redirect('menusitem')