from atexit import register
from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaulttags import comment
from .forms import PostForm, CommentForm, CourseForm, PostModifyForm
from .models import Post, Comment, Genre, Course
from accounts.models import userProfile
from django.core.paginator import Paginator

# 페이지네이션, 객체들 목록을 끊어서 보여주는 것
# from django.core.paginator import Paginator

def index(request):
    # paginator는 삭제 예정
    # 업로드된 영상 게시글
    posts = Post.objects.all().order_by('-uploadDate')
    paginator = Paginator(posts, 8)
    pagenum = request.GET.get('page') # url 부분 ex) @@@?page=1 -> {page:1}
    posts = paginator.get_page(pagenum)
    
    # 업로드된 클래스 게시글
    courses = Course.objects.all().order_by('-uploadDate')
    paginator = Paginator(courses, 8)
    pagenum = request.GET.get('page') # url 부분 ex) @@@?page=1 -> {page:1}
    courses = paginator.get_page(pagenum)

    # likes_ten = Post.objects.all().order_by('-likes_count')[:5] # 모든 포스트 중 택5 -> 쿼리셋
    likes_top_ten = Post.objects.all().order_by('-likes_count') # 모든 포스트 중 택5 -> 딕셔너리 형태
    likes_top_ten_val = Post.objects.all().order_by('-likes_count').values() # 모든 포스트 중 택5 -> 딕셔너리 형태
    likes_top_ten_val = list(likes_top_ten_val)
    # likes_ten = Post.objects.filter(genreName='1').order_by('-likes_count')[:5] # 장르 중 택5

    comment_form = CommentForm()

    context = {
        'posts':posts,
        'courses':courses,
        'comment_form':comment_form,
        'likes_top_ten':likes_top_ten,
        'likes_top_ten_val':likes_top_ten_val,
        # 'rank1':likes_top_ten[0],
        # 'rank2':likes_top_ten[1],
        # 'rank3':likes_top_ten[2],
        # 'rank4':likes_top_ten[3],
        # 'rank5':likes_top_ten[4],
        # 'rank6':likes_top_ten[5],
        # 'rank7':likes_top_ten[6],
        # 'rank8':likes_top_ten[7],
        # 'rank9':likes_top_ten[8],
        # 'rank10':likes_top_ten[9],
    }
    return render(request, 'index.html', context)

# 클래스 만들기
def coursecreate(request):
    print("클래스 만들기 시작")
    # request 메소드가 Post 일 경우 입력값 저장
    if request.method == 'POST' or request.method == 'FILES':
        print("if문 post 요청 받아옴")
        form = CourseForm(request.POST, request.FILES)
        print("form 가져옴")
        print(request.POST)
        # print(form)
        if form.is_valid():
            print("valid 검사 시작")
            unfinished = form.save(commit=False)
            print("commit false 수행")
            print(unfinished)
            unfinished.userId = request.user
            unfinished.save()
            return redirect('index')
    # request method()가 Get일 경우 form 입력 html 띄우기
    else:
        form = CourseForm()
    
    context = {
        'form':form
    }
    return render(request, 'coursecreate.html', context)

# 게시글 작성
def postcreate(request):
    # request 메소드가 Post 일 경우 입력값 저장
    if request.method == 'POST' or request.method == 'FILES':
        form = PostForm(request.POST, request.FILES)
        print(request.POST)
        print(form)
        if form.is_valid():
            unfinished = form.save(commit=False)
            unfinished.userId = request.user
            unfinished.save()
            return redirect('index')
    # request method()가 Get일 경우 form 입력 html 띄우기
    else:
        form = PostForm()
    
    context = {
        'form':form
    }
    return render(request, 'postcreate.html', context)

# 게시글 수정
def modify_post(request, post_id):
    if request.method =='POST' or request.method == 'FILES':
        post = get_object_or_404(Post, pk=post_id)
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            # post = form.save(commit=False)
            # form = PostForm(Post,instance=post)
            # post.title = request.POST['title']
            # post.body = request.POST['body']
            # post.title = form.cleaned_data['title'] # +
            # post.body = form.cleaned_data['body'] # +            
            # post.save()
            form.save()
            return redirect('index')
    # else:
    #     form = PostModifyForm(instance = post)
    return render(request, 'modify_post.html', {'form':form})

# 수정 2 테스트 해보기
# def update(request, article_pk):
#     edit_title = request.POST.get('edit_title')
#     edit_content = request.POST.get('edit_content')
#     article = Article.objects.get(pk=article_pk)
#     article.title = edit_title
#     article.content = edit_content
#     article.save()
#     return redirect('articles:detail', article_pk)

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
#     return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

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

