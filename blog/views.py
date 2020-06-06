from django.shortcuts import render
from django.http import  HttpResponse
# Create your views here.
from .models import Post
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView , CreateView , UpdateView, DeleteView

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


def view_post(request):
    posts = Post.objects.all() 
    context = {'posts': posts}
    return render(request, 'frontend/post.html', context)
 

class ProtectedPostsView(TemplateView):
	template_name = 'frontend/secret-posts.html'

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)


class PostList(ListView):
	model = Post
	template_name = 'frontend/posts.html'
	context_object_name = 'posts'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title']  = 'All Post Data'
		return context


class  PostDetail(DetailView):

	queryset  = Post.objects.all();
	context_object_name = 'post'
	template_name = 'frontend/post-details.html'





