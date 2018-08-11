import datetime
from haystack import indexes
from models import *

class EventIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
#    piece = indexes.FacetMultiValueField()
     # FIXME: note sure if this is necessary:
    piece = indexes.MultiValueField()
    performer = indexes.MultiValueField()

    def prepare_piece(self, obj):
        return [l.name for l in obj.piece.all()]

    def prepare_performer(self, obj):
        return [l.get_fullname for l in obj.performer.all()]


    def get_model(self):
        return Event

class PieceIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')

    def get_model(self):
        return Piece

class PerformerIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    first_name = indexes.CharField(model_attr='first_name')
    last_name = indexes.CharField(model_attr='last_name')

    def get_model(self):
        return Performer

class SpeechIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')

    def get_model(self):
        return Speech

class SpeakerIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    first_name = indexes.CharField(model_attr='first_name')
    last_name = indexes.CharField(model_attr='last_name')

    def get_model(self):
        return Speaker

class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    article_title = indexes.CharField(model_attr='article_title')

    def get_model(self):
        return Reference

#    def index_queryset(self, using=None):
#        """Used when the entire index for model is updated."""
#        return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())
