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


from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class OTPBackend(ModelBackend):
	def authentication(self, request , username=None ):
		user_model = get_user_model()
		try:
			user = user_model.objects.get(username=username)
			return user
		except:
			return None

	def get_user(self, user_id): 
		user_model = get_user_model()
		try:
			return user_model.objects.get(pk=user_id)
		except:
			return None



def otp_login(request):

	import random
	from django.core.mail import send_mail
	
	if request.method == 'POST':
		email = request.POST.get('email')
		otp =  random.randrange(1000,9999)
		send_mail('Unboxing Login OTP ', 'otp is '+str(otp),  'vsaurabh.aec@gmail.com',  [email], fail_silently=True)	
		request.session['otp'] = otp
		request.session['email'] = email
		return  render(request, 'frontend/otp.html', {})
	else:
		return render(request, 'frontend/otp_login.html', {})



def verify_otp(request):

	from django.contrib.auth.models import User
	from django.contrib.auth import login
	from django.shortcuts import redirect 

	if request.method == 'POST':
		otp = request.POST.get('otp')
		email = request.session['email']
		saved_opt= request.session['otp']
		if otp == str(saved_opt):
			user = User.objects.filter(email=email).first()
			if user  is not None:
				login(request, user, backend='blog.views.OTPBackend')
				return redirect ("/admin")
			 
	return redirect("/login")  

 
