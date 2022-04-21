from django.shortcuts import render,redirect
from .models import Category,Product
from django.contrib import messages
# Create your views here.




def collections(request):
    category = Category.objects.filter(status=0)
    context = {'category': category}
    return render(request, 'store/collections.html', context)

def collectionsview(request, slug):
    if(Category.objects.filter(slug=slug,status =0)):
         products = Product.objects.filter(category__slug = slug)
         category = Category.objects.filter(slug=slug).first()
         context = {'products': products, 'category': category}
         return render (request, 'store/products/index.html',context)
    else:
        messages.warning(request, 'Category ga ada')
        return redirect('collections')

def productview(request, cate_slug, prod_slug):
    if(Category.objects.filter(slug=cate_slug,status =0)):
         if(Product.objects.filter(slug=prod_slug,status =0)):
             products = Product.objects.filter(slug= prod_slug, status =0).first
             context = {'products': products}
         else:
             messages.warning(request, 'Product ga ada')
             return redirect('collections')
    else:
        messages.warning(request, 'category ga ada')
        return redirect('collections')
    return render (request, 'store/products/view.html',context)