from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment


class PostCustmise(SummernoteModelAdmin):
    summernote_fields = '__all__'
    list_display = ['title','draft','author']
    list_filter = ['draft','author']
    search_fields = ['title']

class CommentCustmise(admin.ModelAdmin):
    list_display = ['post','user']

admin.site.register(Post,PostCustmise)
admin.site.register(Comment,CommentCustmise)