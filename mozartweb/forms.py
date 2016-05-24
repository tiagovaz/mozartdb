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
            'speech': autocomplete.ModelSelect2Multiple('speech-autocomplete'),
            'place': autocomplete.ModelSelect2('place-autocomplete')
        }

class SpeechForm(forms.ModelForm):
    class Meta:
        model = Speech
        fields = ('__all__')
        widgets = {
            'speaker': autocomplete.ModelSelect2Multiple('speaker-autocomplete')
        }