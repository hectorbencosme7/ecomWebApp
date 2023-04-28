from django.shortcuts import render
from .models import products,orders
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    allProducts = products.objects.all()

    search = request.GET.get('searchbox')
    if search != '' and search is not None:
        allProducts = allProducts.filter(title__icontains=search)

    paginator = Paginator(allProducts,4)
    page = request.GET.get('page')
    allProducts = paginator.get_page(page)
    return render(request,'shop/index.html',{'products':allProducts})

def detail(request,id):
    product = products.objects.get(id=id)
    return render(request,'shop/detail.html',{'product':product})

def chekout(request):

    if request.method == "POST":
        items=request.POST.get('items',"")
        name=request.POST.get('name',"")
        email=request.POST.get('email',"")
        address=request.POST.get('address',"")
        city=request.POST.get('city',"")
        state=request.POST.get('state',"")
        zipcode=request.POST.get('zip',"")
        total=request.POST.get('total',"")

        order = orders(items=items,name=name,email=email,address=address,city=city,state=state,zipcode=zipcode,total=total)
        order.save()
    return render(request,'shop/checkout.html',{})
