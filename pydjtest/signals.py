from django.db.models.signals import *
from pydjtest.models import Products
from django import template
from django.core.mail import mail_admins

def product_changed(sender, **kwargs):
    if sender is not Products:
        return #this is not product was changed

    mail_body = ''
    subject   = ''

    f = open("/home/shevayura/qweqwe.txt", 'wb')
    if kwargs['signal'] is post_save:
        #save
        mail_body = template.loader.get_template('signal_save.html').render(template.Context(kwargs))
        subject   = "Product was changed"
    else:
        #delete
        mail_body = template.loader.get_template('signal_delete.html').render(template.Context(kwargs))
        subject   = "Product was deleted"

    if not subject or not mail_body:
        return
    mail_admins(subject, "%s. See html version for details."%subject, fail_silently=True, html_message=mail_body)


post_save.connect(product_changed)
post_delete.connect(product_changed)