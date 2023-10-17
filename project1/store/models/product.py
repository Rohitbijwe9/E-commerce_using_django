from  django.db import models
from .catagory import Catogory

class Product(models.Model):
    name=models.CharField(max_length=20)
    price=models.IntegerField(default=0)
    catagory=models.ForeignKey(Catogory,on_delete=models.CASCADE,default=1)
    description=models.CharField(max_length=200,default='',blank=True,null=True)
    image=models.ImageField(upload_to='products/',)


    @staticmethod
    def get_all_product():
        return Product.objects.all()
    @staticmethod
    def get_all_product_category_id(catagory_id):
        if catagory_id:
            return Product.objects.filter(catagory=catagory_id)
        else:
            return Product.get_all_product()







    def __str__(self):
        return self.name
