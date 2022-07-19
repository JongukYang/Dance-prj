from django.shortcuts import redirect, render
# 로그인 로그아웃 할 때 꼭 필요한거
from django.contrib import auth
from django.contrib.auth.models import User
import requests
from secret_data import s_restApiKey

# Create your views here.
def login(request):
    # request == POST : 로그인
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # authenticate 메소드는 username,password가 일치하는 객체를 반환함(만약 없으면 NONE반환)
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'bad_login.html')
    # request == GET : 로그아웃
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def signup(request):
    if request.method == "POST":
        if request.POST['password'] == request.POST['repeat']:
            print(request.POST)
            new_user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            auth.login(request, new_user, backend='django.contrib.auth.backends.ModelBackend',)
            return redirect('home')
    return render(request, 'register.html')


## 여기부터 카카오 로그인 구현
def kakaoLoginLogic(request):
    _restApiKey = s_restApiKey
    _redirectUrl = 'http://127.0.0.1:8000/kakaoLoginLogicRedirect'
    _url = f'https://kauth.kakao.com/oauth/authorize?client_id={_restApiKey}&redirect_uri={_redirectUrl}&response_type=code'
    return redirect(_url)

def kakaoLoginLogicRedirect(request):
    _qs = request.GET['code']
    _restApiKey = s_restApiKey
    _redirect_uri = 'http://127.0.0.1:8000/kakaoLoginLogicRedirect'
    _url = f'https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={_restApiKey}&redirect_uri={_redirect_uri}&code={_qs}'
    _res = requests.post(_url)
    _result = _res.json()
    request.session['access_token'] = _result['access_token']
    request.session.modified = True
    return render(request, 'loginSuccess.html')

def kakaoLogout(request):
    _token = request.session['access_token']
    ## 방법 1
    # _url = 'https://kapi.kakao.com/v1/user/logout'
    # _header = {
    #     'Authorization': f'bearer {_token}'
    # }
    ## 방법 2
    _url = 'https://kapi.kakao.com/v1/user/unlink'
    _header = {
      'Authorization': f'bearer {_token}',
    }
    _res = requests.post(_url, headers=_header)
    _result = _res.json()
    if _result.get('id'):
        del request.session['access_token']
        return render(request, 'loginoutSuccess.html')
    else:
        return render(request, 'logoutError.html')

    
