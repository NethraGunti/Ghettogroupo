from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.urls import reverse_lazy

from users.models import User, UserProfile, Interest
from users.forms import UserRegistrationForm, UserProfileForm

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


@login_required
def userprofile(request):
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user.profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = user
            profile.save()

            int_list = form.cleaned_data['interest']
            #remove unchecked interests
            for i in profile.interest.all():
                if i not in int_list:
                    profile.interest.remove(i)
            #add new interests
            for i in int_list:
                if i not in profile.interest.all():
                    profile.interest.add(i)


            return redirect(reverse_lazy('landing-page'))
    else:
        form = UserProfileForm(instance=user.profile)
    return render(request, 'users/profile.html', {'form':form})
