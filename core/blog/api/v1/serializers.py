from rest_framework import serializers

# Serialize posts
class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=250)
    
    