from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser

from .models import Video
from .serializers import VideoSerializer


class UploadVideo(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    parser_classes = [MultiPartParser]

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
