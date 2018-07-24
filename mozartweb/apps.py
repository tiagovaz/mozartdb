from __future__ import unicode_literals

from django.apps import AppConfig
from watson import search as watson

class MozartwebConfig(AppConfig):
    name = 'mozartweb'
    def ready(self):
        Event = self.get_model("Event")
        watson.register(Event)
