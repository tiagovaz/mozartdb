# -*- coding: utf-8 -*-

import os, sys, django
from datetime import datetime
valid_datetime = datetime.strptime('01-01-2017', '%d-%m-%Y')


sys.path.append("/var/www/mozartdb")
os.environ["DJANGO_SETTINGS_MODULE"] = "mozartdb.settings"
django.setup()

from mozartweb.models import *
from django.contrib.auth.models import User


events = Broadcasting.objects.all()
#events = Event.objects.all()
print events.count()
i = 0
for e in events:
    if e.created_on == None:
        e.created_on = valid_datetime
        e.save()
        i = i + 1
        print e.title, e.created_on
print i

