from django.conf.urls import include, url
import gel.views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^$', gel.views.index),
    url(r'^packet/(?P<id>\d+)/$', gel.views.packet),
    url(r'^privacy-policy/$', gel.views.privacy),
    url(r'^colors/$', gel.views.colors),
    url(r'^color/(?P<color>[-\w]+)/$', gel.views.color),
    url(r'^languages/$', gel.views.languages),
    url(r'^language/(?P<language>[-\w]+)/$', gel.views.language),
    url(r'^manufacturers/$', gel.views.manufacturers),
    url(r'^manufacturer/(?P<manufacturer>[-\w]+)/$', gel.views.manufacturer),
    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Enable the admin:
    url(r'^adm/', include(admin.site.urls))
]
