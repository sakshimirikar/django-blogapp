<<<<<<< HEAD

=======
from turtle import pos
>>>>>>> fdc9cef46373a601c1d6b806f73c6d7fdffb6291
from django.shortcuts import render,get_object_or_404
from .models import Post , Comment
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger

from django.views.generic import ListView
from .forms import EmailPostForm , CommentForm
from django.core.mail import send_mail



#creating class based views

class PostListView(ListView):
    queryset=Post.published.all()
    context_object_name='posts'
    paginate_by=3
    template_name='list.html'




# Create your views here.


def post_list(request):

    object_list=Post.published.all()
    paginator=Paginator(object_list,3)
    page=request.GET.get('page') 

    try:
        posts=paginator.page(page)

    except PageNotAnInteger:
        posts=paginator.page(1)

    except EmptyPage:
        posts=paginator.page(paginator.num_pages)
    return render(request, 'list.html' , {'page':page ,'posts' :posts})

 

def post_detail(request,year,month,day,post):
<<<<<<< HEAD
    post=get_object_or_404(Post,slug=post,status='published', publish__year=year, publish__month=month, publish__day=day)

    #List of active comments for this post
    comments=post.comments.filter(active=True)

    new_comment=None

    if request.method == 'POST':
     #A comment was posted
        comment_form=CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment=comment_form.save(commit=False)

            new_comment.post=post

            new_comment.save()
        else:
            comment_form=CommentForm()

        return render(request, 'detail.html' , {'post':post , 'comments':comments , 'new_comment' : new_comment , 'comment_form':comment_form})
     









    return render(request ,'detail.html' , {'post':post})



#handling forms in views


def post_share(request,post_id):
    #retrive post by id 
    post=get_object_or_404(Post,id=post_id)
    sent=False

    if request.method == 'POST': #if request is GET
        #form was submitted
        form = EmailPostForm(request.POST) #displays the empty form

        if form.is_valid(): # if request is POST data
            #Form fields passed validation.
            cd =form.cleaned_data
             #..send email

            post_url=request.build_absolute_uri(post.get_absolute_url())
            subject= '{} ({}) recommends you reading "{}" '.format(cd['name'] , cd['email'] , post.title  )
            message='Read "{}" at {}\n\n{}\'s comments: {}" ' . format(post.title , post_url,cd['name'],cd['comments'])
            send_mail(subject , message, 'sakshimiri@gmail.com',[cd['to']])

            sent=True

    #if request is GET
    else:
        form=EmailPostForm()
    return render(request,'share.html' , {'post':post , 'form' : form , 'sent':sent })









            
    
=======
    post=get_object_or_404(Post,slug=post ,
    publish__year=year, publish__month=month, publish__day=day)
    return render(request ,'detail.html' , {'post':post})
>>>>>>> fdc9cef46373a601c1d6b806f73c6d7fdffb6291
