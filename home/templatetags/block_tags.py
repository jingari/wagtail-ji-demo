from django import template
from django.conf import settings
from django.http import Http404

import re
from datetime import datetime
import time
import calendar

register = template.Library()
@register.inclusion_tag( 'imagecarousel.html', takes_context=True )

@register.assignment_tag(takes_context=False)

def timestamp():
	dt = datetime.now()
	ts = dt.microsecond
	return str(ts)