from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.core.paginator import Paginator

from pydjtest import models, admin


def productList(request, page=1):
    page = int(page)
    products = models.Products.objects.all()
    paginator = Paginator(products, 2)
    try:
        products = paginator.page(page)
    except:
        raise Http404

    context = {}
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

    return render_to_response('product.html', {"product": product})

