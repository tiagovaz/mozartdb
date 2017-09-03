# -*- coding: utf-8 -*-

import os, sys, django

sys.path.append("/var/www/mozartdb")
os.environ["DJANGO_SETTINGS_MODULE"] = "mozartdb.settings"
django.setup()

from mozartweb.admin import *

event_resource = EventResource()
dataset = event_resource.export()
dataset.csv
