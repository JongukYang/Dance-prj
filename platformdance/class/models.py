from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Genre(models.Model):
    id = models.AutoField(primary_key=True, null=False) # pk 
    name = models.CharField(max_length=20) # 장르 이름

    def __str__(self):
        return self.name

class Class(models.Model):
    # 클래스ID, 회원ID, 장르ID, 제목, 내용, 썸네일, 비디오
    userId = models.ForeignKey(User, on_delete=models.CASCADE) # 회원ID # User 모델의 pk를 가져옴
    title = models.CharField(max_length=200) # 제목
    body = models.TextField() # 클래스 설명
    photo = models.ImageField(blank=True, null=True, upload_to='thumbnail') # 썸네일 # upload_to : static/blog_photo 로 저장해줘
    video = models.FileField(blank=True, null=True, upload_to='video') # 배포시에는 models.FilePathField()사용
    genreName = models.ForeignKey(Genre, null=True, on_delete=models.CASCADE) # 장르

    def __str__(self):
        return self.title

# 후기
class Review(models.Model):
    review = models.TextField(100)
    date = models.DateTimeField(auto_now_add=True)
    clazz = models.ForeignKey(Class, null=True, blank=True, on_delete=models.CASCADE)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.review