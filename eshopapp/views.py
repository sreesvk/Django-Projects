from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import UserRegistration,Category,Product,Cart,Wishlist,Order,Purchased

def index(request):
    listcount=0
    if 'user' not in request.session:
        pro_cat = Category.objects.all()
        wid =[7,8,9,10,11]
        women_products = Product.objects.filter(id__in=eid)
        men_products = Product.objects.filter(product_cat = 1)
        mp = [43,44,40,41,52,45]
        m_p = Product.objects.filter(id__in=mp)
        eid = [46,50,49,47,51,48]
        e_c = Product.objects.filter(id__in=eid)
        w_p = Product.objects.filter(id__in=eid)


        cats = Category.objects.all()
        products = Product.objects.all()
        total=0
        context = {
            'pro_cat':pro_cat,
            'women_products':women_products,
            'men_products':men_products,
            'm_p':m_p,
            'w_p':w_p,
            'cats':cats,
            'products' :products,
            'e_c':e_c,
        } 
        template = loader.get_template('index.html')
        return HttpResponse(template.render(context,request))
    else:
        pro_cat = Category.objects.all()
        cart_user = request.session['user']
        wid =[7,8,9,10,11]
        listcount=Wishlist.objects.filter(list_user=cart_user).values('list_name').count()
        cart = Cart.objects.filter(cart_user=cart_user).order_by('-id').values()
        cart2 = Cart.objects.filter(cart_user=cart_user)
        list=Wishlist.objects.filter(list_user=cart_user)
        women_products = Product.objects.filter(id__in=wid)
        men_products = Product.objects.filter(product_cat = 1)
        ids = [43,44,40,41,52,45]
        m_p = Product.objects.filter(id__in=ids)
        eid = [46,50,49,47,51,48]
        e_c = Product.objects.filter(id__in=eid)
        cats = Category.objects.all()
        products = Product.objects.all()
        count = []
        for x in cats:
            catnos = Product.objects.filter(product_cat=x.id).values().count()
            count.append(catnos)

        total=0
        cartcount=0
        for x in cart2:
            total=total+x.total_price 
            cartcount = cartcount+x.cart_quantity 
        context = {
            'cart' : cart,
            'total' : total,
            'pro_cat':pro_cat,
            'cartcount':cartcount,
            'listcount' :listcount,
            'm_p':m_p,
            'e_c':e_c,
            'list' :list,
            'women_products':women_products,
            'men_products':men_products,
            'cats':cats,
            'catsno' :count,
            'cart_user':cart_user,
            'products' :products,
            'catnos' :catnos,
        } 
        template = loader.get_template('index.html')
        return HttpResponse(template.render(context,request))
        

def userlogin(request):
    if 'user' in request.session:
        return HttpResponseRedirect("/useraccount")
    if request.method=='POST':
        username=request.POST['user']
        password=request.POST['pass']
        login=UserRegistration.objects.filter(user_register_user=username,user_password=password).values()
        if(login):
            request.session['user']=username
            return HttpResponseRedirect("/useraccount")
    template=loader.get_template("userlogin.html")
    return HttpResponse(template.render({},request))

def userregistration(request):
    msg=""
    if request.method=='POST':
        reg_name=request.POST['user_register_name']
        reg_email=request.POST['user_register_email']
        reg_number=request.POST['user_register_number']
        reg_propic=request.FILES['user_register_pic']
        reg_user=request.POST['user_register_user']
        reg_pass=request.POST['user_password']

        user_exist=UserRegistration.objects.filter(user_register_user=reg_user)
        email_exist=UserRegistration.objects.filter(user_register_email=reg_email)
        num_exist=UserRegistration.objects.filter(user_register_number=reg_number)

        if email_exist:
            msg="Email already exist"
        elif num_exist:
            msg="Number already exist"
        elif user_exist:
            msg="Username already exist"
        else:
            reg=UserRegistration(user_register_name=reg_name,user_register_email=reg_email,user_register_number=reg_number,user_register_user=reg_user,user_password=reg_pass,user_register_pic=reg_propic)
            reg.save()
            return HttpResponseRedirect("/userlogin/")
    context={
        'msg': msg
    }
    template = loader.get_template('userregistration.html')
    return HttpResponse(template.render(context,request))

