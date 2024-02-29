from django.shortcuts import render,redirect
from.models import*
from django.core.files.storage import default_storage
from django.http import HttpResponse
from django.contrib.auth.models import User  
# Create your views here.
def index (request):
 return render(request,"index.html")

def Login (request):
    msg=""
    print("hello")
    if request.POST:
            email=request.POST["eml"]
            password=request.POST["psd"]
            if login.objects.filter(l_email=email,l_password=password):
                data=login.objects.get(l_email=email,l_password=password)
                print(data)
                if data:
                    if data.l_status=="pending":
                        msg="you are not approved"
                        print(msg)
                    elif data.l_status=="reject":
                        msg="you are rejected"
                        print(msg)
                    else:
                        msg="login sucess"
                        print(msg)
                        # request.session['user_id'] = login.pk
                        if data.l_type=="user":
                            return redirect("/shopview")               
                        elif data.l_type=="shop":
                            return redirect("/rescommon")  
                else: 
                    msg="data not found"
                    print(msg)  
            else:       
                msg="invalid email/password"
                print(msg)
    return render(request,"login.html",{"msg":msg})
    
    
    
def Register (request):
    msg=""
    if request.POST:
        fname=request.POST["fname"]
        lname=request.POST["lname"]
        phone=request.POST["phn"]
        email=request.POST["eml"]
        password=request.POST["psd"]
        if login.objects.filter(l_email=email).exists():
            msg="already exist"
            print(msg)
        else:
            logQry=login.objects.create(l_email=email,l_password=password,l_type="user",l_status="approved")
            logQry.save()
            reQry=register.objects.create(Email=email,Fname=fname,Lname=lname,Phone=phone,Loginid=logQry)
            reQry.save()
            msg="password does not match"
        
    return render(request,"register.html")

def shopreg(request):   
    msg=""
    if request.POST:
        rname=request.POST["rname"]
        phone=request.POST["phn"]
        email=request.POST["eml"]
        rlnum=request.POST["rlnum"]
        address=request.POST["addrs"]
        password=request.POST["psd"]
        image=request.FILES['image']
        if login.objects.filter(l_email=email).exists():
            msg="already exist"
            print(msg)
        else:
            
            logQry=login.objects.create(l_email=email,l_password=password,l_type="shop",l_status="approve")
            logQry.save()
            
                
            regQry=resreg.objects.create(rname=rname,phone=phone, email=email,rimage=image,reslic=rlnum,address=address,resid=logQry)
            regQry.save()
        msg="SUCCESSFULLY REGISTERED "    
        
        
    return render(request,"shopereg.html",{"msg":msg} )

def rescommon(request): 

    return render(request, 'restaurent/rescommon.html')
    
def addproduct (request):
    msg=""
    if request.POST:
        pname=request.POST['pname']
        price=request.POST['price']
        disc=request.POST['desc']
        image= request.FILES['img']

        proQry=product.objects.create(pname=pname,price=price,pimage=image,disc=disc)
        proQry.save()
    else: 
        msg="invalid data" 
        print(msg)   
    
    return render(request,'restaurent/addproduct.html')

def editproduct(request):
     uid=request.GET.get('uid')
     update=product.objects.filter(id=uid)
     if request.POST:
            name=request.POST['pname']
            price = request.POST["price"]
            disc = request.POST["desc"]
           
            
            
        
            updQry=product.objects.filter(id=uid).update(
                pname=name,
                price=price,
                disc=disc,
                
                
            
        )
            return redirect('/viewpro')
     return render(request,'restaurent/edit.html',{'edit':update})
     

def viewpro(request):
    userdata=product.objects.all()
    print(userdata)
    return render(request,'restaurent/viewpro.html',{"userdata":userdata})

def delet(request):
    uid=request.GET.get('uid')
    delet=product.objects.filter(id=uid).delete()
    
    return redirect('/viewpro')

def shopview(request):
    shopdata=resreg.objects.all()
    print (shopdata)
    return render (request,'shopview.html',{'shopview':shopdata})

# def rdelet(request):
#     uid=request.GET.get('uid')
#     delet=resreg.objects.filter(id=uid).delete()
#     return redirect('/shopview')
   
def cview (request) :
    viewdata=product.objects.all()
    print(viewdata)
    return render (request,'cviewpro.html',{'view':viewdata})       