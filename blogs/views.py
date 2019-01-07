from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.

def post_list(request):
    #return render(request, 'blogs/post_list.html', {})
    posts = Post.objects.filter(published_date= timezone.now()).order_by('published_date')
    return render(request, 'blogs/post_list.html',{'posts': posts})
