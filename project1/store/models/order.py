from django.db import models


status=[('ACCEPTED','ACCEPTED'),
       ('PACKED','PACKED'),
       ('ON THE WAY','ON THE WAY'),
       ('DILIVERD','DILIVERD'),
       ('CANCEL','CANCEL')

       ]

class Order(models.Model):
    user=models.BigIntegerField(default=True)
    product_name=models.CharField(max_length=200)
    image=models.ImageField(null=True,blank=True)
    Qty=models.PositiveIntegerField(default=1)
    price=models.IntegerField()
    order_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=50,default='padding',choices=status)
