from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from blog.views import view_post,ProtectedPostsView,PostList,PostDetail,otp_login,verify_otp
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls), 
    url(r"^$",  TemplateView.as_view(template_name='frontend/home.html')), 
    path('blog/', view_post), 
    path('blog/posts/', TemplateView.as_view(template_name='frontend/posts.html') ),
    path('blog/secret-posts/', ProtectedPostsView.as_view()),  
    path('blog/listview-posts/', PostList.as_view()), 
    path('blog/details-posts/<int:pk>/', PostDetail.as_view()), 

    path('login',otp_login), 
    path('verify-otp',verify_otp), 


]