def useraccount(request):
    if 'user' not in request.session:
        return HttpResponseRedirect("/userlogin/")
    userpic = UserRegistration.objects.filter(user_register_user=request.session['user'])
    pro_cat = Category.objects.all()
    cart_user = request.session['user']
    women_products = Product.objects.filter(product_cat = 3)
    men_products = Product.objects.filter(product_cat = 1)
    cats = Category.objects.values()
    catsno = Product.objects.values('product_cat').count()
    
    total=0
    cartcount=0
    
    pro_cat = Category.objects.all()
    context = {
        'pro_cat' : pro_cat,
        'userpic' : userpic,
        'total' : total,
        'pro_cat':pro_cat,
        'cartcount':cartcount,
        'women_products':women_products,
        'men_products':men_products,
        'cats':cats,
        'catsno' :catsno,
        'cart_user':cart_user,
    }
    template=loader.get_template("useraccount.html")
    return HttpResponse(template.render(context,request))

def logout(request):
    del request.session["user"]
    return HttpResponseRedirect("/userlogin")

def productview(request,id):
    product=""
    pro_cat = Category.objects.all()
    userpix=request.session['user']
    userpic = UserRegistration.objects.filter(user_register_user=userpix).values()
    pro_cat = Category.objects.all()
    cart_user = request.session['user']
    listcount=Wishlist.objects.filter(list_user=cart_user).values('list_name').count()
    cart = Cart.objects.filter(cart_user=cart_user).order_by('-id').values()
    cart2 = Cart.objects.filter(cart_user=cart_user)
    list=Wishlist.objects.filter(list_user=cart_user)
    women_products = Product.objects.filter(product_cat = 3)
    men_products = Product.objects.filter(product_cat = 1)
    cats = Category.objects.values()
    catsno = Product.objects.values('product_cat').count()
    
    total=0
    cartcount=0
    for x in cart2:
        total=total+x.total_price 
        cartcount = cartcount+x.cart_quantity 
    if id==0:
        product = Product.objects.all().order_by('-id').values()
    else:
        product = Product.objects.filter(product_cat=id).order_by('-id').values()
    context = {
        'product' : product,
        'pro_cat' : pro_cat,
        'userpic' : userpic,
        'cart' : cart,
        'total' : total,
        'pro_cat':pro_cat,
        'cartcount':cartcount,
        'listcount' :listcount,
        'list' :list,
        'women_products':women_products,
        'men_products':men_products,
        'cats':cats,
        'catsno' :catsno,
        'cart_user':cart_user,
    }
    template = loader.get_template('products.html')
    return HttpResponse(template.render(context,request))

def add_product(request):
    msg=""
    if request.method =='POST':
        if 'product_submit' in request.POST:
            product_name = request.POST["product_name"]
            product_color= request.POST["product_color"]
            product_image = request.FILES["product_image"]
            product_price = request.POST["product_price"]
            product_disc = request.POST["product_disc"]
            product_cat= request.POST["cat_value"]
            registration = Product(product_name=product_name,product_color=product_color,product_image=product_image,product_price=product_price,product_disc=product_disc,product_cat=product_cat)
            registration.save()

            p_cat = Category.objects.get(id=product_cat)
            c = p_cat.cat_count
            p_cat.cat_count = c+1
            p_cat.save()



        if 'cat_submit' in request.POST:
            new_cat = request.POST["new_cat"]
            cat_image = request.FILES["cat_image"]
            new_cat_no = request.POST["new_cat_no"]
            catpro=Category.objects.values('cat_name')
            if new_cat == "":
             prodcat = Category.objects.values('cat_name')
            elif new_cat==catpro:
                msg="Category already exist"
            catreg = Category(cat_name=new_cat,cat_image=cat_image,cat_product_no=new_cat_no)
            catreg.save()

    prod_cat = Category.objects.all()

    template = loader.get_template('add_product.html')
    
    context ={
            'categorylist': prod_cat,
            'msg':msg,
        }
    return HttpResponse(template.render(context,request))

