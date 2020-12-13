from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def landing_page(request):
    return render(request, 'general/landing-page.html', {'user':request.user})

@login_required
def dashboard(request):
    groups = request.user.get_groups()
    return render(request, 'general/dashboard.html', {'groups':groups})