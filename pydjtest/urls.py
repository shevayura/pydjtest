from django.conf.urls import patterns, include, url
import views, settings

# Uncomment the next two lines to enable the admin:
#
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.productList),
    url(r'^list/(?P<page>\d+)/$', views.productList),
    url(r'^product/(?P<alias>[\w\d_-]+)/$', views.productPage),
    url(r'^edit/(?P<id>\d+)/$', views.productEdit),
    
    url(r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))