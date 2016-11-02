from django.contrib import admin
from mozartweb.forms import SpeechForm, PlaceForm, EventForm
from mozartweb.models import City, Country, Type, Speech, Reference, Place, Performer, Piece, Speaker, RadioStation, PerformerType, Comment, Event

class EventAdmin(admin.ModelAdmin):
    #fields = ("title", "reference", "start_date", "end_date", "place", "poster", "type", "performer", "piece", "speech")
    form = EventForm
    # inlines = [
    #     CommentInline,
    # ]
admin.site.register(Event, EventAdmin)

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
admin.site.register(RadioStation)
admin.site.register(PerformerType)

class CommentAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()
admin.site.register(Comment, CommentAdmin)

class CommentInline(admin.TabularInline):
    model = Comment
    fields = ('content', 'user')
    extra = 0

