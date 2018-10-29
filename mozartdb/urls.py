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
from django.views.decorators.cache import cache_page
from django.core.cache import cache



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(
        r'^login$',
        'django.contrib.auth.views.login',
        kwargs={'template_name': 'login.html'},
        name='login'
    ),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name="logout"),
#    url(r'^country-autocomplete/$', CountryAutocomplete.as_view(), name='country-autocomplete',),
#    url(r'^city-autocomplete/$', CityAutocomplete.as_view(), name='city-autocomplete',),
#    url(r'^piece-autocomplete/$', PieceAutocomplete.as_view(), name='piece-autocomplete',),
#    url(r'^performer-autocomplete/$', PerformerAutocomplete.as_view(), name='performer-autocomplete',),
#    url(r'^speaker-autocomplete/$', SpeakerAutocomplete.as_view(), name='speaker-autocomplete',),
#    url(r'^speech-autocomplete/$', SpeechAutocomplete.as_view(), name='speech-autocomplete',),
#    url(r'^place-autocomplete/$', PlaceAutocomplete.as_view(), name='place-autocomplete',),
#    url(r'^reference-autocomplete/$', ReferenceAutocomplete.as_view(), name='reference-autocomplete',),
#    url(r'^radio-autocomplete/$', RadioAutocomplete.as_view(), name='radio-autocomplete',),
    url(
            r'^list/$',
            cache_page(60 * 60 * 24, key_prefix="event_list")(EventList.as_view()),
            name='event_list'
        ),
    url(
            r'^$',
            EventList.as_view(),
            name='event'
        ),
    url(
            r'^(?P<pk>\d+)$',
            cache_page(60 * 60 * 24, key_prefix="event_detail")(EventDetail.as_view()),
            name='event_detail'
        ),
    url(
            r'^(?P<pk>\d+)/new_comment$',
            cache_page(60 * 60 * 24, key_prefix="comment_create")(CommentCreate.as_view()),
            name='comment_create'
        ),
    url(
            r'^(?P<pk>\d+)/new_info$',
            cache_page(60 * 60 * 24, key_prefix="info_create")(InfoCreate.as_view()),
            name='info_create'
        ),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
