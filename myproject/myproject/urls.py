from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^$', 'cms_put.views.mostrar_todo'),
    url(r'^(\d+)$', 'cms_put.views.mostrar_id'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(.*)', 'cms_put.views.contenido'),
)
