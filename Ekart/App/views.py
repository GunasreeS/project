from django.shortcuts import render,redirect
from django.contrib.auth.models import User 
from App.models import Product,Cart,Category,User,Rolerest,Myorders,Orders
from App.forms import UsForm,ProductForm,CartForm,RoleR,CategoryForm,RolUp,UpdPfle,Shipform,ChpwdForm,UpadatePro,CreditForm
from django.core.mail import send_mail
from Ekart import settings
from django.core.mail import EmailMessage
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
import tempfile
from django.template.loader import get_template


# Create your views here.
def home(request):
	data=Category.objects.all()
	a=Cart.objects.filter(user_id=request.user.id)
	count=0
	for i in a:
		count=count+1
	return render(request,'html/home.html',{'data':data,'count':count})


def store(request,id):
	d=Category.objects.all()
	data=Product.objects.filter(cid_id=id)
	a=Cart.objects.filter(user_id=request.user.id)
	count=0
	for i in a:
		count=count+1
	paginator=Paginator(data,4)
	page=request.GET.get('page')
	try:
		data=paginator.page(page)
	except PageNotAnInteger:
		data=paginator.page(1)
	except EmptyPage:
		data=paginator.page(paginator.num_pages)
	return render(request,'html/store.html',{'info':data,'data':d,'count':count})

@login_required
def cart(request):
	data=Category.objects.all()
	a=Cart.objects.filter(user_id=request.user.id)
	amount=1
	sum=0
	count=0
	for i in a:
		amount=i.qunatity*i.product.price
		count=count+1
		sum=sum+amount
		i.amount=amount
	return render(request,'html/cart.html',{'info':a,'sum':sum,'count':count,'data':data})

def quantity(request,id):
	c=Cart.objects.get(id=id)
	c.qunatity=c.qunatity+1
	c.save()
	return redirect('/cart')

def remqun(request,id):
	c=Cart.objects.get(id=id)
	c.qunatity=c.qunatity-1
	c.save()
	return redirect('/cart')

@login_required
def checkout(request):
	d=Shipform(request.POST,instance=request.user)
	a=Category.objects.all()
	if request.method == "POST":
		if d.is_valid():
			d.save()
			return redirect('/Payment')
	d=Shipform(instance=request.user)
	return render(request,'html/checkout.html',{'da':a,'data':a})

@login_required
def payment(request):
	c=Cart.objects.filter(user_id=request.user.id)
	d=Category.objects.all()
	amount=1
	sum=0
	count=0
	for i in c:
		amount=i.qunatity*i.product.price
		count=count+1
		sum=sum+amount
		i.amount=amount
	f=CreditForm(request.POST,instance=request.user)
	if request.method=="POST":
		if f.is_valid():
			m=request.user.email
			receiver=m
			e = f.save(commit=False)
			sb = "Order confirmed"
			mg = 'Ordered items ::'+str(count)+'\n'+ ' will be delivered within 15 days.\n'+'Total amount paid: Rs.'+str(sum)+'\n'+'THANK YOU for Shopping!! \n'+"DESCRIPTION::\n"
			sd = settings.EMAIL_HOST_USER
			snt = EmailMessage(sb,mg,sd,[receiver])
			snt.content_subtype='html'
			snt.send()
			for i in c:
				x=User.objects.get(id=i.product.pid_id)
				sb1= "Order Received"
				mg1='Dear {} you have order to delivery a product : {}, of quantity:: {} within 10 days'.format(x.username,i.product.itemname,i.qunatity)
				sd1=settings.EMAIL_HOST_USER
				re=x.email
				snt=send_mail(sd1,mg1,sd1,[re])
				a=Myorders(pname=i.product.itemname,price=i.product.price,im=i.product.image,user_id=request.user.id,prod=i.product.pid_id,qunatity=i.qunatity)
				a.save()
				b=Orders(pname=i.product.itemname,price=i.product.price,im=i.product.image,prod=i.product.pid_id)
				b.save()
				c.delete()
			e.save()
			messages.success(request,"Successfully placed order")
			return redirect('/')
	f=CreditForm(instance=request.user)
	return render(request,'html/payment.html',{'da':f,'cart':c,'sum':sum,'data':d})
@login_required
def ordercancel(request,si):
	x=Myorders.objects.get(id=si)
	x.delete()
	return redirect('/myorders')

@login_required
def myorders(request):
	a=Cart.objects.filter(user_id=request.user.id)
	my=Myorders.objects.filter(user_id=request.user.id)
	d=Category.objects.all()
	sum=0
	count=0
	for i in my:
		count=count+1
		sum=sum+i.price
	count1=0
	for j in a:
		count1=count1+1
	return render(request,'html/myorders.html',{'sum':sum,'my':my,'data':d,'count':count1})

@login_required
def delivery(request):
	c=Myorders.objects.filter(prod=request.user.id,is_status=0)
	return render(request,'html/delivery.html',{'de':c})
def dell(request,id):
	c=Myorders.objects.get(id=id)
	c.is_status=1
	c.save()
	return redirect('/delivery')

def registration(request):
	if request.method=="POST":
		p=UsForm(request.POST)
		if p.is_valid():
			if p.password1 != p.password2:
				messages.add_message(request,messages.WARNING,'password and confirm_password does not match')
				return render(request,'html/registration.html')
			else:
				e = p.save(commit=False)
				sb = "Testing Email For Ekart"
				mg = "Hi Welcome {}. You have successfully registered for Ekart website".format(e.username)
				sd = settings.EMAIL_HOST_USER
				snt = send_mail(sb,mg,sd,[e.email])
				if snt == 1:
					e.save()
					return redirect('/lg')
				else:
					return redirect('/')
	p=UsForm()
	return render(request,'html/registration.html',{'u':p})

