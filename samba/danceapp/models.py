from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
# 클래스를 이용해 데이터베이스에 Mapping 하는 것을 ORM(Object Oriented Mapping)
# 게시물 모델
class Post(models.Model):
    title = models.CharField(max_length=200) # 제목
    body = models.TextField() # 게시물 설명
    date = models.DateTimeField(auto_now_add=True) # 업로드 시간
    author = models.ForeignKey(User, on_delete=models.CASCADE) # 작성자
    # upload = 

    def __str__(self):
        return self.title

# 댓글 모델
class Comment(models.Model):
    comment = models.TextField(200)
    date = models.DateTimeField(auto_now_add=True)
    # 게시물에 종속적인게 댓글이기 때문에 Foreignkey 로 작성해야함
    # 먼저 어떤 게시물인지 찾기
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment