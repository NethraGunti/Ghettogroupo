from django.shortcuts import render,redirect
from django.urls import reverse_lazy

from users.models import User, UserProfile, Interest
from users.forms import UserRegistrationForm, UserProfileForm, InterestForm

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

def user_profile(request, pk):
   
    if request.POST:
        profile_form = UserProfileForm(request.POST,request.FILES)
        interest_form = InterestForm(request.POST)
        if profile_form.is_valid() and interest_form.is_valid():

            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save()

            interests = interest_form.save(commit=False)
            interests.user = request.user
            interests.save()

            return redirect('landing-page')
    else:
        profile_form = UserProfileForm()
        interest_form = InterestForm()
    return render(request, 'users/userprofile.html', {'user' : User.objects.get(pk=pk),'profile_form' : profile_form,'interest_form' : interest_form})


