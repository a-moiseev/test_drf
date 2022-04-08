from rest_framework import serializers
from videos.models import Video


class VideoSerializer(serializers.ModelSerializer):
    """
    Serializer модели Video
    """
    class Meta:
        model = Video
        fields = ['id', 'title', 'date', 'md5', 'file']
