from django.db.models.signals import *
from pydjtest.models import Products
from django import template
from django.core.mail import mail_admins

def product_changed(sender, **kwargs):
    tpath   = 'signal_save.html'
    subject = "Product was changed"

    if kwargs['signal'] is post_delete:
        #when delete
        tpath   = "signal_delete.html"
        subject = "Product was deleted"


    mail_body = template.loader.get_template(tpath).render(template.Context(kwargs))
    mail_admins(subject, "%s. See html version for details."%subject, fail_silently=True, html_message=mail_body)


post_save.connect(   product_changed, sender=Products )
post_delete.connect( product_changed, sender=Products )