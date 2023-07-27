from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

def post_list(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request,'post_list.html',context)


def post_details(request,id):
    post = Post.objects.get(id=id)
    context = {'post':post}
    return render(request,'post_details.html',context)

def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit= False)
            form.author = request.user
            form.save()
            return redirect('/blogpost/')

    else:
        form = PostForm()

    context = {'form':form}
    return render(request,'new_post.html',context)

def adit_Post(request, id):
    post = Post.objects.get(id = id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()
            return redirect('/blogpost/')

    else:
        form = PostForm(instance = post)

    context = {'form':form}
    return render(request, 'edit_post.html',context)

def delete_post(request, id):
    post = Post.objects.get(id =id)
    post.delete()
    return redirect('/blogpost/')