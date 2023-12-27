from django.contrib import admin
from .models import UserRegistration,Product,Category,Cart,Wishlist,Order,Purchased
# Register your models here.
admin.site.register(UserRegistration)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(Wishlist)
admin.site.register(Order)
admin.site.register(Purchased)


