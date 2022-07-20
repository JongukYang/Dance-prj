from turtle import Turtle
from secret_data import s_restApiKey
from django.shortcuts import redirect, render
import json
import requests
from .forms import PostForm, CommentForm
from .models import Post, Comment


# Create your views here.
def index(request):
    _context = {'check':False}
    if request.session.get('access_token'):
        _context['check'] = True
    return render(request, 'index.html', _context)
    
# def home(request):
#     return render(request, 'index.html')

def loginform(request):
    return render(request, 'loginform.html')

def postcreate(request):
    # request 메소드가 POST일 경우 입력 값 저장
    if request.method == 'POST' or request.method == 'FILES':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # 폼에서 받아온 데이터를 아직 입력하지 않아서 form.save를 하지 않고 다 저장한 후 save 진행
            unfinished = form.save(commit=False) 
            unfinished.author = request.user # auther가 누구인지 알기 위해 user 가져옴
            unfinished.save()
            return redirect('index')
    # request.method == 'GET' 일 경우, from 입력 html 띄우기
    else:
        form = PostForm()
    return render(request, 'postform.html', {'form':form})



