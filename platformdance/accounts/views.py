from xml.dom import UserDataHandler
from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# from django.contrib.auth.models import User
from .models import userProfile

# Create your views here.
# def login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             auth.login(request, form.get_user())
#             return redirect('index')
#     else:
#         form = AuthenticationForm()

#     context = {
#         'form':form,
#     }
#     return render(request, 'login.html', context)

def login(request):
    if request.method == 'POST':
        _id = request.POST["username"]
        _pass = request.POST["password"]
        # _nickname=request.POST["nickname"]
        user = auth.authenticate(request, 
        username=_id, 
        password=_pass, 
        # nickname=_nickname
        )
        print(_id, _pass, user)

        if user is not None:
            auth.login(request, user)
            return redirect('index')

    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('index')

# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             auth.login(request, user)
#             return redirect('index')
#     else:
#         form = UserCreationForm()
    
#     context = {
#         'form':form,
#     }
#     return render(request, 'signup.html', context)

def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['repeat']:
            new_user = userProfile.objects.create_user(
                username=request.POST['username'], 
                password=request.POST['password'],
                nickname=request.POST['nickname'],
                # danceSkill=request.POST['user_level'],
                )
            auth.login(request, new_user)
            return redirect('index')      
    return render(request, 'signup.html')


# def signup(request):
#     if request.method == 'POST':
#         if request.POST['password'] == request.POST['repeat']:
#             new_user = userProfile.objects.create_user(
#                 username=request.POST['username'], 
#                 password=request.POST['password'],
#                 nickname=request.POST['nickname'],
#                 danceSkill=request.POST['user_level'],
#                 # phoneNum=request.POST['phoneNum'],
#                 # gender=request.POST['gender'],
#                 # createdAt=request.POST['createdAt'],
#                 # birth=request.POST['birth'],
#                 )
#             auth.login(request, new_user)
#             return redirect('index')      
#     return render(request, 'signup.html')

# 장고 폼 사용하지 않기 위한 user 회원가입 주석
# radio 타입을 가져오기 위해 name 으로 설정된 user_level 을 사용할거임
# user = get_object_or_404(User, pk=user_id)
# selected_user_level = user.user_level_set.get(pk=request.POST['user_level'])