from django.urls import path
from .views import *

urlpatterns=[
    path('product/',index,name='home_url'),
    path('signup/',Signup.as_view(),name='signup_url'),
    path('login/',Login.as_view(),name='login_url'),
    path('productdet/<int:pk>/',product,name='productdet_url'),
    path('logout/', logout, name='logout_url'),
    path('addcart/', addcart, name='addcart_url'),
    path('showcart/', showcart, name='showcart_url'),
    path('plus_cart/', plus_cart, name='plus_cart'),
    path('minus_cart/', minus_cart, name='mius_cart'),
    path('remove_cart/', remove_cart, name='remove_cart'),

    path('checkout/',Checkout_view, name='checkout'),
    path('order/',ordhis, name='order_url'),
    path('farm/',farmdet,name='farm_url'),

    path('otp/<int:otp1>/',otp,name='otp_url'),


    path('thankyou/',thank,name='orderconf2_url')




]