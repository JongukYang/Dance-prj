from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# 유저 프로필 모델 -> 장고의 User 모델과 1:1 관계를 통해 접근
class userProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # 생년월일, 춤 실력, 전화번호, 등
    # birth = models.CharField(max_length=200)
    
    def __str__(self):
        return self.user
