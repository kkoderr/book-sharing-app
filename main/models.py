from django.db import models
from django.conf import settings
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

# Create your models here.

class Borrowership(models.Model):
	borrowership_type = models.CharField(max_length=10) #free, paid
	price = models.IntegerField()

	def __str__(self):
		return self.borrowership_type

class Book(models.Model):
	title = models.CharField(max_length=30)
	img = models.ImageField(upload_to='img/%Y/%m/%d/')
	author = models.CharField(max_length=50)
	availability = models.BooleanField(default=True)
	borrowership = models.ForeignKey(Borrowership, on_delete=models.CASCADE)
	owner = models.CharField(max_length=30)

class UserBorrowership(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	borrowership = models.ForeignKey(Borrowership, on_delete=models.CASCADE)
	#payment_id
	book = models.ForeignKey(Book, on_delete=models.CASCADE)
	turned_back = models.BooleanField(default= False)
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()
	#owner = models.ForeignKey()


class Ownership(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	book = models.ForeignKey(Book, on_delete=models.CASCADE)
	city_region = models.CharField(max_length=30)


class Owner(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	rating = models.IntegerField()

class Group(models.Model):
	name = models.CharField(max_length=30)
	group_icon = models.ImageField(upload_to='group_icon/%Y/%m/%d')
	members = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class AbstractPost(models.Model):
	#post_owner = foreingKey
	post_content = models.TextField()
	likes = models.IntegerField()
	dislikes = models.IntegerField()
	#reply = models.ForeignKey(Reply, on_delete=models.CASCADE)

	class Meta:
		abstract = True

class Reply(AbstractPost):
	post_content = models.TextField()


# class User(models.Model):
# 	def save(self, *args,**kwargs):
# 		pass
