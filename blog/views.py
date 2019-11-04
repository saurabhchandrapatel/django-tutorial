from django.shortcuts import render
from django.http import  HttpResponse
# Create your views here.
from .models import Post

def view_post(request):
    posts = Post.objects.all() 
    context = {'posts': posts}
    return render(request, 'frontend/post.html', context)
 