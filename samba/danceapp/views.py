from turtle import Turtle
from django.shortcuts import redirect, render
import json
import requests
from secret_data import s_restApiKey

# Create your views here.
def index(request):
    _context = {'check':False}
    if request.session.get('access_token'):
        _context['check'] = True
    return render(request, 'index.html', _context)
    



