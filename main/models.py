from django.db import models

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

# Create your models here.

class Book(models.Model):
	title = models.CharField(max_length=30)
	author = models.CharField(max_length=50)
	availability = models.BooleanField(default=True)
	borrowership = models.ForeignKey(Borrowership, on_delete=models.CASCADE)
	owner = models.CharField(max_length=30)
	

class Borrowership(models.Model):
	borrowership_type = models.CharField(max_length=10) #free, paid
	price = models.IntegerField()

	def __str__(self):
		return self.borrowership_type


class UserBorrowership(models.Model):
	#user = foreingKey(user)
	borrowership = models.ForeignKey(Borrowership, on_delete=models.CASCADE)
	#payment_id
	book = models.ForeignKey(Book, on_delete=models.CASCADE)
	turned_back = models.BooleanField(default= False)
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()
	#owner = models.Foreignkey()


class Ownership(models.Model):
	#user = foreingKey
	book = models.ForeignKey(Book, on_delete=models.CASCADE)
	city_region = models.CharField(max_length=30)


class Owner(models.Model):
	#user = foreingKey
	#rating = 

class Group(models.Model):
	name = models.CharField(max_length=30)
	#members = foreingKey


class Post(models.Model):
	#post_owner = foreingKey
	post_content = models.TextField()
	#likes = 
	#dislikes
	reply = models.Foreignkey(Reply, on_delete=models.CASCADE)

	class Meta:
		abstract = True

class Reply(Post):


class UserCreationModel(BaseUserManager):
	def create_user(self):
		user = self.model(email, password, **extra_fields)
		user.set_password(password)
		user.save(self._db)


class User(AbstractBaseUser, PermissionsMixin):
	username = models.CharField(max_length)
	email = models.EmailField(max_length=255, unique=True)
	name = models.CharField(max_length=30, unique=True)

	objects = UserCreationModel()

	#USERNAME_FIELD = 
	 



