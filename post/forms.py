from django import forms
from .models import Post, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class  PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','contents')
        labels ={
            'title' : '제목',
            'contents' : '내용'
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'content']
        labels = {
            'author': '이름',
            'content': '내용'
        }


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254, help_text='<br>Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        labels = {
            'username': 'ID'
        }
