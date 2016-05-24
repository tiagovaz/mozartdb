from django.contrib import admin

from models import *
from forms import *

#class EventAdmin(admin.ModelAdmin):
#    raw_id_fields = ("performer",)


admin.site.register(City)
admin.site.register(Country)
admin.site.register(Type)
admin.site.register(Speech)

class PlaceAdmin(admin.ModelAdmin):
    form = PlaceForm
admin.site.register(Place, PlaceAdmin)
admin.site.register(Performer)
admin.site.register(Piece)
admin.site.register(Speaker)

class EventAdmin(admin.ModelAdmin):
    form = EventForm
admin.site.register(Event, EventAdmin)
