from django.shortcuts import HttpResponse, redirect
from django.shortcuts import render
from .models.product import  Product
from .models.catagory import  Catogory
from .models.customer import  Customer
from .models.cart import  Cart
from .models.order import  Order
from django.contrib import messages
from  django.views import  View
from  django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
import random

from django.db.models  import Q

# Create your views here.

def farmdet(request):
    template_name='store/farmdet.html'
    context={}
    return render(request,template_name,context)

def index(request):
    total_iteam=0
    products=None
    if request.session.has_key('phone'):
        phone=request.session['phone']
        catagory=Catogory.get_all_categories()
        customer=Customer.objects.filter(phone=phone)
        total_iteam=len(Cart.objects.filter(phone=phone))

        for c in customer:
            name=c.name

            catagoryId=request.GET.get('category')
            if catagoryId:
                products=Product.get_all_product_by_category_id(catagoryId)
            else:
                products=Product.get_all_product



            template_name='store/home.html'

            #context={'products':products,'catagory':catagory}
            context={'products':products,'catagory':catagory,'name':name,'total_iteam':total_iteam}
            print(request.session.get('phone'))
            return render(request,template_name,context)
    else:
        return redirect('login_url')



#==================================================Login====================================================================
class Login(View):

    def get(self,request):
        template_name = 'store/login.html'
        return render(request, template_name)

    def post(self,request):
        template_name = 'store/login.html'

        otpn = random.randint(1000, 9999)

        to_email = request.POST.get('email')
        subject = 'WELCOME'
        massage = f'welcome to 32 ACERS ORGANIC FARMS YOUR LOGIN ID IS {otpn}'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [to_email]
        send_mail(subject, massage, from_email, recipient_list)


        phone = request.POST.get('phone')
        error_massage = None
        value = {'phone': phone}
        customer = Customer.objects.filter(phone=request.POST['phone'])
        if customer:
            request.session['phone']=phone
            return redirect('otp_url',otp1=otpn)
        else:
            error_massage = 'Mobile Number is Invalid!!'
            context = {'error': error_massage, 'value': value}
        return render(request, template_name, context)





#==========================================================signup==============================================
class Signup(View):
    def get(self,request):
        template_name = 'store/signup.html'
        return render(request, template_name)

    def post(self,request):
        template_name = 'store/signup.html'
        postDta = request.POST
        name = postDta.get('name')
        phone = postDta.get('phone')

        error_massage = None

        value = {
            'phone': phone,
            'name': name
        }

        customer = Customer(name=name, phone=phone)
        if (not name):
            error_massage = 'Name is required'

        elif (not phone):
            error_massage = 'Phone no is required'

        elif len(phone) < 10:
            error_massage = 'Mobile no is 10 charactor required'
        elif customer.isExist():
            error_massage = 'Mobile Number Already Exist'

        if not error_massage:
            messages.success(request, 'Congratulation !! Register sucessfull')

            customer.register()

            return redirect('signup_url')
        else:
            context = {'error': error_massage, 'value': value}
            return render(request, template_name, context)
#==========================================product det--------------------------------------------------------

def product(request,pk):
    total_iteam=0
    template_name='store/productdetail.html'
    product= Product.objects.get(pk=pk)
    iteam_already_in_cart=False
    if request.session.has_key('phone'):
        phone=request.session['phone']
        total_iteam=len(Cart.objects.filter(phone=phone))
        iteam_already_in_cart = Cart.objects.filter(Q(product=product.id) & Q(phone=phone)).exists()
        customer= Customer.objects.filter(phone=phone)
        for c in customer:
            name=c.name

    context={'product':product,'iteam_already_in_cart':iteam_already_in_cart,'name':name,'total_iteam':total_iteam}

    return render(request,template_name,context)

#=========================logout----------------------------------------------------------

def logout(request):
    if request.session.has_key('phone'):
        del request.session['phone']
        return redirect('login_url')
    else:
        return redirect('login_url')
    #=============================================add cart========================================

def addcart(request):
    phone=request.session['phone']
    product_id=request.GET.get('prod_id')
    product_name= Product.objects.get(id=product_id)
    product= Product.objects.filter(id=product_id)

    for p in product:
        image=p.image
        price=p.price
        Cart(phone=phone,product=product_name,image=image,price=price).save()
        return redirect(f"/productdet/{product_id}/")

#==============================show cart========================================




def showcart(request):
    total_iteam= 0
    if request.session.has_key('phone'):
        phone = request.session['phone']
        total_iteam = len(Cart.objects.filter(phone=phone))
        customer = Customer.objects.filter(phone=phone)
        for c in customer:
            name = c.name

            cart = Cart.objects.filter(phone=phone)
            context={'name':name,'total_iteam':total_iteam,'cart':cart}

            if cart:
                template_name='store/showcart.html'
                return render(request,template_name,context)
            else:
                template_name='store/emptycart.html'
                return render(request,template_name,)



def plus_cart(request):
    if request.session.has_key('phone'):
        phone = request.session['phone']
        product_id = request.GET['prod_id']
        cart= Cart.objects.get(Q(product=product_id) & Q(phone=phone))
        cart.quantity+=1
        cart.save()

        data = {'quantity': cart.quantity}
        return JsonResponse(data)






def minus_cart(request):
    if request.session.has_key('phone'):
        phone = request.session['phone']
        product_id = request.GET['prod_id']
        cart= Cart.objects.get(Q(product=product_id) & Q(phone=phone))
        cart.quantity-=1
        cart.save()

        data = {'quantity': cart.quantity}
        return JsonResponse(data)


def remove_cart(request):
    if request.session.has_key('phone'):
        phone = request.session['phone']
        product_id = request.GET['prod_id']
        cart= Cart.objects.get(Q(product=product_id) & Q(phone=phone))
        cart.delete()

        return JsonResponse()


def Checkout_view(request):
    templatee_name='includes/checkout.html'

    if request.session.has_key('phone'):
        phone = request.session['phone']
        name =request.POST.get('name')
        adress =request.POST.get('adress')
        mobile =request.POST.get('mobile')
        cart_product = Cart.objects.filter(phone=phone)
        for i in cart_product:
            qty=i.quantity
            price=i.price
            product_name=i.product
            image=i.image

            Order(user=phone,product_name=product_name,image=image,Qty=qty,price=price).save()
            cart_product.delete()
    if request.method=='POST':
        to_email = request.POST.get('email')
        subject = 'THANK YOU'
        massage = f'your order placeed successfully , your order will deliver next 5to7 working day , THANKYOU FOR SHOPING FROM 32 ACERS ORGANIC FARMS'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [to_email]
        send_mail(subject, massage, from_email, recipient_list)
        return redirect('orderconf2_url')
    return render(request,templatee_name)


def ordhis(request):
    total_iteam=0
    template_name='store/ordhis.html'

    if request.session.has_key('phone'):
        phone = request.session['phone']
        total_iteam = len(Cart.objects.filter(phone=phone))
        customer = Customer.objects.filter(phone=phone)
        for c in customer:
            name = c.name

            order = Order.objects.filter(user=phone)
            context = {'order': order, 'name': name, 'total_iteam': total_iteam}

            if order:
                return render(request, template_name, context)
            else:
                return render(request, 'store/emptyorder.html', context)

    else:
        return redirect('login_url')





def otp(request,otp1):

    template_name = 'store/otp.html'

    if request.method == 'POST':
        otp_no = request.POST.get('otp')
        if otp1 == int(otp_no):
            return redirect('home_url')
        else:
            return redirect('otp_url')
    return render(request, template_name)




def thank(request):
    template_name='store/orderconf.html'
    return render(request,template_name)
