
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from shop.models import Catergory,Products

def categories(request):
   c=Catergory.objects.all()
   context={'cat':c}
   return  render(request,'categories.html',context)

def products(request,p):
   c=Catergory.objects.get(id=p)
   p=Products.objects.filter(catergory=c)
   context={'categories':c,'products':p}
   return render(request,'products.html',context)
def details_products(request,p):
   pro=Products.objects.get(id=p)
   context={'products':pro}
   return render(request,'details.html',context)


def register(request):
   if (request.method == "POST"):
      u = request.POST['u']
      p = request.POST['p']
      cp = request.POST['cp']
      fn = request.POST['fn']
      ln = request.POST['ln']
      e = request.POST['e']
      if (cp==p):
          u=User.objects.create_user(username=u,password=p,email=e,first_name=fn,last_name=ln)
          u.save()
          return redirect('shop:categories')

   return render(request,'register.html')


def user_login(request):
   if (request.method == "POST"):
      u = request.POST['u']
      p = request.POST['p']
      user = authenticate(username=u, password=p)
      if user:
         login(request, user)
         return redirect('shop:categories')
      else:
         return HttpResponse("invalid credentials")

   return render(request, 'login.html')


def user_logout(request):
   logout(request)
   return redirect('shop:login')
def add_categories(request):
   if (request.method=="POST"):
      n=request.POST['n']
      i=request.FILES['i']
      d=request.POST['d']
      c=Catergory.objects.create(name=n,image=i,desc=d)
      c.save()
      return redirect('shop:categories')
   return render(request,'add_categories.html')
def add_products(request):
   if(request.method=="POST"):
      n=request.POST['n']
      i=request.FILES.get('i')
      d=request.POST['d']
      s=request.POST['s']
      p=request.POST['p']
      c=request.POST['c']
      cat=Catergory.objects.get(name=c)
      p=Products.objects.create(name=n,image=i,desc=d,stock=s,price=p,catergory=cat)
      p.save()
      return redirect('shop:categories')
   return render(request,'add_products.html')
def addstock(request,p):
   product=Products.objects.get(id=p)
   if(request.method=="POST"):
      product.stock=request.POST['n']
      product.save()
      return redirect('shop:details',p)
   context={'pro':product}
   return render(request,'addstock.html',context)