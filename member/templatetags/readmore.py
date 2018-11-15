from django import template
from django.utils.html import escape
from django.utils.safestring import mark_safe

register = template.Library()

import re

readmore_showscript = ''.join([
"this.parentNode.style.display='none';",
"this.parentNode.parentNode.getElementsByClassName('more')[0].style.display='inline';",
"return false;",
]);

@register.filter
def readmore(txt, showwords=15):
    global readmore_showscript
    # words = re.split(r' ', escape(txt))

    if len(txt) <= showwords:
        return txt

    txt = list(txt)

    # wrap the more part
    txt.insert(showwords, '<span class="more" style="display:none;">')
    txt.append('</span>')

    # insert the readmore part
    txt.insert(showwords, '<span class="readmore">... <a href="#" onclick="')
    txt.insert(showwords+1, readmore_showscript)
    txt.insert(showwords+2, '">read more</a>')
    txt.insert(showwords+3, '</span>')

    # Wrap with <p>
    txt.insert(0, '<p>')
    txt.append('</p>')

    return mark_safe(''.join(txt))

readmore.is_safe = True