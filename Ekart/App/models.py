from django.db import models
from django.contrib.auth.models import User,AbstractUser
from datetime import date
# Create your models here.
class User(AbstractUser):
	t=[(1,'customer'),(2,'seller')]
	age= models.IntegerField(null=True)
	phonenu=models.IntegerField(null=True)
	image=models.ImageField(null=True,blank=True)
	phno=models.CharField(null='True',max_length=30)
	address=models.TextField(null='True')
	city=models.CharField(max_length=30,null='True')
	state=models.CharField(max_length=40,null='True')
	pin=models.IntegerField(null='True')
	creditcardnumber=models.IntegerField(null='True')
	Expyear=models.CharField(max_length=20,null='True')
	expmonth=models.CharField(max_length=20,null='True')
	cvv=models.IntegerField(null='True')
	role=models.IntegerField(choices=t,default=1)


class Category(models.Model):
	cname=models.CharField(max_length=20)
	def __str__(self):
		return self.cname


class Product(models.Model):
	pid=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
	cid=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
	itemtype=models.CharField(max_length=200,null=True)
	itemname=models.CharField(max_length=200,null=True)
	price= models.FloatField()
	qunatity=models.IntegerField(null=True)
	image=models.ImageField(null=True,blank=True)

	def __str__(self):
		return self.itemname

class Myorders(models.Model):
	pname=models.CharField(max_length=300)
	price=models.IntegerField()
	a=[("product quality issues","product quality issues"),("I want to change address/phone number","I want to change address/phone number"),("I have purchased product somewhere else","I have purchased product somewhere else"),("others","others")]
	cancel=models.CharField(max_length=200,choices=a,null=True)
	im=models.ImageField()
	qunatity=models.IntegerField(default=1,null=True)
	is_status=models.IntegerField(default=0)
	date=models.DateTimeField(auto_now_add='True',null='True')
	user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
	prod=models.IntegerField(null=True)


class Cart(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	product=models.ForeignKey(Product,on_delete=models.CASCADE)
	qunatity=models.IntegerField(default=1,null=True)
	amount=models.IntegerField(default=0,null=True)


class Rolerest(models.Model):
	t=[(2,'seller')]
	uname=models.CharField(max_length=30)
	cname=models.CharField(max_length=50,null=True)
	email=models.CharField(max_length=100,null=True)
	roletype=models.IntegerField(choices=t)
	prf = models.CharField(max_length=250)
	is_checked=models.BooleanField(default=0)
	uid=models.OneToOneField(User,on_delete=models.CASCADE)

class Orders(models.Model):
	pname=models.CharField(max_length=300)
	price=models.IntegerField()
	im=models.ImageField()
	date=models.DateTimeField(auto_now_add='True',null='True')
	prod=models.IntegerField(null=True)
