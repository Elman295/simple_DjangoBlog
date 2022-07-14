from django.shortcuts import render, redirect
from . import forms
from . import models
# Create your views here.


def home_page(request):
    posts = models.Post.objects.all()
    context = {
        "posts":posts,
    }
    return render(request,template_name="post/home_page.html",context=context)



def create_post(request):
    if request.method == "POST":
        form = forms.CreateNewPost(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            models.Post.objects.create(author=data.get("author"),title=data.get("title"), description= data.get("description"), body=data.get("body"))
            return redirect(to="post:homepage")
    else:
        form = forms.CreateNewPost()
    context = {
        "form":form,
    }
    return render(request, template_name="post/createnewpost.html",context = context)



def detail_post(request,id):
    post = models.Post.objects.get(id = id)
    context = {
        "post":post,
    }
    return render(request,template_name="post/detailpost.html",context=context)


def delete_post(request,id):
    post = models.Post.objects.get(id = id)
    post.delete()
    return redirect(to="post:homepage")


def update_post(request,id):
    post = models.Post.objects.get(id=id)
    if request.method == "POST":
        form = forms.CreateNewPost(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect(to="post:homepage")
    else:
        form = forms.CreateNewPost(instance=post)
    context = {
        "form":form,
    }
    return render(request,template_name="post/updatepost.html",context=context)



