from rest_framework import serializers
from ...models import Post

# Serialize posts
# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=250)


# Model Serializer posts
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        # fields = "__all__"
        exclude = ["updated_date", "image", "category"]
    
    