from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import *

# Create your views here.

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	now = timezone.now()
	#posts = Post.objects.all()
	return render(request, 'blog/post_list.html', {'posts': posts, 'now': now})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	now = timezone.now()
	return render(request, 'blog/post_detail.html', {'post': post, 'now': now})
