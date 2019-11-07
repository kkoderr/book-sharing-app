from django.db import models
from django.conf import settings
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

# Create your models here.

class Book(models.Model):
	title = models.CharField(max_length=30)
	img = models.ImageField(upload_to='img/%Y/%m/%d/')
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
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	borrowership = models.ForeignKey(Borrowership, on_delete=models.CASCADE)
	#payment_id
	book = models.ForeignKey(Book, on_delete=models.CASCADE)
	turned_back = models.BooleanField(default= False)
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()
	#owner = models.Foreignkey()


class Ownership(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	book = models.ForeignKey(Book, on_delete=models.CASCADE)
	city_region = models.CharField(max_length=30)


class Owner(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	#rating =

class Group(models.Model):
	name = models.CharField(max_length=30)
	group_icon = models.ImageField(upload_to='group_icon/%Y/%m/%d')
	members = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class AbstractPost(models.Model):
	#post_owner = foreingKey
	post_content = models.TextField()
	#likes =
	#dislikes
	reply = models.Foreignkey(Reply, on_delete=models.CASCADE)

	class Meta:
		abstract = True

class Reply(Post):
	post_content = models.TextField()


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

	USERNAME_FIELD = 'email'
