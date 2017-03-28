# coding: utf-8

from django.conf.urls import url, include
from django.contrib import admin

from sample_api.urls import router as sample_api_router
from sample_api import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # sample_api.urlsをincludeする
    url(r'^api/', include(sample_api_router.urls)),
    url(r'^affi$', views.affi_list),
    url(r'^affi/amazon$', views.amazon_list),
    url(r'^affi/yahoo$', views.yahoo_list),
    url(r'^affi/itunes$', views.itunes_list),

]