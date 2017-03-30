from django.conf.urls import url, include
from django.contrib import admin

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^admin', include(admin.site.urls)),
    url(r'^wti/api/', include('wti.urls', namespace='wti')),
    url(r'^wti/', include('wtifont.urls', namespace='wtifont')),
]
