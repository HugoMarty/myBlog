from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
# Create your views here.
from .models import *
def Index(request):
    return render(request,'bindex.html')

def Login(request):
    if request.method=='GET':
        return render(request,'login_Page.html')
    else:
        name=request.POST.get('uname',0)
        pwd=request.POST.get('upwd',0)
        if User.objects.filter(username=name,password=pwd):
            return redirect('indexPage')
        else:
            return HttpResponse('登录失败')
def Register(request):
    if request.method=='GET':
        return render(request,'register_Page.html')
    else:
        name=request.POST.get('uname',0)
        pwd=request.POST.get('upwd',0)
        if User.objects.filter(username=name):
            return HttpResponse("用户名已存在")
        user=User(username=name)
        user.password=pwd
        user.save()
        return render(request,'index.html')