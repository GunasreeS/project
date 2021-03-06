from django.urls import path
from App import views
from django.contrib.auth import views as v

urlpatterns =[
    path('store/<int:id>/',views.store,name="store"),
    path('',views.home,name="home"),
    path('cart/',views.cart,name="carts"),
    path('checkout/',views.checkout,name="checkout"),
    path('Payment/',views.payment,name="pay"),
    path('product/',views.product,name="product"),
    path('lg/',views.Login_user,name="lg"),
    path('lgo/',v.LogoutView.as_view(template_name='html/logout.html'),name="logo"),
    path('reg/',views.registration,name="reg"),
    path('profile/',views.profile,name='pro'),
    path('upr/',views.updateprofile,name="upf"),
    path('join/',views.joinus,name="join"),
    path('del/<int:id>/',views.deletedata,name="delete"),
    path('seller/',views.sellerdetails,name="seller"),
    path('addcart/<int:id>/',views.addcart,name="addcart"),
    path('remove/<int:id>/',views.remove,name="remove"),
    path('yourpro/',views.yourproducts,name="yrpro"),
    path('category/',views.addcategory,name="addcategory"),
    path('per/',views.permissions,name='perm'),
    path('rlrq/',views.rolreq,name='rr'),
    path('gvp/<int:k>/',views.giveper,name='gvpr'),
    path('search/',views.search,name='search'),
    path('ch/',views.cgf,name="cg"),
    path('updateproduct/<int:id>/',views.uptpro,name='uppro'),
    path('view/',views.viewcategory,name="viewcat"),
    path('delete/<int:id>/',views.deletecat,name="deletecat"),
    path('rst/',v.PasswordResetView.as_view(template_name="html/resetpassword.html"),name="rt"),
    path('rst_done/',v.PasswordResetDoneView.as_view(template_name="html/resetpassworddone.html"),name="password_reset_done"),
    path('rst_cf/<uidb64>/<token>/',v.PasswordResetConfirmView.as_view(template_name="html/resetpasswordconfirm.html"),name="password_reset_confirm"),
    path('rst_cmplt/',v.PasswordResetCompleteView.as_view(template_name="html/resetpwdcomplete.html"),name="password_reset_complete"),
    path('myorders/',views.myorders,name="myorders"),
    path('ordcancel/<int:si>/',views.ordercancel,name="ordcancel"),
    path('delivery/',views.delivery,name="delivery"),
    path('deli/<int:id>/',views.dell,name="deli"),
    path('quan/<int:id>/',views.quantity,name="quan"),
    path('req/<int:id>/',views.remqun,name="req"),

]