from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView

# def post_list(request): # QUERY , TEMPLATE , CONTEXT  
#     posts = Post.objects.all()
#     context = {'posts': posts}
#     return render(request,'post_list.html',context)

class PostList(ListView):
    model = Post  # template ==> model_list && context ==> model_List , object_list   


# def post_details(request,id):
#     post = Post.objects.get(id=id)
#     context = {'post':post}
#     return render(request,'post_details.html',context)

class Postdetails(DetailView):
    model = Post          # context ==> model-name OR object

"""
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
"""

class CreatePOST(CreateView):
    model = Post
    fields = ['title','content','draft','tags','image','author']
    success_url = '/blogpost/'

"""
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
"""

class UpdatePost(UpdateView):
    model = Post
    fields = ['title','content','draft','tags','image','author']
    success_url = '/blogpost/'
    template_name = "blog/edit_post.html"	

"""
def delete_post(request, id):
    post = Post.objects.get(id =id)
    post.delete()
    return redirect('/blogpost/')
"""

class DeletePost(DeleteView):
    model = Post
    success_url = '/blogpost/'

