from crequest.middleware import CrequestMiddleware
from django.utils import timezone

def add_info_log(sender, instance, **kwargs):
    current_request = CrequestMiddleware.get_request()
    if current_request:
        instance.changed_by = current_request.user
    else:
        instance.changed_by = None
    from models import AdditionalInfoLog
    if instance.created_on.strftime("%Y%d%H%M%S") != timezone.now().strftime("%Y%d%H%M%S"):
        a = AdditionalInfoLog.objects.create(changed_by=instance.changed_by, info=instance)