def addtocart(request,id):
    if 'user' in request.session:
        cart_user = request.session['user']
        cart_pro=Cart.objects.filter(cart_user=cart_user, cart_id=id).values()
        if request.method=='POST':
            qty = request.POST['quantity']
        if cart_pro:
            cart=Cart.objects.filter(cart_user=cart_user, cart_id=id)[0]
            cart.cart_quantity+=int(qty)
            cart.save()
        else:
            x = Product.objects.filter(id=id)[0]
            cart=Cart(cart_user=cart_user,cart_id=x.id,cart_name=x.product_name,cart_quantity=1,cart_price=x.product_price,cart_image=x.product_image,cart_disc=x.product_disc,total_price=x.product_price)
            cart.save()
        return HttpResponseRedirect('/shoppy-cart')
    
    else:
        return HttpResponseRedirect('/userlogin')
def cart(request):
    if 'user' not in request.session:
        return HttpResponseRedirect('/userlogin')
    else:
        cart_user = request.session['user']

        if request.method=='POST':
            cart_qty=int(request.POST['cart_qty'])
            cart_id=request.POST['cart_id']
            cart_qc=request.POST['cart_qc']
            if cart_qc=='max':
                cart_qty+=1
            elif cart_qc=='min':
                if cart_qty>1:
                    cart_qty-=1
            
            cart=Cart.objects.filter(id=cart_id)[0]
            cart.cart_quantity=cart_qty
            cart.total_price=cart_qty * cart.cart_price
            cart.save() 
        
        cart = Cart.objects.filter(cart_user=cart_user).order_by('-id').values()
        cart2 = Cart.objects.filter(cart_user=cart_user)
        pro_cat = Category.objects.all()
        listcount=Wishlist.objects.filter(list_user=cart_user).values('list_name').count()
        list=Wishlist.objects.filter(list_user=cart_user)
        women_products = Product.objects.filter(product_cat = 3)
        men_products = Product.objects.filter(product_cat = 1)
        cats = Category.objects.values()
        catsno = Product.objects.values('product_cat').count()
        userpic = UserRegistration.objects.filter(user_register_user=request.session['user'])
        total=0
        cartcount=0
        for x in cart2:
            total=total+x.total_price
            cartcount = cartcount+x.cart_quantity
            
        context = {
            'userpic':userpic,
            'cart' : cart,
            'total' : total,
            'pro_cat':pro_cat,
            'cartcount':cartcount,
            'listcount' :listcount,
            'list' :list,
            'women_products':women_products,
            'men_products':men_products,
            'cats':cats,
            'catsno' :catsno,
            'cart_user':cart_user,
        } 
        template=loader.get_template("cart.html")
        return HttpResponse(template.render(context,request))
    
def delfromcart(request,id):
    cart=Cart.objects.filter(id=id)[0]
    cart.delete()
    return HttpResponseRedirect('/cart')
def delfromcout(request,id):
    cout = Order.objects.filter(id=id)[0]
    cout.delete()
    return HttpResponseRedirect('/check-out/')
def delallcart(request):
    cart=Cart.objects.all()
    cart.delete()
    template=loader.get_template("pcout.html")
    return HttpResponse(template.render({},request))
def delallcout(request):
    co=Order.objects.all()
    co.delete()
    template=loader.get_template("cfm_ordr.html")
    return HttpResponse(template.render({},request))


def addtolist(request,id):
    if 'user' not in request.session:
        return HttpResponseRedirect('/userlogin')
       
    else:   
        list_user = request.session['user']
        product =Product.objects.all() 
        list=Product.objects.filter(id=id)[0]
        wishlist=Wishlist(list_user=list_user,list_name=list.product_name,list_image = list.product_image,list_price=list.product_price,list_id = list.id)
        wishlist.save()
    return HttpResponseRedirect('/wishlist')

def wishlist(request):
    if 'user' not in request.session:
        return HttpResponseRedirect("/userlogin")
    else:
        list_user = request.session['user']  
    list=Wishlist.objects.filter(list_user=list_user)
    userpic = UserRegistration.objects.filter(user_register_user=request.session['user'])
    pro_cat = Category.objects.all()
    listcount=Wishlist.objects.filter(list_user=list_user).values('list_name').count()
    women_products = Product.objects.filter(product_cat = 3)
    men_products = Product.objects.filter(product_cat = 1)
    cats = Category.objects.values()
    catsno = Product.objects.values('product_cat').count()
    cart = Cart.objects.filter(cart_user=list_user).order_by('-id').values()
    cart2 = Cart.objects.filter(cart_user=list_user)
    total=0
    cartcount=0
    for x in cart2:
        total=total+x.total_price 
        cartcount = cartcount+x.cart_quantity 
    context = {
        
    } 
    context = {
    'list' : list,
    'pro_cat' : pro_cat,
    'userpic' : userpic,
    'cart' : cart,
    'total' : total,
    'pro_cat':pro_cat,
    'cartcount':cartcount,
    'listcount' :listcount,
    'women_products':women_products,
    'men_products':men_products,
    'cats':cats,
    'catsno' :catsno,
    'cart_user':list_user,
    }
    template=loader.get_template("wishlist.html")
    return HttpResponse(template.render(context,request))

