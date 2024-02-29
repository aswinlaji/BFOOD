from django.db import models

# Create your models here.

class login(models.Model):
    l_email=models.CharField(max_length=50,null=True)
    l_password=models.CharField(max_length=50,null=True)
    l_type=models.CharField(max_length=50,null=True)
    l_status=models.CharField(max_length=50,null=True)
    
class register(models.Model):
    Fname=models.CharField(max_length=50,null=True)
    Lname=models.CharField(max_length=50,null=True)
    Email=models.CharField(max_length=50,null=True)
    Phone=models.CharField(max_length=50,null=True)
    Loginid=models.ForeignKey(login,on_delete=models.CASCADE,null=True)
    
class resreg(models.Model):
    rname=models.CharField(max_length=50,null=True)
    phone=models.CharField(max_length=50,null=True)
    email=models.CharField(max_length=50,null=True)
    address=models.CharField(max_length=50,null=True)
    reslic=models.CharField(max_length=50,null=True)
    rimage=models.ImageField(null=True,upload_to="images/")
    resid=models.ForeignKey(login,on_delete=models.CASCADE,null=True)
    
class product(models.Model):
    pname=models.CharField(max_length=50,null=True)
    price=models.CharField(max_length=50,null=True)
    pimage=models.ImageField(null=True,upload_to="images/")
    disc=models.CharField(max_length=200,null=True)    
    
    
    
    
        
    
