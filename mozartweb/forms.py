from dal import autocomplete
from django import forms
from models import *

class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('__all__')
        widgets = {
            'country': autocomplete.ModelSelect2('country-autocomplete'),
            'city': autocomplete.ModelSelect2('city-autocomplete'),
        }

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('__all__')
        widgets = {
            'performer': autocomplete.ModelSelect2Multiple('performer-autocomplete'),
            'piece': autocomplete.ModelSelect2Multiple('piece-autocomplete'),
            'speaker': autocomplete.ModelSelect2Multiple('speaker-autocomplete')
        }

