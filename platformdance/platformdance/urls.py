"""platformdance URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from danceapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # 관리자 페이지는 배포시에 삭제
    path('admin/', admin.site.urls),
    # 계정 관련 url은 accounts/urls.py 에서 처리
    path('accounts/', include('accounts.urls')),
    
    # 메인 홈페이지
    path('', views.index, name='index'),
    # about us
    path('aboutus/', views.aboutus, name='aboutus'),

    # 마이페이지
    path('mypage/<int:user_id>', views.mypage, name='mypage'),
    # user 프로필 이미지 수정
    path('modifyprofileimg/<int:user_id>', views.modifyprofileimg, name='modifyprofileimg'),
    # 게시글 생성 (영상 업로드)
    path('postcreate/', views.postcreate, name='postcreate'),
    # 게시글 생성 (클래스 업로드)
    path('coursecreate/', views.coursecreate, name='coursecreate'),
    
    # 게시글 세부 페이지 보기
    path('post_detail/<int:post_id>', views.post_datail, name='post_detail'),
    # user 에 따른 개인 포스트 보기
    path('user_post_detail/<int:userId_id>', views.user_post_detail, name='user_post_detail'),
    # 게시글 삭제
    path('delete_post/<int:post_id>', views.delete_post, name='delete_post'),
    # 클래스 삭제
    
    # 댓글 달기
    path('new_comment/<int:post_id>', views.new_comment, name='new_comment'),
    # 댓글 삭제
    path('delete_comment/<int:comment_id>', views.delete_comment, name='delete_comment'),

    # 영상 / 클래스 좋아요
    path('likes/<int:post_id>', views.likes, name='likes'), # 게시글(영상)
    path('course_likes/<int:course_id>', views.course_likes, name='course_likes'), # 클래스
    
    # 게시글 수정
    path('modify_post/<int:post_id>', views.modify_post, name='modify_post'),

    # 클래스 전체 보기
    path('course', views.course, name='course'),

    # 장르별 영상 포스트 보기 / # 장르별 클래스 보기
    path('genre_post', views.genre_post, name='genre_post'),
    path('genre_course', views.genre_course, name='genre_course'),

    # 클래스 세부 페이지
    path('course_detail/<int:course_id>', views.course_detail, name='course_detail'),
    
    # 클래스 신청
    path('regCourse/<int:course_id>', views.regCourse, name='regCourse'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
