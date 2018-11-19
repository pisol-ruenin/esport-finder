import django_filters
from .models import UserProfile

class MemberFilter(django_filters.FilterSet):
    class Meta:
        model = UserProfile
        fields = ['codename','game','rank','role','province']