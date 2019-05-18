from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls import url

from hc.accounts import views as accounts_views

urlpatterns = [
    path('admin/login/', accounts_views.login),
    path('admin/', admin.site.urls),
    path('accounts/', include('hc.accounts.urls')),
    path('projects/add/', accounts_views.add_project, name="hc-add-project"),
    path('projects/<uuid:code>/settings/', accounts_views.project, name="hc-project-settings"),
    path('projects/<uuid:code>/remove/', accounts_views.remove_project, name="hc-remove-project"),
    path('', include('hc.api.urls')),
    path('', include('hc.front.urls')),
    path('', include('hc.payments.urls')),
    path(r'', include('puput.urls')),

    ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

