from crispy_forms.helper import FormHelper
from dal import autocomplete
from django import forms
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, HTML, Field, Div
from django.views import generic

from models import *

class Search(forms.ModelForm, Layout):
    helper = FormHelper()
    helper.form_method = 'GET'
    helper.form_action = '/result/'
    helper.add_input(Submit('submit', 'Chercher'))

    helper.layout = Layout (
                Div(
                    Div( 'title', css_class='col-sm-12'),
                    Div( 'reference', css_class='col-sm-12'),
                    Div( 'place', css_class='col-sm-12'),
                    Div( 'place', css_class='col-sm-12'),
                    Div( 'place', css_class='col-sm-12'),
                    Div( 'type', css_class='col-sm-12'),
                    Div( 'performer', css_class='col-sm-12'),
                    Div( 'speech', css_class='col-sm-12'),
                    Div( 'speaker', css_class='col-sm-12'),
                    Div( 'start_date', css_class='col-sm-12'),
                    Div( 'end_date', css_class='col-sm-12'),
                    css_class='row'
            ),
    )

    class Meta:
        model = Event
        fields = '__all__'


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