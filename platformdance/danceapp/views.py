from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, CommentForm, CourseForm
from .models import Post, Comment, Genre, Course
# from django.contrib.auth.models import User
from accounts.models import userProfile

# 페이지네이션, 객체들 목록을 끊어서 보여주는 것
# from django.core.paginator import Paginator

def indexstyle(request):
    return render(request, 'indexstyle.html')

# Create your views here.
def index(request):
    posts = Post.objects.filter().order_by('-updateDate')
    # likes_ten = Post.objects.all().order_by('-likes_count')[:5] # 모든 포스트 중 택5 -> 쿼리셋
    likes_top_ten = Post.objects.all().order_by('-likes_count')[:10] # 모든 포스트 중 택5 -> 딕셔너리 형태
    # likes_ten = Post.objects.filter(genreName='1').order_by('-likes_count')[:5] # 장르 중 택5
    comment_form = CommentForm()
    context = {
        'posts':posts,
        'comment_form':comment_form,
        'likes_top_ten':likes_top_ten,
        'rank1':likes_top_ten[0],
        'rank2':likes_top_ten[1],
        'rank3':likes_top_ten[2],
        'rank4':likes_top_ten[3],
        'rank5':likes_top_ten[4],
        'rank6':likes_top_ten[5],
        'rank7':likes_top_ten[6],
        'rank8':likes_top_ten[7],
        'rank9':likes_top_ten[8],
        'rank10':likes_top_ten[9],
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
            return redirect('index')
    # request method()가 Get일 경우
    # form 입력 html 띄우기
    else:
        form = PostForm()
    
    context = {
        'form':form
    }
    return render(request, 'postcreate.html', context)

# 클래스 만들기
def coursecreate(request):
    # request 메소드가 Post 일 경우
    # 입력값 저장
    if request.method == 'POST' or request.method == 'FILES':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            unfinished = form.save(commit=False)
            unfinished.userId = request.user
            unfinished.save()
            return redirect('index')
    # request method()가 Get일 경우
    # form 입력 html 띄우기
    else:
        form = CourseForm()
    
    context = {
        'form':form
    }
    return render(request, 'date.html', context)

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

# 게시글 수정
def modify_post(request, post_id):
    # post = Post.objects.get(id=post_id)
    if request.method == "POST" or request.method == 'FILES':
        post = get_object_or_404(Post, pk=post_id)
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            # form = PostForm(Post,instance=post)    
            # post.title = request.POST['title']
            # post.body = request.POST['body']
            post.save()
            return redirect('index')
    else:
        form = PostForm(instance=post)
    return render(request, 'modify_post.html', {'form':form})
#     # context = {
#     #     'form':form,
#     #     'writing':True,
#     #     'now':'edit',
#     # }
#     # return render(request, 'modify_post.html', context)



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

# 댓글 삭제
def delete_comment(request, comment_id):
    del_comment = get_object_or_404(Comment, pk=comment_id)
    del_comment.delete()
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

# # 장르를 클릭했을 때 genre.id 를 넘겨받아 각각의 장르마다 따른 필터 적용
# def showpostall(request):
#     posts = Post.objects.filter(genreName=1)
#     # posts = Post.objects.filter().order_by('-uploadDate')
#     comment_form = CommentForm()
#     context = {
#         'posts':posts,
#         'comment_form':comment_form
#     }
#     return render(request, 'show_post_all.html', context)

# user_detail 로 바꾸기
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
        else:
            post.likes_user.add(request.user)
            post.likes_count += 1
            post.save()
    # 현재 내가 있는 페이지로 redirect 
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))     

# 게시글 세부 페이지로 이동
# post_detail로 바꾸기
def post(request, post_id):
    post = Post.objects.get(id = post_id)
    comment_form = CommentForm()
    context = {
        'post':post,
        'comment_form':comment_form,
    }
    return render(request, 'post.html', context)

# 장르 페이지
def genre_post(request):
    genre_id = request.GET.get('genre_id', None)
    genre = Genre.objects.get(id=int(genre_id))
    posts = Post.objects.filter().order_by('-updateDate')
    genrepost = Post.objects.filter(genreName='1').order_by('-uploadDate')
    comment_form = CommentForm()
    context = {
        'genre':genre,
        'posts':posts,
        'comment_form':comment_form,
    }
    return render(request, 'genre_post.html', context)

