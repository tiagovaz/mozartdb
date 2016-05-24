from django.contrib import admin

from models import *
from forms import *

class EventAdmin(admin.ModelAdmin):
    fields = ("titre","reference", "place", "poster", "type", "performer", "piece", "speech")




admin.site.register(City)
admin.site.register(Country)
admin.site.register(Type)
class SpeechAdmin(admin.ModelAdmin):
    form = SpeechForm
admin.site.register(Speech, SpeechAdmin)
admin.site.register(Reference)
class PlaceAdmin(admin.ModelAdmin):
    form = PlaceForm
admin.site.register(Place, PlaceAdmin)
admin.site.register(Performer)
admin.site.register(Piece)
admin.site.register(Speaker)
class EventAdmin(admin.ModelAdmin):
    form = EventForm
admin.site.register(Event, EventAdmin)
