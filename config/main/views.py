from django.shortcuts import render
from .models import Product
from django.conf.urls.static import static
def home(request):
    products=Product.objects.all()
    context={
        'products':products
    }
    return render(request,'home.html',context)
