from django.shortcuts import render

def landing_page(request):
    return render(request, 'general/landing-page.html', {'user':request.user})