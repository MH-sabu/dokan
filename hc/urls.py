from django.contrib import admin
from django.urls import include, path

from hc.accounts import views as accounts_views

urlpatterns = [
    
    path("accounts/", include("hc.accounts.urls")),
    
    path("", include("hc.api.urls")),
    path("", include("hc.front.urls")),
    path("", include("hc.payments.urls")),
]
