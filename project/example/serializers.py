from rest_framework import serializers

class ThingSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=25)
