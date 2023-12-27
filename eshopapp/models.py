from django.db import models

class UserRegistration(models.Model):
    user_register_name=models.CharField(max_length=255)
    user_register_email=models.EmailField(max_length=255)
    user_register_number=models.CharField(max_length=255)
    user_register_user=models.CharField(max_length=255)
    user_register_pic=models.CharField(null=True)
    user_password=models.CharField(max_length=255)
    def __str__(self):
        return self.user_register_name
class Product(models.Model):
    product_name=models.CharField(max_length=255)
    product_color =models.CharField(max_length=255,null=True)
    product_price=models.FloatField()
    product_image = models.CharField(null=True) 
    product_disc=models.CharField(null=True,max_length=400)
    product_cat=models.IntegerField(null=True)
    product_id = models.IntegerField(null=True)

    def __str__(self):
        return self.product_name
class Category(models.Model):
    cat_name=models.CharField(max_length=255)
    cat_image=models.CharField(null=True,)
    cat_product_no=models.IntegerField(null=True)
    cat_count = models.IntegerField(null=True, default=0)

    def __str__(self): 
        return self.cat_name
class Cart(models.Model):
    cart_user=models.CharField(max_length=255)
    cart_id=models.IntegerField()
    cart_name=models.CharField(max_length=255)
    cart_color = models.CharField(max_length=255,null=True)
    cart_quantity=models.IntegerField()
    cart_price=models.FloatField()
    cart_disc = models.CharField(null=True,max_length=400)
    cart_image=models.CharField( null=True) 
    total_price=models.FloatField(default=0)
    def __str__(self):
        return self.cart_name
class Wishlist(models.Model):
    list_user=models.CharField(max_length=255,null=True)
    list_name=models.CharField(max_length=255)
    list_image=models.CharField(null=True)
    list_price=models.FloatField()
    list_id = models.CharField(max_length=255,null=True)
    def __str__(self):
        return self.list_name
class Order(models.Model):
    o_product_name=models.CharField(max_length=255)
    o_product_qty=models.IntegerField()
    o_product_price=models.FloatField()
    o_product_image=models.CharField(null=True)
    o_product_total=models.FloatField(default=0)
    current_user=models.CharField(max_length=255)
    delvry_fname=models.CharField(max_length=255)
    delvry_lname=models.CharField(max_length=255)
    delvry_mail=models.CharField(max_length=255)
    delvry_phone=models.CharField(max_length=255)
    delvry_address=models.TextField()
    delvry_upi=models.CharField(max_length=255,default='inda@upi')
    delvry_type=models.CharField(max_length=255,default='cod')
    
    def __str__(self):
        return self.o_product_name

    # Create your models here.
