from django import forms
from .models import Class, Review

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        # fields = '__all__'
        fields = ['title', 'body', 'photo', 'video', 'genreName']

    def __init__(self, *args, **kwargs):
        super(ClassForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs = {
            'class': 'form-control', 
            'placeholder': "클래스 이름 입력",
            'rows':20
        }

        self.fields['body'].widget.attrs = {
            'class': 'form-control', 
            'placeholder': "클래스 설명 입력",
            'rows':20,
            'cols':100
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review']

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        self.fields['review'].widget.attrs = {
            'class': 'form-control', 
            'placeholder': "후기 입력",
            'rows':10
        }