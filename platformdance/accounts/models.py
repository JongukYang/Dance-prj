from atexit import register
from django.db import models
# from django.contrib.auth.models import User
# 유저 프로필 모델 -> 장고의 User 모델과 1:1 관계를 통해 접근
from django.contrib.auth.models import AbstractUser

class userProfile(AbstractUser):
    nickname = models.CharField(max_length=50, null=True, blank=True) # 실제 이름
    danceSkill = models.CharField(max_length=10 ,null=True, blank=True) # 상 중 하
    phoneNum = models.IntegerField(null=True, blank=True) # 핸드폰 번호
    gender = models.CharField(max_length=10 ,null=True, blank=True) # 성별
    createdAt = models.DateTimeField(auto_now_add=True) # 생성 일자
    birth = models.DateField(null=True, blank=True) # 생년월일
    profilephoto = models.ImageField(blank=True, null=True, upload_to='profilephoto') # 프사
    # 이메일 넣을까 말까

    def __str__(self):
        return self.username


# return HttpResponse('사용자명이 이미 존재합니다.')
