from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

# Create your views here.

def post_list(request):
    #return render(request, 'blogs/post_list.html', {})
    posts = Post.objects.all().order_by('published_date')
    from pprint import pprint
    pprint(posts)
    return render(request, 'blogs/post_list.html',{'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blogs/post_detail.html', {'post': post})
