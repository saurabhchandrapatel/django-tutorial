from django.contrib import admin
from .models import Post,Category
# Register your models here.
from django.utils.html import format_html
from django.urls import path
from django.shortcuts import render
from django.conf.urls import url
from guardian.admin import GuardedModelAdmin


class CategoryAdmin(GuardedModelAdmin):
    list_display = ('name',)
    list_per_page = 10
    list_max_show_all = 50


class PostAdmin(GuardedModelAdmin):
    list_display = ('title', "category","added_by","action_btn")
    search_fields = ('title',"category__name")
    actions = None
    list_display_links  = ("category","added_by")
    #list_filter = ('category',)
    change_list_template = "admin/posts/list.html"
    add_form_template = "admin/posts/add.html"
    #change_form_template = "admin/posts/edit.html"
    list_per_page = 10
    list_max_show_all = 50

    def action_btn(self,obj): 
    	html = "<a class='btn btn-default' href='/admin/blog/post/"+str(obj.id)+"/change/'>Edit</a>"
    	html += "<a class='btn btn-default' href='/admin/blog/post/"+str(obj.id)+"/delete/'>Delete</a>"

    	return format_html(html)
    action_btn.short_description = "Action"

    
    def get_view_data(self,request,object_id):
        try:
            object_id = 4
            data = Post.objects.get(id=object_id)
            return render("admin/blog/view.html", data)
        except:
            return render("admin/blog/nodata.html")
            
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
