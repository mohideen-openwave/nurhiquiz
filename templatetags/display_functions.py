# oppia/templatetags/display_functions.py
import json
import math
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='get_index')
def get_index(start,index):
    return start+index

@register.filter(name='secs_to_duration')
def secs_to_duration(secs):
    if secs == 0:
        return "-"
    
    if secs < 60:
        return "< 1 min"
    
    if secs < 120:
        return "1 min"
    
    return str(int(math.floor(secs/60))) + " mins"
    
    #minutes = int(math.floor(secs/60))
    #seconds = int(secs - (minutes*60))
    #return str(minutes)+'\''+str(seconds)+'"'

@register.filter(name='title_lang')
@stringfilter
def title_lang(title,lang):
    try:
        titles = json.loads(title)
        if lang in titles:
            return titles[lang]
        else:
            for l in titles:
                return titles[l]
    except:
        pass
    return title