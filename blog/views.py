from django.shortcuts import render
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request,'post_list.html',context)