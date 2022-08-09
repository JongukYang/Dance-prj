from cProfile import label
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
    hits = models.PositiveIntegerField(default=0) # 조회수

    def __str__(self):
        return self.title

# class LikePost(models.Model):
#     user = models.ForeignKey(userProfile, on_delete=models.CASCADE, related_name="liked_users")
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="liked_posts")

#     def __str__(self):
#         return f"{self.user} liked {self.post}"


# 강좌 클래스 모델 만들기
class Course(models.Model):
    # pk=course_id 로 두기
    userId = models.ForeignKey(userProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200) # 제목
    body = models.TextField() # 게시물 설명
    uploadDate = models.DateTimeField(auto_now_add=True) # 처음 업로드 시간
    updateDate = models.DateTimeField(auto_now=True) # 수정 시간
    photo = models.ImageField(blank=True, null=True, upload_to='thumbnail') # 썸네일 # upload_to : static/blog_photo 로 저장해줘
    video = models.FileField(blank=True, null=True, upload_to='video') # 배포시에는 models.FilePathField()사용
    genreName = models.ForeignKey(Genre, null=True, on_delete=models.CASCADE) # 장르
    likes_user = models.ManyToManyField(userProfile, related_name='course_likes', blank=True) # 좋아요 누른 사람
    likes_count = models.PositiveIntegerField(default=0) 
    register_user = models.ManyToManyField(userProfile, related_name='register_user', blank=True)
    register_count = models.PositiveIntegerField(default=0) 
    # 최대 인원 수, 위치, 클래스 날짜 및 시간, 끝나는 시간
    maxRegCount = models.IntegerField(default=0, null=False) 
    startDate = models.DateField(auto_now=False, auto_now_add=False)
    # 강좌 위치
    location = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.title

# 댓글 모델
class Comment(models.Model):
    # comment_id 는 pk로서 존재함
    userId = models.ForeignKey(userProfile, on_delete=models.CASCADE)
    comment = models.TextField('', max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.comment

