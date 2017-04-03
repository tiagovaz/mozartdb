from django.contrib import admin
from easy_select2 import select2_modelform
#from mozartweb.forms import RadioDiffusionForm
from mozartweb.models import City, Country, Type, TypeBroadcasting, Speech, Reference, Place, Performer, Piece, Speaker, RadioStation, PerformerType, Comment, Event, Broadcasting

#from forms import *

EventForm = select2_modelform(Event, attrs={'width': '480px'})
BroadcastingForm = select2_modelform(Broadcasting, attrs={'width': '480px'})
PlaceForm = select2_modelform(Place)
RadioStationForm = select2_modelform(RadioStation)
SpeechForm = select2_modelform(Speech)
PerformerForm = select2_modelform(Performer)

class PlaceAdmin(admin.ModelAdmin):
    form = PlaceForm

class RadioStationAdmin(admin.ModelAdmin):
    form = RadioStationForm

class SpeechAdmin(admin.ModelAdmin):
    form = SpeechForm

class PerformerAdmin(admin.ModelAdmin):
    form = PerformerForm


admin.site.register(City)
admin.site.register(Country)
admin.site.register(Type)
admin.site.register(TypeBroadcasting)
admin.site.register(Speech, SpeechAdmin)
admin.site.register(Reference)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Performer, PerformerAdmin)
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

#class RadioDiffusionInline(admin.TabularInline):
#    model = Event.relates_to_radio.through
#    form = RadioDiffusionForm
#    exclude = ('relates_to_radio',)
#    fk_name = 'from_event'
#
class EventAdmin(admin.ModelAdmin):
#    exclude = ('relates_to_radio',)
    exclude = ('bc_key', 'radio_station', 'created_by', 'edited_by')
    form = EventForm
#    inlines = (RadioDiffusionInline, )

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

class BroadcastingAdmin(admin.ModelAdmin):
    exclude = ('created_by', 'edited_by')
    form = BroadcastingForm

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

admin.site.register(Event, EventAdmin)
admin.site.register(Broadcasting, BroadcastingAdmin)
