from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['title', 'body', 'photo', 'video', 'genreName']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs = {
            'class': 'form-control', 
            'placeholder': "제목 입력(4-100)",
            'id':'title',
        }
        self.fields['body'].widget.attrs = {
            'class': 'form-control', 
            'placeholder': "내용 작성",
            'id': 'content',
            'rows':15,
        }
        self.fields['photo'].widget.attrs = {
            # 'class': 'form-control', 
            'placeholder': "사진 선택",
            'id': 'id_photo',
            'style': 'color:black;' # 알아서 색 맞춰 수정하기
        }
        self.fields['video'].widget.attrs = {
            # 'class': 'form-control', 
            'placeholder': "비디오 선택",
            'id': 'id_video',
            'style':"color:black;"
        }
        self.fields['genreName'].widget.attrs = {
            # 'class': 'form-control', 
            'placeholder': "장르 선택",
            'id': 'id_gerneName',
            'style': 'color:black;' # 알아서 색 맞춰 수정하기
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


