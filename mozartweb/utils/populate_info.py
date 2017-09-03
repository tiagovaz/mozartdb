# -*- coding: utf-8 -*-

import os, sys, django

sys.path.append("/var/www/mozartdb_test")
os.environ["DJANGO_SETTINGS_MODULE"] = "mozartdb.settings"
django.setup()

from mozartweb.models import *

comments = Comment.objects.all()
#info =  AdditionalInfo.objects.all()
#
#for i in info:
#    i.delete()
#
for c in comments:
    if c.event is None:
        print "NO EVENT AT " + c.content
    if c.user is None:
        print "NO USER AT " + c.content
    else:
        AdditionalInfo.objects.create(content = c.content, created_on = c.created_date, created_by = c.user, event = c.event)
