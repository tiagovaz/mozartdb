from django.contrib import admin
#from mozartweb.forms import SpeechForm, PlaceForm, EventForm
#from mozartweb.models import City, Country, Type, Speech, Reference, Place, Performer, Piece, Speaker, RadioStation, PerformerType, Comment, Event

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

class EventAdmin(admin.ModelAdmin):
    form = EventForm
    def save_model(self, request, obj, form, change): 
        instance = form.save(commit=False)
        if not hasattr(instance,'created_by'):
            instance.created_by = request.user
        instance.edited_by = request.user
        instance.save()
        form.save_m2m()
        return instance

    def save_formset(self, request, form, formset, change): 

        def set_user(instance):
            if not instance.created_by:
                instance.created_by = request.user
            instance.edited_by = request.user
            instance.save()

        if formset.model == Article:
            instances = formset.save(commit=False)
            map(set_user, instances)
            formset.save_m2m()
            return instances
        else:
            return formset.save()

    #fields = ("title", "reference", "start_date", "end_date", "place", "poster", "type", "performer", "piece", "speech")
    # inlines = [
    #     CommentInline,
    # ]
admin.site.register(Event, EventAdmin)
