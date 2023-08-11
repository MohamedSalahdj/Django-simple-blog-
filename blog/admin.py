from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment


class PostCustmise(SummernoteModelAdmin):
    summernote_fields = '__all__'


admin.site.register(Post,PostCustmise)
admin.site.register(Comment)