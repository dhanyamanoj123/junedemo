from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
def home(request):
    return render(request,'home.html')
from books.models import Book
@login_required
def viewsbooks(request):
    # k=con.execute('select * from Book')
    # k=modelname.objects.all()
    b=Book.objects.all() #reads all records from the book table
    context={'book':b}#sends data from view function to html page
    return render(request,'viewsbooks.html',context)
@login_required
def addbooks(request):
    if(request.method=="POST"):
        t=request.POST['t']
        a=request.POST['a']
        p=request.POST['p']
        pa=request.POST['pa']
        l=request.POST['l']
        c=request.FILES['c']
        f=request.FILES['f']
        b=Book.objects.create(title=t,author=a,price=p,pages=pa,language=l,cover=c,pdf=f)
        b.save()
        return viewsbooks(request)

    return render(request,'addbooks.html')
def book(request,p):
    b=Book.objects.get(id=p)
    context={'book':b}

    return render(request,'book.html',context)
def delete(request,p):

     b=Book.objects.get(id=p)
     b.delete()
     return redirect('books:viewsbooks')

def edit(request,p):
     b=Book.objects.get(id=p)

     if(request.method=="POST"):
      b.title=request.POST['t']
      b.author=request.POST['a']
      b.price=request.POST['p']
      b.pages = request.POST['pa']
      b.language = request.POST['l']
      if(request.FILES.get('i')==None):
          b.save()
      else:
          b.cover=request.FILES.get('i')
      if (request.FILES.get('f') == None):
          b.save()
      else:
          b.pdf = request.FILES.get('f')
          b.save()
          return redirect('books:viewsbooks')

     context = {'book': b}
     return render(request,'edit.html',context)