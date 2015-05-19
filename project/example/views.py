from django.shortcuts import render
from rest_framework import viewsets
from .models import Thing
from .serializers import ThingSerializer


class ThingViewSet(viewsets.ModelViewSet):
    queryset = Thing.objects.all()
    def get_serializer_class(self):
        print 'Method is:', self.request.method
        return ThingSerializer
