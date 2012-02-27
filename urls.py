from django.conf.urls.defaults import patterns, include, url
from dws.core.urls import urlpatterns as urls, wurlpatterns as wurls
from django.conf import settings
from dws.core.views import BootstrapView

urlpatterns = urls
urlpatterns += patterns('',
        url(r'^', BootstrapView.as_view(template_name="index.html")),
)

wurlpatterns = [].extend(wurls)