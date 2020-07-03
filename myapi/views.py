from rest_framework import viewsets

from mysite.serializers import HeroSerializer
from myapi.models import Hero


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer