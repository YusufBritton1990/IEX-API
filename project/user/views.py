from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form':form})



# def Login.as_view()
