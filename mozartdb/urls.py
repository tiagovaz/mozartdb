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

from mozartweb.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^country-autocomplete/$', CountryAutocomplete.as_view(), name='country-autocomplete',),
    url(r'^city-autocomplete/$', CityAutocomplete.as_view(), name='city-autocomplete',),
    url(r'^piece-autocomplete/$', PieceAutocomplete.as_view(), name='piece-autocomplete',),
    url(r'^performer-autocomplete/$', PerformerAutocomplete.as_view(), name='performer-autocomplete',),
    url(r'^speaker-autocomplete/$', SpeakerAutocomplete.as_view(), name='speaker-autocomplete',),
    url(r'^speech-autocomplete/$', SpeechAutocomplete.as_view(), name='speech-autocomplete',),
    url(r'^place-autocomplete/$', PlaceAutocomplete.as_view(), name='place-autocomplete',),
    url(r'^reference-autocomplete/$', ReferenceAutocomplete.as_view(), name='reference-autocomplete',),
    url(r'^radio-autocomplete/$', RadioAutocomplete.as_view(), name='radio-autocomplete',),
    url(
            r'^list/$',
            EventList.as_view(),
            name='event_list'
        ),
    url(
            r'^$',
            EventList.as_view(),
            name='event'
        ),
    url(
            r'^(?P<pk>\d+)$',
            EventDetail.as_view(),
            name='event_detail'
        ),
    url(
            r'^(?P<pk>\d+)/new_comment$',
            CommentCreate.as_view(),
            name='comment_create'
        ),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
