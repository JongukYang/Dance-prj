from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, CommentForm
from .models import Post, Comment
# from django.contrib.auth.models import User
from accounts.models import userProfile

# 페이지네이션, 객체들 목록을 끊어서 보여주는 것
# from django.core.paginator import Paginator

# Create your views here.
def index(request):
    posts = Post.objects.filter().order_by('-updateDate')
    # posts = Post.objects.order_by('-date')
    comment_form = CommentForm()
    context = {
        'posts':posts,
        'comment_form':comment_form
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

# 게시글 삭제
def delete_post(request, post_id):
    del_post = get_object_or_404(Post, pk=post_id)
    del_post.delete()
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

# def delete_post(request, post_id, user_id):
#     if request.user.is_authenticated:
#         del_post = get_object_or_404(Post, pk=post_id)
#         if request.user == del_post.userId:
#             del_post.delete()
#     return redirect('index')    

# 댓글 저장
def new_comment(request, post_id):
    filled_form = CommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.userId = request.user
        finished_form.post = get_object_or_404(Post, pk=post_id)
        print("comment:", request.body)
        print("post_id :", post_id)
        finished_form.save()
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

def showpostall(request):
    posts = Post.objects.filter().order_by('-updateDate')
    comment_form = CommentForm()
    context = {
        'posts':posts,
        'comment_form':comment_form
    }
    return render(request, 'show_post_all.html', context)

def post_detail(request, userId_id):
    posts = Post.objects.filter(userId=userId_id).order_by('-uploadDate')
    user = get_object_or_404(userProfile, pk=userId_id)
    # username = Post.objects.
    comment_form = CommentForm()
    context = {
        'posts':posts,
        'comment_form':comment_form,
        'user':user,
    }
    return render(request, 'post_detail.html', context)

def likes(request, post_id):
    if request.user.is_authenticated:    
        post = get_object_or_404(Post, pk=post_id)
        # user = request.user
        # check_like_post = 
        if request.user in post.likes_user.all():
        # if post.likes_user.filter(pk=request.user.pk).exists():
            post.likes_user.remove(request.user)
            post.likes_count -= 1
            post.save()    
            # return redirect('index')
        else:
            post.likes_user.add(request.user)
            post.likes_count += 1
            post.save()
        # return redirect('index')
    # 현재 내가 있는 페이지로 redirect 
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))     


# 게시글 수정
def modify_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == "POST" or request.method == 'FILES':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form = PostForm(instance=Post)    
            post.title = request.POST['title']
            post.body = request.POST['body']
            post.save()
            print("danceapp/views/modify_post :")
            return redirect('index')
    else:
        form = PostForm()
        context = {
            'form':form,
            'writing':True,
            'now':'edit',
        }
        return render(request, 'modify_post.html', context)