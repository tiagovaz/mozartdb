# -*- coding: utf-8 -*-

import os, sys, django

sys.path.append("/var/www/mozartdb")
os.environ["DJANGO_SETTINGS_MODULE"] = "mozartdb.settings"
django.setup()

from mozartweb.models import *

objs = Performer.objects.all()

for i in objs:
    print i.last_name

