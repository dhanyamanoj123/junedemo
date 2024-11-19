from django.shortcuts import render
from shop.models import Products

from django.db.models import Q
def search_products(request):
     if(request.method=="POST"):
          query=request.POST['q']
          if query:
             p=Products.objects.filter(Q(name__icontains=query) | Q(desc__icontains=query))
             context={'pro':p,'query':query}#filter the records matching with query
     return render(request,'search.html',context)