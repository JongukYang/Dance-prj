from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClassForm, ReviewForm
from .models import Class, Review
from django.contrib.auth.models import User

# Create your views here.
def classapp(request):
    return render(request, 'class.html')

def class_list(request):
    return render(request, 'class_list.html')

def class_write(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = ClassForm(request.POST, request.FILES)
        if form.is_valid():
            unfinished = form.save(commit=False)
            unfinished.userId = request.user
            unfinished.save()
            print("danceapp/views/class_write :", unfinished)
            return redirect('index')
    # request method()가 Get일 경우
    # form 입력 html 띄우기
    else:
        form = ClassForm()
    
    context = {
        'form':form
    }
    return render(request, 'class_write.html')

def delete_post(request, post_id):
    del_post = get_object_or_404(Class, pk=post_id)
    del_post.delete()
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
