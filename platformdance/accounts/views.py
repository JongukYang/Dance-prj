from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth.login(request, form.get_user())
            return redirect('index')
    else:
        form = AuthenticationForm()

    context = {
        'form':form,
    }
    return render(request, 'login.html', context)

def logout(request):
    auth.logout(request)
    return redirect('index')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    
    context = {
        'form':form,
    }
    return render(request, 'signup.html', context)