def delfromlist(request,id):
    list=Wishlist.objects.filter(id=id)[0]
    list.delete()
    return HttpResponseRedirect('/wishlist')

def checkout(request):
    if 'user' not in request.session:
        return HttpResponseRedirect('/userlogin')
    else:
        current_user = request.session['user']

    if request.method=='POST':
        if 'delvry_address' in request.POST:
            order=Order.objects.filter(current_user=current_user)
            for x in order:
                x.delvry_fname=request.POST['delvry_fname']
                x.delvry_lname=request.POST['delvry_lname']
                x.delvry_mail=request.POST['delvry_mail']
                x.delvry_phone=request.POST['delvry_phone']
                x.delvry_address=request.POST['delvry_address']
                x.delvry_upi=request.POST['delvry_upi']
                x.delvry_type=request.POST['delvry_type']
                x.save()
            
        else:
            carts=Cart.objects.filter(cart_user = current_user)
            for x in carts:
                orders=Order(
                    o_product_name=x.cart_name, 
                    o_product_image=x.cart_image, 
                    o_product_qty=x.cart_quantity,
                    o_product_price=x.cart_price,
                    o_product_total=x.total_price,
                    current_user=x.cart_user,
                )
                orders.save()
        return HttpResponseRedirect('/checkout')
    
    userpic = UserRegistration.objects.filter(user_register_user=request.session['user'])
    pro_cat = Category.objects.all()
    order=Order.objects.filter(current_user = current_user)
    total=0
    for x in order:
        total = total + x.o_product_total 

    context = {
        'order' : order,
        'total' : total,
        'userpic':userpic,
        'pro_cat':pro_cat,
    }

    template=loader.get_template("checkout.html")
    return HttpResponse(template.render(context,request))
def deleteorder(request,id):
    order=Order.objects.filter(id=id)[0]
    order.delete()
    return HttpResponseRedirect('/checkout/')
def search(request):
    search=request.GET['search']
    search=Product.objects.filter(product_name__contains=search)
    context = {
        'search' : search,
    }
    template=loader.get_template("search.html")
    return HttpResponse(template.render(context,request))

def order_confirm(request):
    if 'user' not in request.session:
        return HttpResponseRedirect('/userlogin')
    else:
         current_user= request.session['user']

    order=Order.objects.filter(current_user = current_user)

    total=0
    for x in order:
        total = total + x.o_product_total * x.o_product_qty
        address = x.delvry_address
        del_type = x.delvry_type

    context = {
        'order' : order,
        'total' : total,
        'address' : address,
        'del_type' : del_type,
    }
 
    template=loader.get_template("confirm_order.html")
    return HttpResponse(template.render(context,request))
def confirmed(request):
     if 'user' not in request.session:
        return HttpResponseRedirect('/userlogin')
     else:
        current_user= request.session['user']
        order=Order.objects.filter(current_user=current_user)
        purchase = Purchased.objects.filter(current_user=current_user)
        if request.method=='POST':
            for x in order:
                    purchase = Purchased (
                    delvry_address = x.delvry_address,
                    delvry_type = x.delvry_type,
                    p_product_name=x.o_product_name, 
                    p_product_image=x.o_product_image, 
                    p_product_qty=x.o_product_qty,
                    p_product_price=x.o_product_price,
                    p_product_total=x.o_product_total,
                    current_user=x.current_user,
                    )
                    purchase.save()

     template=loader.get_template("confirmed.html")
     return HttpResponse(template.render({},request))


def loginn(request):
    template=loader.get_template("loginn.html")
    return HttpResponse(template.render({},request))
