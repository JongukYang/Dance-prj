from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class userProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # 생년월일, 춤 실력, 전화번호, 등



