from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.
# 유저 프로필 모델 -> 장고의 User 모델과 1:1 관계를 통해 접근
class userProfile(AbstractUser):
    nickname = models.CharField(max_length=50, null=True, blank=True)
    danceSkill = models.CharField(max_length=10 ,null=True, blank=True)
    phoneNum = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10 ,null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    birth = models.DateField(null=True, blank=True)
    # 생년월일, 춤 실력, 전화번호, 등
    # birth = models.DateField()

    def __str__(self):
        return self.username


# return HttpResponse('사용자명이 이미 존재합니다.')
