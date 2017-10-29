"""ccf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.views.generic.base import TemplateView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from aircraft.views import AircraftList, AircraftView
from faq.views import MembershipView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^scribbler/', include('scribbler.urls')),

    url(r'^$', AircraftList.as_view(), name="aircraft"),

    url(r'^aircraft/(?P<tailnum>[A-Z0-9]+)$', 
        AircraftView.as_view(), name="aircraft-detail",),

    url(r'^contact$', 
        TemplateView.as_view(template_name='contact.html'), 
        name="contact"),

    url(r'^membership$', 
        MembershipView.as_view(), name="membership"),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)