from crispy_forms.helper import FormHelper
#from dal import autocomplete
from django import forms
from crispy_forms.layout import Layout, Submit, Div

from models import *

class Search(forms.ModelForm, Layout):
    helper = FormHelper()
    helper.form_method = 'GET'
    helper.form_action = '/result/'
    helper.add_input(Submit('submit', 'Chercher'))

    class Meta:
        model = Event
        fields = '__all__'


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('__all__')

class RadioDiffusionForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ('relates_to_radio',)

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('__all__')

class SpeechForm(forms.ModelForm):
    class Meta:
        model = Speech
        fields = ('__all__')

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = [
            'content'
        ]

        widgets = {
            'content': forms.Textarea(
                attrs={
                    'placeholder': "Votre commentaire ici."
                }
            ),
        }
