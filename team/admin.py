from django.contrib import admin
from .models import *

admin.site.register(Team)
admin.site.register(TeamMember)
admin.site.register(TeamRole)
admin.site.register(TeamRecruitPost)