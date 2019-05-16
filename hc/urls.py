from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls import url
from puput import urls as puput_urls

from hc.accounts import views as accounts_views

urlpatterns = [
    
    path("accounts/", include("hc.accounts.urls")),
    
    path("", include("hc.api.urls")),
    path("", include("hc.front.urls")),
    path("", include("hc.payments.urls")),
    path('', include('puput.urls')),
    ]



if settings.DEBUG:
    import os
    from django.conf.urls.static import static
    from django.views.generic.base import RedirectView
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns() # tell gunicorn where static files are in dev mode
    urlpatterns += static(settings.MEDIA_URL + 'images/', document_root=os.path.join(settings.MEDIA_ROOT, 'images'))
    urlpatterns += [
        url(r'^favicon\.ico$', RedirectView.as_view(url=settings.STATIC_URL + 'myapp/images/favicon.ico')),
    ]