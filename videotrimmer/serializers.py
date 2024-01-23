from rest_framework import serializers
from videotrimmer.models import Video

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'content')