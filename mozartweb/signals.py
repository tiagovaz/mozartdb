from crequest.middleware import CrequestMiddleware

def add_info_log(sender, instance, **kwargs):
    current_request = CrequestMiddleware.get_request()
    if current_request:
        instance.changed_by = current_request.user
    else:
        instance.changed_by = None
    from models import AdditionalInfoLog
    a = AdditionalInfoLog.objects.create(changed_by=instance.changed_by, info=instance)
