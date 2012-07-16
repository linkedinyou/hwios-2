from django.conf.urls.defaults import patterns, include, url
from dws.core.urls import urls, wurls
from django.conf import settings
from dws.core.views import BootstrapView

urlpatterns = urls
urlpatterns.extend(patterns('',
        (r'^ckeditor/', include('ckeditor.urls')),
        (r'^misc/', include('dws.misc.urls')),

        url(r'^', BootstrapView.as_view(template_name="index.html")),
        
))


wurlpatterns = []
wurlpatterns.extend(wurls)
