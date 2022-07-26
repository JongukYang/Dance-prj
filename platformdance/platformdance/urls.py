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
    # 메인 홈페이지
    path('', views.index, name='index'),
    # 계정 관련 url은 accounts/urls.py 에서 처리
    path('accounts/', include('accounts.urls')),
    # danceapp 파일 업로드
    path('postcreate/', views.postcreate, name='postcreate'),
    # 포스트 전체 보기
    path('showpostall/', views.showpostall, name='showpostall'),
    # user 에 따른 개인 포스트 보기
    path('post_detail/<int:userId_id>', views.post_detail, name='post_detail'),
    # 게시글 삭제
    path('delete_post/<int:post_id>', views.delete_post, name='delete_post'),
    # 댓글
    path('new_comment/<int:post_id>', views.new_comment, name='new_comment'),
    # 좋아요
    path('likes/<int:post_id>', views.likes, name='likes'),
    # 게시글 수정
    path('modify_post/<int:post_id>', views.modify_post, name='modify_post'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)