def contact(request):
    template=loader.get_template("contact.html")
    return HttpResponse(template.render({},request))
def shoppingcart(request):
    template=loader.get_template("shopping-cart.html")
    return HttpResponse(template.render({},request))
def shop(request):
    template=loader.get_template("shop.html")
    return HttpResponse(template.render({},request))
def check_out(request):
    template=loader.get_template("check-out.html")
    return HttpResponse(template.render({},request))
def reg(request):
    template=loader.get_template("register.html")
    return HttpResponse(template.render({},request))
def pindex(request):
    template=loader.get_template("p_index.html")
    return HttpResponse(template.render({},request))
def ownindex(request):
    template=loader.get_template("own_index.html")
    return HttpResponse(template.render({},request))
def pd(request,id):


    if 'user' not in request.session:
        return HttpResponseRedirect('/userlogin')
    cuser = request.session['user']
    cprod = Product.objects.filter(product_id=id).all()
    cprods = Product.objects.filter(product_id=id)
    pro_cat = Category.objects.all()
    cart_user = request.session['user']
    listcount=Wishlist.objects.filter(list_user=cart_user).values('list_name').count()
    cart = Cart.objects.filter(cart_user=cart_user).order_by('-id').values()
    cart2 = Cart.objects.filter(cart_user=cart_user)
    list=Wishlist.objects.filter(list_user=cart_user)
    women_products = Product.objects.filter(product_cat = 3)
    men_products = Product.objects.filter(product_cat = 1)
    ids = [43,44,40,41,52,45]
    m_p = Product.objects.filter(id__in=ids)
    eid = [46,50,49,47,51,48]
    e_c = Product.objects.filter(id__in=eid)
    cats = Category.objects.all()
    products = Product.objects.all()
    count = []
    for x in cats:
        catnos = Product.objects.filter(product_cat=x.id).values().count()
        count.append(catnos)

    total=0
    cartcount=0
    for x in cart2:
        total=total+x.total_price 
        cartcount = cartcount+x.cart_quantity 
        
    if request.method=='POST':
        qty = request.POST['quantity']
    
    for x in cprod:
        cat = Category.objects.filter(cat_product_no = x.product_cat )
    context = {
        'product' : cprods,
        'cat' :cat,
        'cart' : cart,
            'total' : total,
            'pro_cat':pro_cat,
            'cartcount':cartcount,
            'listcount' :listcount,
            'm_p':m_p,
            'e_c':e_c,
            'list' :list,
            'women_products':women_products,
            'men_products':men_products,
            'cats':cats,
            'catsno' :count,
            'cart_user':cart_user,
            'products' :products,
            'catnos' :catnos,
    }
    
    template=loader.get_template("pd.html")
    return HttpResponse(template.render(context,request))

def pcart(request):
    request.session['logs'] = []
    if 'user' not in request.session:
        return HttpResponseRedirect('/userlogin')
    else:
        cart_user = request.session['user']
        apply_coupon=0
        distotal=0
        gtotal=0
        pid=""

        if request.method=='POST':
             if 'carto' in request.POST:
                cart_qty=int(request.POST['cart_qty'])
                cart_id=request.POST['cart_id']
                cart_qc=request.POST['cart_qc']
                if cart_qc=='max':
                    cart_qty+=1
                elif cart_qc=='min':
                    if cart_qty>1:
                        cart_qty-=1
                
                cart=Cart.objects.filter(id=cart_id)[0]
                cart.cart_quantity=cart_qty
                cart.total_price=cart_qty * cart.cart_price
                cart.save() 
             if 'coupon' in request.POST:
                apply_coupon = request.POST['coupon_code']

        cart = Cart.objects.filter(cart_user=cart_user).order_by('-id').values()
        cart2 = Cart.objects.filter(cart_user=cart_user)
        pro_cat = Category.objects.all()
        listcount=Wishlist.objects.filter(list_user=cart_user).values('list_name').count()
        list=Wishlist.objects.filter(list_user=cart_user)
        women_products = Product.objects.producto = Product.objects.all()
        men_products = Product.objects.filter(product_cat = 1)
        cats = Category.objects.values()
        catsno = Product.objects.values('product_cat').count()
        
        producto = Product.objects.all()
        userpic = UserRegistration.objects.filter(user_register_user=request.session['user'])
        total=0
        cartcount=0
        for x in cart2:
            total=total+x.total_price
            cartcount = cartcount+x.cart_quantity
            pid = x.cart_id
        if apply_coupon == "WINTERSHOPPY":
            request.session['logs'] = "1"
            distotal = total*0.10
            gtotal = total-distotal

        else:
            request.session['logs'] = "0"
            gtotal = total
        context = {
            'userpic':userpic,
            'cart' : cart,
            'total' : total,
            'pro_cat':pro_cat,
            'cartcount':cartcount,
            'listcount' :listcount,
            'list' :list,
            'women_products':women_products,
            'men_products':men_products,
            'cats':cats,
            'catsno' :catsno,
            'cart_user':cart_user,
            'producto':producto,
            'distotal':distotal,
            'gtotal':gtotal,
        } 
    template=loader.get_template("pcart.html")
    return HttpResponse(template.render(context,request))

