import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mozartdb.settings")
django.setup()
# now your code can go here...

from mozartweb.models import Event

if __name__ == '__main__':    
    events = Event.objects.all()
    for e in events:
        for r in e.relates_to_radio.all():
            print "EVENT: %s RADIO: %s" % (e, r)
