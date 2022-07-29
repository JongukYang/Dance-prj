from django.db import models
# from django.contrib.auth.models import User
# Create your models here.
# 유저 프로필 모델 -> 장고의 User 모델과 1:1 관계를 통해 접근
# from django.contrib.auth.models import User


from django.contrib.auth.models import AbstractUser

class userProfile(AbstractUser):
    nickname = models.CharField(max_length=50, null=True, blank=True) # 실제 이름
    danceSkill = models.CharField(max_length=10 ,null=True, blank=True) # 상 중 하
    phoneNum = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10 ,null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username


# return HttpResponse('사용자명이 이미 존재합니다.')
