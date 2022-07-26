from tkinter import CASCADE
from django.db import models
# from django.contrib.auth.models import User
from accounts.models import userProfile

# Create your models here.
# 장르 모델
class Genre(models.Model):
    id = models.AutoField(primary_key=True, null=False) # pk 
    name = models.CharField(max_length=20) # 장르 이름

    def __str__(self):
        return self.name

# user가 작성한 게시글 모델        
class Post(models.Model):
    # 게시글ID, 회원ID, 장르ID, 제목, 내용, 작성시간, 수정시간, 썸네일, 비디오
    # 게시글ID는 primarykey로서 이미 있음
    userId = models.ForeignKey(userProfile, on_delete=models.CASCADE) # 회원ID # User 모델의 pk를 가져옴
    title = models.CharField(max_length=200) # 제목
    body = models.TextField() # 게시물 설명
    uploadDate = models.DateTimeField(auto_now_add=True) # 처음 업로드 시간
    updateDate = models.DateTimeField(auto_now=True) # 수정 시간
    photo = models.ImageField(blank=True, null=True, upload_to='thumbnail') # 썸네일 # upload_to : static/blog_photo 로 저장해줘
    video = models.FileField(blank=True, null=True, upload_to='video') # 배포시에는 models.FilePathField()사용
    genreName = models.ForeignKey(Genre, null=True, on_delete=models.CASCADE) # 장르
    likes_user = models.ManyToManyField(userProfile, related_name='likes', blank=True) # 좋아요 누른 사람
    likes_count = models.PositiveIntegerField(default=0) # 좋아요 개수

    def __str__(self):
        return self.title


# 댓글 모델
class Comment(models.Model):
    # comment_id 는 pk로서 존재함
    userId = models.ForeignKey(userProfile, on_delete=models.CASCADE)
    comment = models.TextField(100)
    date = models.DateTimeField(auto_now_add=True)
    # 댓을이 어떤 게시물에 달려있는 댓글인지 확인할 수 있는 변수 필요 
    # 따라서 위의 Blog 객체를 참조해야 하는데 이것을 외래키 라고함(foreign key)
    # 코멘트는 블로그의 종속된 것이기 때문에 블로그 포스트가 삭제된다면 같이 삭제한다. 
    # 그것이 on_delete=models.CASCADE
    ## 게시물에 종속적인게 댓글이기 때문에 Foreignkey 로 작성해야함
    ## 먼저 어떤 게시물인지 찾기
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.comment


