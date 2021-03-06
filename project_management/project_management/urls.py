# urls.py: deployment-specific URLs, including some required for the tasks submodule
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import tasks.urls

urlpatterns = patterns('',
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(tasks.urls, namespace="tasks"))
)
