from django.contrib import admin
from forms import *

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

class CommentAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()
admin.site.register(Comment, CommentAdmin)

class CommentInline(admin.TabularInline):
    model = Comment
    fields = ('content', 'user')
    extra = 0

class EventAdmin(admin.ModelAdmin):
    #fields = ("title", "reference", "start_date", "end_date", "place", "poster", "type", "performer", "piece", "speech")
    form = EventForm
    inlines = [
        CommentInline,
    ]
admin.site.register(Event, EventAdmin)