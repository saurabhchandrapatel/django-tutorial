from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
	name = models.CharField(max_length=100,)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "category"
		verbose_name_plural = "Categories"

# Create your models here.
class Post(models.Model):  
    title = models.CharField(max_length=100,)
    body = models.TextField() 
    category = models.ForeignKey(Category, blank=True , null=True, default=None, on_delete=models.CASCADE)
    added_by = models.ForeignKey(User, blank=True , null=True, default=None, on_delete=models.CASCADE)
    no_of_view = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title

class Comment(models.Model):
	comment =  models.TextField() 
	comment_by  = models.ForeignKey(User, blank=True , null=True, default=None, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, blank=True , null=True, default=None, on_delete=models.CASCADE)
	class Meta:
		verbose_name = "Comment"
		verbose_name_plural = "Comments"