def Login_user(request):
	if request.method=='POST':
		username=request.POST.get('username')
		password=request.POST.get('password')

		user=authenticate(request,username=username,password=password)

		if not user:
			messages.add_message(request,messages.WARNING,'invalid Credentials')
			return render(request,'html/login.html')
		else:
			login(request,user)
			messages.add_message(request,messages.SUCCESS,f'Welcome {user.username}')
			return redirect('/')
	return render(request,'html/login.html')


@login_required
def product(request):
	if request.method=="POST":
		j=ProductForm(request.POST,request.FILES)
		if j.is_valid():
			i=j.save(commit=False)
			i.pid_id=request.user.id
			i.save()
	j=ProductForm()
	k=Product.objects.all()
	return render(request,'html/product.html',{'u':j,'info':k})

@login_required
def joinus(req):
	if req.method=="POST":
		a=Sellerform(req.POST,req.FILES)
		if a.is_valid():
			a.save()
	a=Sellerform()
	return render(req,'html/joinus.html',{'s':a,'data':d})

@login_required
def deletedata(req,id):
	data=Product.objects.get(id=id)
	data.delete()
	return redirect('/product')

@login_required
def profile(req):
	data=Category.objects.all()
	return render(req,'html/profile.html',{'data':data})

@login_required
def updateprofile(request):
	data=Category.objects.all()
	if request.method == "POST":
		t = UpdPfle(request.POST,instance=request.user)
		if t.is_valid():
			t.save()
			return redirect('/profile')
	t = UpdPfle(instance=request.user)
	return render(request,'html/updateprofile.html',{'z':t,'data':data})

@login_required
def sellerdetails(req):
	data=Category.objects.all()
	p=User.objects.filter(role=2)
	return render(req,'html/sellerdetails.html',{'se':p,'data':data})

@login_required
def addcart(request,id):
	a=Product.objects.get(id=id)
	if request.method=="POST":
		c=Cart(user_id=request.user.id,product_id=a.id)
		c.save()
		return redirect('/cart')
	return render(request,'html/addcart.html')

@login_required
def remove(req,id):
	data=Cart.objects.get(id=id)
	data.delete()
	return redirect('/cart')

@login_required
def yourproducts(request):
	d=Product.objects.filter(pid_id=request.user.id)
	return render(request,'html/yourproducts.html',{'data':d})

@login_required
def permissions(request):
	data=Category.objects.all()
	ty=Rolerest.objects.all()
	return render(request,'html/givepermissions.html',{'q':ty,'data':data})

@login_required
def rolreq(request):
	data=Category.objects.all()
	if request.method== "POST":
		k =RoleR(request.POST)
		if k.is_valid():
			s=k.save(commit=False)
			s.uname= request.user.username
			s.uid_id= request.user.id
			sb = "Testing mail"
			mg = "Hi Welcome {}. You have successfully requested for seller.Please wait for your request acceptance".format(s.uname)
			sd = settings.EMAIL_HOST_USER
			snt = send_mail(sb,mg,sd,[s.email])
			if snt == 1:
				s.save()
				return redirect('/')
			else:
				return redirect('/')
	k=RoleR()
	return render(request,'html/rolreq.html',{'a':k,'data':data})
@login_required
def giveper(request,k):
	data=Category.objects.all()
	r=User.objects.get(id=k)
	if request.method == "POST":
		k=RolUp(request.POST,instance=r)
		if k.is_valid():
			e=k.save(commit=False)
			sb = "Confirmation Email For Ekart"
			mg = "Hi Welcome {}. Your request is accepted.....Now you are a seller".format(r.username)
			sd = settings.EMAIL_HOST_USER
			snt = send_mail(sb,mg,sd,[r.email])
			e.save()
			return redirect('/per')
	k2= RolUp(instance=r)
	return render(request,'html/acceptpermissions.html',{'y':k2,'data':data})


@login_required
def addcategory(request):
	data=Category.objects.all()
	if request.method=="POST":
		a=CategoryForm(request.POST)
		if a.is_valid():
			a.save()
	c=CategoryForm()
	return render(request,'html/addcategory.html',{'c':c,'data':data})

def search(request):
	try:
		q=request.GET.get('q')
	except:
		q=None
	if q:
		p1=Product.objects.filter(itemname__icontains=q)
		paginator=Paginator(p1,8)
		page=request.GET.get('page')
		try:
			p1=paginator.page(page)
		except PageNotAnInteger:
			p1=paginator.page(1)
		except EmptyPage:
			p1=paginator.page(paginator.num_pages)
		context={'d':p1}
		template="html/search.html"
	else:
		message="Search for a specific Product name"
		context={'empty':True,'message':message}
		template="html/search.html"
	return render(request,template,context)
	return render(con)

@login_required
def cgf(request):
	data=Category.objects.all()
	if request.method=="POST":
		print("yes")
		c=ChpwdForm(user=request.user,data=request.POST)
		if c.is_valid():
			c.save()
			return redirect('/lg')
	c=ChpwdForm(user=request)
	return render(request,'html/changepwd.html',{'t':c,'data':data})

@login_required
def uptpro(request,id):
	d=Product.objects.get(id=id)
	if request.method=="POST":
		a=UpadatePro(request.POST,instance=d)
		if a.is_valid():
			a.save()
			return redirect('/yourpro')
	b=UpadatePro(instance=d)
	return render(request,'html/updateproduct.html',{'d':b})
@login_required
def viewcategory(req):
	d=Category.objects.all()
	return render(req,'html/Category.html',{'data':d})

@login_required
def deletecat(req,id):
	d=Category.objects.get(id=id)
	d.delete()
	return redirect('/category')
