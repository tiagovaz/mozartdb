"""mozartdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from mozartweb.views import CountryAutocomplete, CityAutocomplete, PerformerAutocomplete, PieceAutocomplete
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^country-autocomplete/$', CountryAutocomplete.as_view(), name='country-autocomplete',),
    url(r'^city-autocomplete/$', CityAutocomplete.as_view(), name='city-autocomplete',),
    url(r'^piece-autocomplete/$', PieceAutocomplete.as_view(), name='piece-autocomplete',),
    url(r'^performer-autocomplete/$', PerformerAutocomplete.as_view(), name='performer-autocomplete',)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