def deldis(request):
    request.session['logs'] = "0"
    return HttpResponseRedirect('/check-out/')

def pout(request):
    if 'user' not in request.session:
        return HttpResponseRedirect('/userlogin')
    else:
        distotal=0
        gtotal =0
        current_user = request.session['user']

        if request.method=='POST':
            if 'delvry_address' in request.POST:
                order=Order.objects.filter(current_user=current_user)
                for x in order:
                    x.delvry_fname=request.POST['delvry_fname']
                    x.delvry_lname=request.POST['delvry_lname']
                    x.delvry_mail=request.POST['delvry_mail']
                    x.delvry_phone=request.POST['delvry_phone']
                    x.delvry_address=request.POST['delvry_address']
                    x.delvry_upi=request.POST['delvry_upi']
                    x.delvry_type=request.POST['delvry_type']
                    x.save()
                
            else:
                carts=Cart.objects.filter(cart_user = current_user)
                for x in carts:
                    orders=Order(
                        o_product_name=x.cart_name, 
                        o_product_image=x.cart_image, 
                        o_product_qty=x.cart_quantity,
                        o_product_price=x.cart_price,
                        o_product_total=x.total_price,
                        current_user=x.cart_user,
                    )
                    orders.save()
            return HttpResponseRedirect('/check-out/')
        
    userpic = UserRegistration.objects.filter(user_register_user=request.session['user'])
    pro_cat = Category.objects.all()
    order=Order.objects.filter(current_user = current_user)
    total=0
    for x in order:
        total = total + x.o_product_total 
    if request.session['logs']=="1":
         distotal = total*0.10
         gtotal = total-distotal
    else:
        gtotal =total
    context = {
        'order' : order,
        'total' : total,
        'userpic':userpic,
        'pro_cat':pro_cat,
        'distotal':distotal,
        'gtotal':gtotal,
    }

    
    template=loader.get_template("pcout.html")
    return HttpResponse(template.render(context,request))

def cnodr(request):
    address = ""
    del_type = ""
    delvry_fname = ""
    delvry_lname = ""
    delvry_mail =""
    delvry_phone = ""
    if 'user' not in request.session:
        return HttpResponseRedirect('/userlogin')
    else:
         current_user= request.session['user']
         if request.method=='POST':
            if 'delvry_address' in request.POST:
                order=Order.objects.filter(current_user=current_user)
                for x in order:
                    x.delvry_fname=request.POST['delvry_fname']
                    x.delvry_lname=request.POST['delvry_lname']
                    x.delvry_mail=request.POST['delvry_mail']
                    x.delvry_phone=request.POST['delvry_phone']
                    x.delvry_address=request.POST['delvry_address']  
                    
                    x.delvry_type=request.POST['delvry_type']
                    x.save()
                
            else:
                carts=Cart.objects.filter(cart_user = current_user)
                for x in carts:
                    orders=Order(
                        o_product_name=x.cart_name, 
                        o_product_image=x.cart_image, 
                        o_product_qty=x.cart_quantity,
                        o_product_price=x.cart_price,
                        o_product_total=x.total_price,
                        current_user=x.cart_user,
                    )
                    orders.save()


    orderz=Order.objects.filter(current_user = current_user)

    total=0
    for x in orderz:
        total = total + x.o_product_total * x.o_product_qty
        address = x.delvry_address
        del_type = x.delvry_type
        delvry_fname = x.delvry_fname
        delvry_lname = x.delvry_lname
        delvry_mail = x.delvry_mail
        delvry_phone = x.delvry_phone



    
    context = {
        'order' : orderz,
        'total' : total,
        'delvry_address': address,
        'del_type' : del_type,
        'delvry_fname':delvry_fname,
        'delvry_phone':delvry_phone,
        'delvry_mail':delvry_mail,
        'delvry_lname':delvry_lname,
        
        
    }
 
    
    template=loader.get_template("cfm_ordr.html")
    return HttpResponse(template.render(context,request))

