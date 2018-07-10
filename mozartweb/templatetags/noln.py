# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def noln(value):
    dic = {" »":"&nbsp;»", "« ":"«&nbsp;", " :":"&nbsp;:"}
    for i, j in dic.iteritems():
        value = value.replace(i, j)
    return value
