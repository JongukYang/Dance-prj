from django import forms

from .models import Course, Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['title', 'body', 'photo', 'video', 'genreName']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs = {
            'class': 'input-title', 
            'placeholder': "제목 입력(4-100)",
            # 'id':'title',
        }
        self.fields['body'].widget.attrs = {
            'class': 'input-intro', 
            'placeholder': "내용 작성",
            # 'id': 'content',
            'rows':5,
            'cols':20,
        }
        self.fields['photo'].widget.attrs = {
            # 'class': 'form-control', 
            'placeholder': "사진 선택",
            'id': 'imagefile',
            # 'style': 'color:black;' # 알아서 색 맞춰 수정하기
        }
        self.fields['video'].widget.attrs = {
            # 'class': 'form-control', 
            'placeholder': "비디오 선택",
            'id': 'videofile',
            # 'style':"color:black;"
        }
        self.fields['genreName'].widget.attrs = {
            'class': 'form-control', 
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
            'rows':1
        }


# 강의
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        # fields = '__all__'
        # fields = ['title', 'body', 'photo', 'video', 'genreName', 'startDate', 'maxRegCount', 'location']
        fields = ['title', 'body', 'photo', 'genreName', 'startDate', 'location']

        widgets = {
            'startDate': forms.DateInput(format=('%Y/%m/%d'), 
            attrs={'class':'form-control', 'placeholder':'날짜 선택', 'type':'date'}
            ),
        }
    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)

        self.fields['startDate'].widget.attrs = {
            'class': 'form-control', 
            'Date' : forms.DateInput(format=("%d/%m/%Y"))
        }
        self.fields['title'].widget.attrs = {
            'class': 'form-control', 
            #'placeholder': "제목 입력(4-100)",
            
        }
        self.fields['body'].widget.attrs = {
            'class': 'form-control', 
            #'placeholder': "내용 작성",
            'id': 'content',
            'rows':15,
        }
        self.fields['photo'].widget.attrs = {
            'class': 'form-control', 
            'placeholder': "사진 선택",
            'id': 'id_photo',
            'onchange' : 'loadFile(this)',
            'style': 'color:white;' # 알아서 색 맞춰 수정하기
        }
        self.fields['genreName'].widget.attrs = {
            'class': 'form-control', 
            'placeholder': "장르 선택",
            'id': 'id_genreName',
            # 'style': 'color:black;' # 알아서 색 맞춰 수정하기
        }
        self.fields['location'].widget.attrs = {
            'class': 'form-control', 
            'placeholder': "위치 입력",
            'id': 'id_location',
            # 'style': 'color:black;' # 알아서 색 맞춰 수정하기
        }
        # self.fields['maxRegCount'].widget.attrs = {
        #     # 'class': 'form-control', 
        #     'placeholder': "최대 수강 인원",
        #     'id': 'id_maxRegCount',
        #     # 'style': 'color:black;' # 알아서 색 맞춰 수정하기
        # }
        
class PostModifyForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'photo', 'video', 'genreName']