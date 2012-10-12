from django import template
register = template.Library()


from pydjtest.models import Products
import random

@register.tag
def rand_products(parser, token):
    count = 0
    try:
        tag_name, count = token.split_contents()
        count = count.strip(' "')
        if not count:
            count = 0
        count = int(count)
    except ValueError:
        msg = '%r tag requires a single integer argument' % token.contents[0]
        raise template.TemplateSyntaxError(msg)

    return RandProductsNode(count)

class RandProductsNode(template.Node):

    def __init__(self, count):
        self.count = count if count > 0 else 1

    def render(self, context):
        # get all ids
        ids = []
        for p in Products.objects.all():
            if p.id == context['product'].id: continue
            ids.append(p.id)

        products = []
        for i in range(self.count):
            if not len(ids):
                break
            id = ids.pop(random.randint(0, len(ids)-1))
            products.append(Products.objects.get(id=id))

        context['rand_products'] = products

        return ''