# 개인 유저 프로필 보기
def user_post_detail(request, userId_id):
    posts = Post.objects.filter(userId=userId_id).order_by('-uploadDate')
    user = get_object_or_404(userProfile, pk=userId_id)
    # username = Post.objects.
    comment_form = CommentForm()
    context = {
        'posts':posts,
        'comment_form':comment_form,
        'user':user,
    }
    return render(request, 'user_post_detail.html', context)

# 게시글 좋아요
def likes(request, post_id):
    if request.user.is_authenticated:    
        post = get_object_or_404(Post, pk=post_id)
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
def post_datail(request, post_id):
    post = Post.objects.get(id = post_id)
    post.hits += 1
    post.save()
    comment_form = CommentForm()
    context = {
        'post':post,
        'comment_form':comment_form,
    }
    return render(request, 'post_detail.html', context)

# 장르 페이지
def genre_post(request):
    genre_id = request.GET.get('genre_id', None)
    genre = Genre.objects.get(id=int(genre_id))
    posts = Post.objects.filter().order_by('-uploadDate')
    likes_top = Post.objects.filter(genreName=int(genre_id)).order_by('-likes_count')
    comment_form = CommentForm()
    context = {
        'genre':genre,
        'posts':posts,
        'comment_form':comment_form,
        'likes_top':likes_top,
        # 장르별 게시글이 10개가 안 넘어서 오류 뜸
        # 'rank1':likes_top[0],
        # 'rank2':likes_top[1],
        # 'rank3':likes_top[2],
        # 'rank4':likes_top[3],
        # 'rank5':likes_top[4],
        # 'rank6':likes_top[5],
        # 'rank7':likes_top[6],
        # 'rank8':likes_top[7],
        # 'rank9':likes_top[8],
        # 'rank10':likes_top[9],
    }
    return render(request, 'genre_post.html', context)

# 장르에 맞는 클레스 출력
def genre_course(request):
    genre_id = request.GET.get('genre_id', None)
    genre = Genre.objects.get(id=int(genre_id))
    courses = Course.objects.filter(genreName=genre).order_by('-uploadDate')
    likes_top_ten = Course.objects.all().order_by('-likes_count') # 모든 포스트 중 택5 -> 딕셔너리 형태
    comment_form = CommentForm()
    context = {
        'genre':genre,
        'courses':courses,
        'comment_form':comment_form,
        'likes_top_ten':likes_top_ten,
    }
    return render(request, 'genre_course.html', context)

# 클래스 좋아요
def course_likes(request, course_id):
   if request.user.is_authenticated:    
       course = get_object_or_404(Course, pk=course_id)
       if request.user in course.likes_user.all():
       # if post.likes_user.filter(pk=request.user.pk).exists():
           course.likes_user.remove(request.user)
           course.likes_count -= 1
           course.save()    
       else:
           course.likes_user.add(request.user)
           course.likes_count += 1
           course.save()
   # 현재 내가 있는 페이지로 redirect 
   return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

# 클래스 상세보기
def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    context = {
        'course': course,
    }
    return render(request, 'course_detail.html', context)

# 클래스 신청하기
def regCourse(request, course_id):
   if request.user.is_authenticated:    
       course = get_object_or_404(Course, pk=course_id)
       if request.user in course.register_user.all():
    #    if course.register_user.filter(pk=request.user.pk).exists():
           course.register_user.remove(request.user)
           course.register_count -= 1
           course.save()    
       else:
           course.register_user.add(request.user)
           course.register_count += 1
           course.save()
   # 현재 내가 있는 페이지로 redirect 
   return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

# 마이페이지 정보 전달
def mypage(request, user_id):
    if request.user.is_authenticated:
        myposts = Post.objects.filter(userId=user_id).order_by('-uploadDate')
        myprofile = userProfile.objects.filter(id=user_id)
        mylikedvideo = Post.objects.filter(likes_user=user_id).order_by('-uploadDate')
        myregcourse = Course.objects.filter(register_user=user_id)
        context = {
            'posts':myposts,
            'myprofile':myprofile,
            'mylikedvideo':mylikedvideo,
            'myregcourse':myregcourse,
        }
        return render(request, 'mypage.html', context)

# 마이페이지 프로필 사진 추가
def modifyprofileimg(request, user_id):
    if request.method == 'POST' or request.method == 'FILES':
        user = userProfile.objects.get(id=user_id)
        # 유저 프로필 사진 지우고, 새로운거 저장
        if user.profilephoto:
            user.profilephoto.delete()
            user.profilephoto = request.FILES['profileimg']
        user.save()
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    else:
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

def course(request):
    return render(request, 'course.html')

def aboutus(request):
    return render(request, 'about_us.html')