def adminlogin(request):
    if 'admin' in request.session:
        return HttpResponseRedirect("adminproducts")
    if 'user' in request.session:
        return HttpResponseRedirect('useraccount/')
    if request.method=='POST':
        username=request.POST['user']
        password=request.POST['pass']
        if username=='sree' and password=='123456':
            request.session['admin']=username
            return HttpResponseRedirect("adminproducts")
        else:
            return HttpResponseRedirect("adminlogin?inv=1")
    template=loader.get_template("adminlogin.html")
    return HttpResponse(template.render({},request))

def adminproducts(request):
    if 'admin' not in request.session:
        return HttpResponseRedirect("adminlogin")
    else:
        adminuser = request.session['admin']
        products = Product.objects.all().order_by('-id').values()
        cats = Category.objects.all()

           
        #create context for pass to template
        context = {
            'products' : products,
            'cats' : cats
        } 
        template=loader.get_template("adminproducts.html")
        return HttpResponse(template.render(context,request))

def admineditprod(request,id):
    if request.method=='POST':
            id=request.POST['id']
            product_name=request.POST['product_name']
            product_price=request.POST['product_price']
            product_cat=request.POST['product_cat']
            prod = Product.objects.filter(id=id)[0]
            prod.product_name=product_name
            prod.product_price=product_price
            prod.product_cat=product_cat

            if len(request.FILES) != 0:
                product_image=request.FILES['product_image']
                prod.product_image=request.FILES['product_image']
            prod.save()
            return HttpResponseRedirect("/adminproducts")  
        
    product=Product.objects.filter(id=id)[0]
    cat=Category.objects.all()
    context={
        'product': product,
        'cat':cat
    }
    template=loader.get_template("admineditprod.html")
    return HttpResponse(template.render(context,request))

def admindelprod(request,id):
    product=Product.objects.filter(id=id)[0]
    product.delete()
    return HttpResponseRedirect('/adminproducts')

def adminlogout(request):
    del request.session["admin"]
    return HttpResponseRedirect("adminlogin")

def cateditprod(request,id):
    if request.method=='POST':
            id=request.POST['id']
            cat_name=request.POST['cat_name']
            cat_product_no=request.POST['cat_product_no']
            catz = Category.objects.filter(id=id)[0]
            catz.cat_name = cat_name
            catz.cat_product_no = cat_product_no

            if len(request.FILES) != 0:
                cat_image=request.FILES['cat_image']
                catz.cat_image = request.FILES['cat_image']
                catz.save()
            return HttpResponseRedirect("/adminproducts")  
        
    product=Product.objects.filter(id=id)[0]
    cat=Category.objects.filter(id=id)[0]
    context={
        'product': product,
        'cat':cat
    }
    template=loader.get_template("cateditprod.html")
    return HttpResponse(template.render(context,request))

def catdelprod(request,id):
    catd=Category.objects.filter(id=id)[0]
    catd.delete()
    return HttpResponseRedirect('/adminproducts')

def purchased(request):
   address=""
   dtype=""
   if 'user' not in request.session:
        return HttpResponseRedirect('/userlogin')
   else:
        current_user= request.session['user']
        order=Order.objects.filter(current_user=current_user)
       
        purchsd=Purchased.objects.filter(current_user = current_user)
        total=0
        for x in purchsd:
                total = total + x.p_product_total * x.p_product_qty
                address = x.delvry_address
                dtype = x.delvry_type

        context = {
                'purchsd' : purchsd,
                'total' : total,
                'address' : address,
                'dtype' : dtype,
            }

   template=loader.get_template("purchase.html")
   return HttpResponse(template.render(context,request))
# Create your views here.
