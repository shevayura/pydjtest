from django.http import Http404
from django.shortcuts import render_to_response
from django.core.paginator import Paginator
from django.template import RequestContext

from pydjtest import models, admin, forms


def productList(request, page=1):
    page = int(page)
    products = models.Products.objects.all()
    paginator = Paginator(products, 2)
    try:
        products = paginator.page(page)
    except:
        raise Http404

    context = RequestContext(request, {})
    context['products']    = products
    context['main_active'] = 1
    return render_to_response('list.html', context)


def productPage(request, alias):
    try:
        product = models.Products.objects.get(alias=alias)
    except:
        product = None
    if not product:
        raise Http404

    context = RequestContext(request, {"product": product})

    return render_to_response('product.html', context)

def productEdit(request, id):
    if not request.user.is_active or not request.user.is_superuser:
        raise Http404 #filter other users
    try:
        id = int(id)
        product = models.Products.objects.get(id=id)
    except:
        raise Http404 #bad id or product with this id is not exist

    form = None
    messages = {'good':[], 'error':[]}

    if request.method == 'POST':
        form = forms.ProductForm(request.POST, request.FILES, instance=product)
        #check form
        if form.is_valid():
            form.save()
            messages['good'].append("Saved!")
        else:
            messages['error'].append("Error in form")

    if request.method == 'GET':
        #create form
        form = forms.ProductForm(instance=product)

    context = RequestContext(request, {
                    "form": form,
                    'product':product,
                    'messages':messages
                    })
                    
    return render_to_response('edit.html', context)
