from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content','draft','tags','image']
        # exclude = ('author','Created date',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_content']