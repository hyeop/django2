from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User
from django.contrib.auth.hashers import check_password
from django.contrib import messages
# Create your views here.

def chpass(request):
    u = request.user
    cp = request.POST.get("cpass")
    if check_password(cp, u.password):
        np = request.POST.get("npass")
        u.set_password(np)
        u.save()
        return redirect("acc:login")
    return redirect("acc:update")

def update(request):
    if request.method == "POST":
        u = request.user
        uco = request.POST.get("ucomm")
        upi = request.FILES.get("upic")
        uma = request.POST.get("umail")
        u.comment, u.email = uco, uma
        if upi:
            u.pic.delete()
            u.pic = upi
        u.save()
        return redirect("acc:profile")

    return render(request, "acc/update.html")

def signup(request):
    if request.method == "POST":
        una = request.POST.get("uname")
        upa = request.POST.get("upass")
        uco = request.POST.get("ucomm")
        upi = request.FILES.get("upic")
        uag = request.POST.get("uage")
        uma = request.POST.get("umail")
        try:
            User.objects.create_user(username=una, password=upa, comment=uco, pic=upi, age=uag, email=uma)
            return redirect("acc:login")
        except:
            pass # 메세지 넣을곳
    return render(request, "acc/signup.html")

def delete(request):
    request.user.pic.delete()
    request.user.delete()
    return redirect("acc:index")

def index(request):
    d = {1:"one", 2:"two", 3:"three"}
    context = {
        "d" : d
    }
    return render(request, "acc/index.html", context)

def profile(request):
    return render(request, "acc/profile.html")

def ulogout(request):
    logout(request)
    return redirect("acc:index")

def ulogin(request):
    if request.method == "POST":
        un = request.POST.get("uname")
        up = request.POST.get("upass")
        u = authenticate(username=un, password=up)
        if u:
            login(request, u)
            messages.success(request, f"{u} 님 환영합니다!")
            return redirect("acc:index")
        else:
            messages.info(request, "계정정보가 일치하지않습니다")
    return render(request, "acc/login.html")