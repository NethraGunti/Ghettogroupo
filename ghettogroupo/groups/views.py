from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def test_view(request, username, code):
    print(username, code)
    return HttpResponse(username+str(code))