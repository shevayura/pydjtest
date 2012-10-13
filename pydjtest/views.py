from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from django.core.paginator import Paginator
from django.template import RequestContext
from django import template
from django.template.response import TemplateResponse

from easy_thumbnails.files import get_thumbnailer
import json

from pydjtest import models, admin, forms, middlewares


def productList(request, page=1):
    page = int(page) #escape
    products = models.Products.objects.all()
    paginator = Paginator(products, 2)
    try:
        products = paginator.page(page)
    except:
        raise Http404

    return TemplateResponse(request, 'list.html', {'products': products, 'main_active':1})


def productPage(request, alias):
    try:
        product = models.Products.objects.get(alias=alias)
    except:
        product = None
    if not product:
        raise Http404
    
    return TemplateResponse(request, 'product.html', {'product': product})

def productEdit(request, id):
    if not request.user.is_active or not request.user.is_superuser:
        raise Http404 #filter other users
    try:
        id = int(id)
        product = models.Products.objects.get(id=id)
    except:
        raise Http404 #bad id or product with this id is not exist

    form = None

    if request.method == 'POST':
        response = {}
        saved    = False
        form = forms.ProductForm(request.POST, request.FILES, instance=product)
        #check form
        if form.is_valid():
            form.save()
            response['status'] = 'ok'
            saved = True
        else:
            response['status'] = 'error'

        context = RequestContext(request, { 'product':product, 'form':form, 'saved':saved })
        response['form'] = template.loader.get_template('form.html').render(context)
        response['name'] = product.name
        resp = TemplateResponse(request, '')
        resp.content = json.dumps(response)
        return resp
        #return HttpResponse(json.dumps(response))

    if request.method == 'GET':
        #create form
        form = forms.ProductForm(instance=product)
        return TemplateResponse(request, 'edit.html', {"form": form, 'product': product})
