from django.shortcuts import render, redirect
from .forms import AddProductForm
from .models import Product
# Create your views here.
def product_list(request):
    context = {'product_list': Product.objects.all() }
    return render(request, "add_product/product_list.html", context)



def product_form(request, id=0):
    if request.method == "GET": 
        if id == 0:
            form = AddProductForm()
        else:
            product = Product.objects.get(pk=id)
            form = AddProductForm(instance=product)
        return render(request, "add_product/product_form.html", {'form':form})

    else:
        if id == 0:

            form = AddProductForm(request.POST)
        else:
            product = Product.objects.get(pk=id)
            form = AddProductForm(request.POST,instance= product)
        if form.is_valid():
            form.save()
        return redirect('/product/list')




def product_delete(request, id):
    product = Product.objects.get(pk=id)
    product.delete()
    return redirect('/product/list')
