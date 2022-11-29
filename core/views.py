from distutils.command.build_scripts import first_line_re
from email import message
import email
from multiprocessing import context
from turtle import title
from django.shortcuts import redirect, render
from django.contrib import messages

from core.forms import CommentForm, NewsletterForm,SubscribersForm
from .models import Newsletter, Post, Subscribers,Video,Category
from django.shortcuts import render,get_object_or_404, HttpResponseRedirect
from django.views.generic import ListView
from django.core.mail import send_mail
from django_pandas.io import read_frame
from django.db.models import Q
from django.core.paginator import Paginator


def about(request):
    return render(request, 'core/about.html')


def contact(request):
    return render(request, 'core/contact.html')



def index(request,category_slug=None):
    if request.method == 'POST':
        form = SubscribersForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'subscription successful')
            return redirect ('index')
    else:
        form = SubscribersForm()
    search_post = request.GET.get('search')
    if search_post:
        posts = Post.objects.filter(Q(title__icontains=search_post)| Q(content__icontains=search_post))
    else:
        posts = Post.objects.all()
        videos = Video.objects.all()
        recent_posts = Post.objects.order_by('-date')[:5]
        # pagination for posts
        p = Paginator( Post.objects.all(), 8)
        page =request.GET.get('page')
        page_number = p.get_page(page)
       
        
        paginator = Paginator(Video.objects.all(), 6)
        page = request.GET.get('page')
        chapters = paginator.get_page(page)
       
    context = {
        'posts':posts,
        'page_number':page_number,
        'vidoes':videos,
        'chapters':chapters,
        'recent_posts':recent_posts,
        'form' : form,
       
        
    }
    return render(request, 'core/index.html', context)


def detail_page(request,post):
    post = get_object_or_404(Post,slug=post)
    comments = post.comments.filter(status=True)
    user_commnent = None
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            user_commnent = comment_form.save(commit=False)
            user_commnent.post = post
            user_commnent.save()
            return HttpResponseRedirect('/' + post.slug)
    else:
        comment_form = CommentForm()
    return render(request, 'core/post_detail.html', {'post': post, 'comments':  user_commnent, 'comments': comments, 'comment_form': comment_form})


class CatListView(ListView):
    template_name = 'category.html'
    context_object_name = 'catlist'

    def get_queryset(self):
        content = {
            'cat': self.kwargs['category'],
            'posts': Post.objects.filter(category__name=self.kwargs['category'])
        }
        return content


def category_list(request):
    category_list = Category.objects.exclude(name='default')
    context = {
        "category_list": category_list,
    }
    return context


def letters(request):
    emails = Subscribers.objects.all()
    df = read_frame(emails, fieldnames=['email'])
    mail_list = df['email'].values.tolist()
    print(mail_list)
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            title = form.cleaned_data.get('title')
            message = form.cleaned_data.get('message')
            send_mail(
        title,
        message,
        '',
        mail_list,
        fail_silently=True,
    )

            messages.success(request, 'message sent successfuly')
            return redirect('index')
            
    else:
        form = NewsletterForm()

    context = {
        'form':form,
    }
    return render(request, 'core/newsletter.html', context)




        







 
   
        
  
    
