from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

    # 장고의 Form 태그를 이용하여 부트스트랩을 적용하기 위해선 init 생성자를 만들어야함
    def __init__(self, *args, **kwargs):
        # 아래 super(PostForm)은 PostForm의 생성자 라는 뜻
        super(PostForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs = {
            'class': 'form-control',
            'placeholder': '글 제목 입력',
            'rows': 20,
        }

        self.fields['body'].widget.attrs = {
            'class': 'form-control', 
            'placeholder': "글 제목 입력",
            'rows':20,
            'cols':100
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

        self.fields['comment'].widget.attrs = {
            'class': 'form-control', 
            'placeholder': "댓글 입력",
            'rows':10
        }