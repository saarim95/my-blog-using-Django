from django.db import models
from django.utils.html import format_html

# Create your models here.

#category model


class Category(models.Model):
	cat_id=models.AutoField(primary_key=True)
	title=models.CharField(max_length=100)
	description=models.TextField()
	url=models.CharField(max_length=100)
	image=models.ImageField(upload_to='Category/')
	add_date=models.DateTimeField(auto_now_add=True,null=True)

	def image_tag(self):
		return format_html('<img src="/media/{}" style="width:35px;height:35px;border-radius:50%;" />'.format(self.image))
    
	def __str__(self):
		return self.title


#post mode
class Post(models.Model):
	post_id=models.AutoField(primary_key=True)
	title=models.CharField(max_length=200)
	content=models.TextField()
	url=models.CharField(max_length=100 )
	cat=models.ForeignKey(Category,on_delete=models.CASCADE)
	image=models.ImageField(upload_to='post/')
	list_per_page=30

	def __str__(self):
		return self.title