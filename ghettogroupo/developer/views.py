from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from developer.models import DeveloperKey

@login_required
def get_keys(request):
    developer = DeveloperKey.objects.filter(user=request.user).first()
    if developer:
        keys = True
        ci = developer.client_id
        sk = developer.secret_key
    else:
        keys = False
        ci = None
        sk = None
    return render(request, 'developer/keys.html', {'keys': keys, 'ci': ci, 'sk': sk})

@login_required
def gen_keys(request):
    developer = DeveloperKey.objects.filter(user=request.user).first()
    if not developer:
        new_keys = DeveloperKey.objects.create(
            user=request.user
        )
        new_keys.save()
    
    return redirect(reverse_lazy('developer'))
