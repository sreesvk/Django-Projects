from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.index,name='index'),
    path('index/',views.index,name='index'),
    path('userlogin/',views.userlogin,name='userlogin'),
    path('userregistration/',views.userregistration,name='userregistration'),
    path('useraccount/',views.useraccount,name='useraccount'),
    path('logout/',views.logout,name='logout'),
    path('products/<int:id>',views.productview,name='products'),
    path('add_product/',views.add_product,name='add_product'),
    path('addtocart/<int:id>',views.addtocart,name='addtocart'),
    path('cart/',views.cart,name='cart'),
    path('delfromcart/<int:id>',views.delfromcart,name='delfromcart'),
    path('addtolist/<int:id>',views.addtolist,name='addtolist'),
    path('wishlist/',views.wishlist,name='wishlist'),
    path('delfromlist/<int:id>',views.delfromlist,name='delfromlist'),
    path('checkout/',views.checkout,name='checkout'),
    path('deleteorder/<int:id>',views.deleteorder,name='deleteorder'),
    path('search',views.search,name='search'),
    path('confirm_order/',views.order_confirm,name='confirm order'),
    path('confirmed/',views.confirmed,name='confirm'),
    path('contact/',views.contact,name='contact'),
    path('pd/<int:id>',views.pd,name='pd'),
    path('shoppy-cart',views.pcart,name='shoppy-cart'),
    path('delallcart/',views.delallcart,name='delallcart'),
    path('check-out/',views.pout,name='check-out'),
    path('confirmed_order/',views.cnodr,name='confirmed_order'),
    path('delfromcout/<int:id>',views.delfromcout,name='delfromcout'),
    path('purchased/',views.purchased,name='purchased'),
    path('deldis/',views.deldis,name='deldis'),
    

    path('adminlogin',views.adminlogin,name='adminlogin'),
    path('adminproducts',views.adminproducts,name='adminproducts'),
    path('adminlogout',views.adminlogout,name='adminlogout'),
    path('admineditprod/<int:id>',views.admineditprod,name='admineditprod'),
    path('admindelprod/<int:id>',views.admindelprod,name='admindelprod'),
    path('cateditprod/<int:id>',views.cateditprod,name='admineditprod'),
    path('catdelprod/<int:id>',views.catdelprod,name='admindelprod'),

]+ static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)