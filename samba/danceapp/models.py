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
    # 사진을 추가하고싶어
    photo = models.ImageField(blank=True, null=True, upload_to='blog_photo') # upload_to : static/blog_photo 로 저장해줘
    # upload = 

    def __str__(self):
        return self.title

# 댓글 모델
class Comment(models.Model):
    comment = models.TextField(200)
    date = models.DateTimeField(auto_now_add=True)
    # 댓을이 어떤 게시물에 달려있는 댓글인지 확인할 수 있는 변수 필요 
    # 따라서 위의 Blog 객체를 참조해야 하는데 이것을 외래키 라고함(foreign key)
    # 코멘트는 블로그의 종속된 것이기 때문에 블로그 포스트가 삭제된다면 같이 삭제한다. 
    # 그것이 on_delete=models.CASCADE
    ## 게시물에 종속적인게 댓글이기 때문에 Foreignkey 로 작성해야함
    ## 먼저 어떤 게시물인지 찾기
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment