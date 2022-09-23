from rest_framework import generics
from .serializer import ThingSerializer
from .models import Blog
from .permissions import IsOwnerOrReadOnly


class BlogList(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = ThingSerializer


class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Blog.objects.all()
    serializer_class = ThingSerializer
