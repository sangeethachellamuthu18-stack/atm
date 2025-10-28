from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from . import models

def Loginpage(request):
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")

        user=models.RegisterPage.objects.all.filter(email=email,password=password).first()
        if user:
            messages.success(request,"login sucessfully")
            return redirect("Dashboard")
        else:
            messages.error(request,"incorrect email or password")
            return render(request,"atm/login.html")

    return render(request,"atm/login.html")

def Registerpage(request):
    if request.method=="POST":
        firstname=request.POST.get("firstname")
        lastname=request.POST.get("lastname")
        email=request.POST.get("email")
        account_number=request.POST.get("account_number")
        balance=request.POST.get("balance")
        password=request.POST.get("password")
        re_enter_password=request.POST.get("re_enter_password")

        if password != re_enter_password:
            messages.error(request,"password does not match")
            return render(request,"atm/signup.html")
        
        if firstname and email and account_number and balance and password and re_enter_password:
            models.RegisterPage.objects.create(
                firstname=firstname,
                lastname=lastname,
                email=email,
                account_number=account_number,
                balance=balance,
                password=password
            )
            messages.success(request,"registration sucessfull")
            return redirect('Loginpage')
        else:
            messages.error(request,"All fields are required")
            return render(request,"atm/signup.html")    
    return render(request,"atm/signup.html") 

def Dashboard(request):
    user=models.RegisterPage.objects.all()


    return render(request,'atm/dashboard.html',{'user':user})
