from django.conf.urls.defaults import patterns, include, url
from dws.core.urls import wurls
from django.conf import settings
from dws.core.views import BootstrapView


urlpatterns = (patterns('',
        (r'^ckeditor/', include('ckeditor.urls')),
        (r'^', include('dws.core.urls')),

        url(r'^', BootstrapView.as_view(template_name="index.html")),
        
))


wurlpatterns = []
wurlpatterns.extend(wurls)
