from rest_framework import generics
from .serializer import ThingSerializer
from .models import Thing


class ThingList(generics.ListAPIView):
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer


class ThingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer
