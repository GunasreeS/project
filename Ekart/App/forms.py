from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django import forms
from App.models import Product,User,Rolerest,Category,Myorders





class UsForm(UserCreationForm):
	password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"password"}))
	password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"confirm password"}))
	class Meta:
		model=User
		fields=['username','email']
		widgets={
		"username":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"username",
			}),
		"email":forms.EmailInput(attrs={"class":"form-control","placeholder":"Email"})


		}

class ProductForm(forms.ModelForm):
	class Meta:
		model=Product
		fields=['cid','itemtype','itemname','price','qunatity','image']
		widgets={
		"category":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"category",
			}),
		"itemtype":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"itemtype",
			}),
		"itemname":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"itemname",
			}),
		"price":forms.NumberInput(attrs={
			"class":"form-control",
			"placeholder":"price",
			}),
		"qunatity":forms.NumberInput(attrs={
			"class":"form-control",
			"placeholder":"quantity",
			}),
		}



class CartForm(forms.ModelForm):
	class Meta:
		model=Product
		fields=['itemname','price','image']
		widgets={
		"itemname":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"itemname",
			}),
		"price":forms.NumberInput(attrs={
			"class":"form-control",
			"placeholder":"itemname",
			}),
		}

class CategoryForm(forms.ModelForm):
	class Meta:
		model=Category
		fields=["cname"]
		widgets={
		"cname":forms.TextInput(attrs={"class":"form-control","placeholder":"enter cname"}),
		}

class RoleR(forms.ModelForm):
	class Meta:
		model = Rolerest
		fields= ["cname","email","roletype","prf"]
		widgets={
		"uname":forms.TextInput(attrs={"class":"form-control","readonly":True}),
		"cname":forms.TextInput(attrs={"class":"form-control","placeholder":"enter category name you have"}),
		"email":forms.EmailInput(attrs={"class":"form-control","placeholder":"Email"}),
		"roletype":forms.Select(attrs = {"class": "form-control",}),
		"prf":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Enter proof"}),


		}

class RolUp(forms.ModelForm):
	class Meta:
		model = User
		fields = ["username","role"]
		widgets={
		"username": forms.TextInput(attrs={"class":"form-control","readOnly":True,}),
		"role":forms.Select(attrs={"class":"form-control"}),
		}

class UpdPfle(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username','email','age','phno','address','city','state','pin']
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control",
			"readonly":True,
			}),
		"email":forms.EmailInput(attrs={"class":"form-control","placeholder":"update email","required":True,}),
		"age":forms.NumberInput(attrs={"class":"form-control","placeholder":"update age","required":True,}),
		"address":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"address"}),
		"email":forms.EmailInput(attrs={"class":"form-control my-2","placeholder":"Enter your email"}),
		"phno":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Phone number"}),
		"city":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"city"}),
		"state":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"state"}),
		"pin":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Pincode"}),
		}

class Shipform(forms.ModelForm):
	class Meta:
		model=User
		fields=["phno","address","city","state","pin"]
		widgets = {
		"phno":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Phone number"}),
		"city":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"city"}),
		"address":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"address"}),
		"state":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"state"}),
		"pin":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Pincode"}),
		}

class ChpwdForm(PasswordChangeForm):
	old_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control",'placeholder':"Enter Old password"}))
	new_password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control",'placeholder':"Enter New password"}))
	new_password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control",'placeholder':"Confirm your New password"}))
	class Meta:
		model=User
		fields=['oldpassword','newpassword','confirmpassword']

class UpadatePro(forms.ModelForm):
	class Meta:
		model=Product
		fields=['price','qunatity']
		widgets={
		"price":forms.NumberInput(attrs={
			"class":"form-control",
			"placeholder":"price",
			}),
		"qunatity":forms.NumberInput(attrs={
			"class":"form-control",
			"placeholder":"quantity",
			}),
		}

class CreditForm(forms.ModelForm):
	class Meta:
		model=User
		fields=['creditcardnumber','Expyear','expmonth','cvv']
		widgets={
		"creditcardnumber":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"card number"}),
		"Expyear":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Expyear"}),
		"expmonth":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"expmonth"}),
		"cvv":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"cvv number"}),
		}
						
class Delivery(forms.ModelForm):
	class Meta:
		model=Myorders
		fields=['is_status']
		widgets={
		"is_status":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"status"}),
		}