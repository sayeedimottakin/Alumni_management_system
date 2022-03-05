from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from alumni_profile.models import Alumni_Profile
from .forms import PostForm,CommentForm,UpdatePostForm
from .models import Post,Comment
from django.core.paginator import Paginator
import math
# Create your views here.
@login_required
def welcome_view(request):
    profile = []
    try:
        profile = Alumni_Profile.objects.get(user=request.user)   
    except:
        pass
    if not profile or profile.is_verified == False:
        return redirect('home') 
    context={}
    return render(request,"social_media/welcome_view.html",context)

@login_required
def social_media_view(request):
    profile = []
    try:
        profile = Alumni_Profile.objects.get(user=request.user)   
    except:
        pass
    if not profile or profile.is_verified == False:
        return redirect('home') 
    disciplines= list(set(Alumni_Profile.objects.values_list('discipline',flat=True).filter(is_verified=True)))
    disciplines.sort()
    disciplines.insert(0,'All')
    
    batch = list(set(Alumni_Profile.objects.values_list('batch',flat=True).filter(is_verified=True)))
    batch.sort()
    batch.insert(0,'All')

    # print(request.user.alumni)
    post1 = Post.objects.get(body='jkhsadjkfag')
    # temp = Comment.objects.get(post=post1)
    # print(post1.comment_set.all())
    form = PostForm()
    cmt_form = CommentForm()
    post_list = Post.objects.all()
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = Post(
                body=form.cleaned_data["body"],
                tag=form.cleaned_data["tag"],
                author=request.user.alumni,
                image = form.cleaned_data["image"],
                files = form.cleaned_data["files"],
            )
            post.save()
        elif request.POST['manage_post'] == '1':
            post_list = Post.objects.all().order_by('-created_on')
        else:
            pass


        paginator = Paginator(post_list,5)
        page_number = request.GET.get('page')
        posts = paginator.get_page(page_number)

        context={
            'disciplines':disciplines,
            'batch':batch,
            'post_form':form,
            'posts':posts,
            'anchor':'post_list',
            'cmt_form':cmt_form,
        }
        return render(request,"social_media/social_media_view.html",context)

    paginator = Paginator(post_list,5)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    
    context={
        'disciplines':disciplines,
        'batch':batch,
        'post_form':form,
        'posts':posts,
        'cmt_form':cmt_form,
    }
    return render(request,"social_media/social_media_view.html",context)

def post_details(request,id):
    post = Post.objects.get(id=id)
    cmt_form = CommentForm()
    update_post = UpdatePostForm(request.POST or None, instance=post)
    if request.method == 'POST':
        if update_post.is_valid():
            post.save()
        return redirect('post_details',id=post.id)
    context = {
        'post':post,
        'cmt_form':cmt_form,
        'update_post':update_post,
    }
    return render(request,"social_media/post_details.html",context)


def add_comment(request,id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST,request.FILES)
        if form.is_valid():
            comment = Comment(
                author=request.user.alumni,
                body=form.cleaned_data['body'],
                post=post,
            )
            comment.save()
        return redirect('post_details',id=post.id)


def delete_post(request,id):
    # print('yoo')
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('social_media_view')


def edit_comment(request,id):
    comment = Comment.objects.get(id=id)
    post_id = comment.post.id
    new_body = request.POST['comment']
    comment.body = new_body
    comment.save()
    return redirect('post_details',id=post_id)


def delete_comment(request,id):
    # print('yoo')
    comment = Comment.objects.get(id=id)
    post_id = comment.post.id
    comment.delete()
    return redirect('post_details',id=post_id)
