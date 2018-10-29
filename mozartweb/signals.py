from crequest.middleware import CrequestMiddleware
from django.utils import timezone
from django.core.cache import cache

def add_info_log(sender, instance, **kwargs):
    current_request = CrequestMiddleware.get_request()
    if current_request:
        instance.changed_by = current_request.user
    else:
        instance.changed_by = None
    from models import AdditionalInfoLog, AdditionalInfo
    if instance.created_on.strftime("%Y%d%H%M%S") != timezone.now().strftime("%Y%d%H%M%S"):
        # Do not log if same people + same event + same day
        infos_for_this_event = AdditionalInfoLog.objects.filter(info__event=instance.event)
        for i in infos_for_this_event:
            if i.changed_on.strftime("%d%m%y") == timezone.now().strftime("%d%m%y") and i.changed_by == instance.changed_by:
                i.delete()
        a = AdditionalInfoLog.objects.create(changed_by=instance.changed_by, info=instance)

def clear_info_cache(sender, instance, **kwargs):
    cache.delete_pattern("*info*")
    cache.delete_pattern("*event*")

def clear_comment_cache(sender, instance, **kwargs):
    cache.delete_pattern("*comment*")
    cache.delete_pattern("*event*")

def clear_event_cache(sender, instance, **kwargs):
    cache.delete_pattern("*event*")
