from django import forms
from .models import Post, Comment
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content','draft','tags','image']
        widgets = {
            'content': SummernoteWidget(),
            'bar': SummernoteInplaceWidget(),
        }
        # exclude = ('author','Created date',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_content']