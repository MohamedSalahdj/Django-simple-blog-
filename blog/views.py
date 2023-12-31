from django.shortcuts import render, redirect
from .models import Post,Comment
from .forms import PostForm, CommentForm
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView

# def post_list(request): # QUERY , TEMPLATE , CONTEXT  
#     posts = Post.objects.all()
#     context = {'posts': posts}
#     return render(request,'post_list.html',context)

class PostList(ListView):
    model = Post  # template ==> model_list && context ==> model_List , object_list   
    

def post_details(request,pk):
    post = Post.objects.get(id=pk)
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form = comment_form.save(commit=False)
            comment_form.user = request.user
            comment_form.post = post
            comment_form.save()
    else:
        comment_form = CommentForm()
    comments = Comment.objects.filter(post= post)
    context = {'post':post,'form':comment_form,'comments':comments}
    return render(request,'blog/post_detail.html',context)


"""
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit= False) # save in memory and need it to add other fields before saving all data in db
            form.author = request.user
            form.save() # this save in DB
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

