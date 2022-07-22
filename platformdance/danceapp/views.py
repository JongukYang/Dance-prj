from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, CommentForm
from .models import Post, Comment

# 페이지네이션, 객체들 목록을 끊어서 보여주는 것
# from django.core.paginator import Paginator

# Create your views here.
def index(request):
    posts = Post.objects.filter().order_by('-updateDate')
    # posts = Post.objects.order_by('-date')
    context = {
        'posts':posts
    }
    return render(request, 'index.html', context)

def postcreate(request):
    # request 메소드가 Post 일 경우
    # 입력값 저장
    if request.method == 'POST' or request.method == 'FILES':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            unfinished = form.save(commit=False)
            unfinished.userId = request.user
            unfinished.save()
            print("danceapp/views/postcreate :", unfinished)
            return redirect('index')
    # request method()가 Get일 경우
    # form 입력 html 띄우기
    else:
        form = PostForm()
    
    context = {
        'form':form
    }
    return render(request, 'postcreate.html', context)

def delete_post(request, post_id):
    del_post = get_object_or_404(Post, pk=post_id)
    del_post.delete()
    return redirect('index')