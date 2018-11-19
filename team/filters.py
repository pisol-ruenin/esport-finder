import django_filters
from .models import Team

class TeamFilter(django_filters.FilterSet):
    class Meta:
        model = Team
        fields = ['name','game']