# -*- coding: utf-8 -*-

import os, sys, django

sys.path.append("/var/www/mozartdb")
os.environ["DJANGO_SETTINGS_MODULE"] = "mozartdb.settings"
django.setup()

from mozartweb.models import *
from django.contrib.auth.models import User

admin = User.objects.get(id=5)

print admin

#events = Broadcasting.objects.all()
events = Event.objects.all()
print events.count()
i = 0
for e in events:
    if e.created_by == None:
        e.created_by = admin
        e.save()
        i = i + 1
        print e.title, e.created_by
print i

