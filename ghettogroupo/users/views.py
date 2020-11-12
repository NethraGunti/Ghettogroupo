from django.shortcuts import render,redirect
from django.urls import reverse_lazy

from users.models import User
from users.forms import UserRegistrationForm

def landing_page(request):
    return render(request, 'users/home.html')

def UserRegisterView(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('landing-page')
    else:
        form = UserRegistrationForm()
    return render(request,'users/register.html', {'form':form})
