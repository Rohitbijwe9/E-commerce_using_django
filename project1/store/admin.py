from django.contrib import admin
from .models import Product
from .models import Catogory
from .models import Customer
from .models import Cart
from .models import Order

#class ProductAdmin(admin.ModelAdmin):
    #list_display = []

class AdminProduct(admin.ModelAdmin):
    list_display = ['id','name','price','catagory','description','image']
class AdminCustomer(admin.ModelAdmin):
    list_display = ['id','name','phone']

class AdminCart(admin.ModelAdmin):
    list_display = ['phone','product','image','quantity','price']
class AdminOrder(admin.ModelAdmin):
    list_display = ['user','product_name','image','Qty','price','order_date','status']

admin.site.register(Product,AdminProduct)
admin.site.register(Catogory)
admin.site.register(Customer,AdminCustomer)
admin.site.register(Cart,AdminCart)
admin.site.register(Order,AdminOrder)


# Register your models here.
