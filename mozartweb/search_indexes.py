import datetime
from haystack import indexes
from models import Event, Piece


class EventIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
#    piece = indexes.FacetMultiValueField()
    piece = indexes.MultiValueField()

    def prepare_piece(self, obj):
        return [l.name for l in obj.piece.all()]

    def get_model(self):
        return Event

class PieceIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')

    def get_model(self):
        return Piece

#    def index_queryset(self, using=None):
#        """Used when the entire index for model is updated."""
#        return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())
