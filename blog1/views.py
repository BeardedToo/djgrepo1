from django.shortcuts import render
from django.utils import timezone
from blog1.models import Post # TODO: wildcard this, both app and model

# Create your views here.

def post_list(request):
	#posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	posts = Post.objects.all()
	return render(request, 'blog/post_list.html', {})

