from rest_framework import serializers
from ...models import Post , Category
from accounts.models import Profile , User

# Serialize posts
# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=250)

# Model Serializer categories
class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = "__all__" #["id", "name"]

# Model Serializer posts
class PostSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source='get_snippet')
    relative_url = serializers.URLField(source='get_absolute_api_url', read_only=True)
    absolute_url = serializers.SerializerMethodField(method_name='get_abs_url')
    # category = serializers.SlugRelatedField(many=False, slug_field='name', queryset=Category.objects.all())
    # category = CategorySerializer()
    
    
    # باید در نظر داشت که چه فیلدی باید رید اونلی شود، یعنی مهم
    # است که امنیت به چه صورت باشد که به ضرر کار نباشد
    # content = serializers.ReadOnlyField()
    # content = serializers.CharField(read_only=True)
    class Meta:
        model = Post
        exclude = ["updated_date", "image"]
        # fields = "__all__"
        #read_only_fields = ['content', 'title']
        read_only_fields = ['author']
        
    def get_abs_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)
    
    def to_representation(self, instance):
        request = self.context.get('request')
        rep = super().to_representation(instance)
        if request.parser_context.get('kwargs').get('pk'):
            rep.pop('snippet', None)
            rep.pop('relative_url', None)
            rep.pop('absolute_url', None)
        else:
            rep.pop('content', None)
            
        rep['category'] = CategorySerializer(instance.category, context={'request': request}).data
        return rep
    
    def create(self, validated_data):
        # user = User.objects.get(id= self.context.get('request').user.id)
        # validated_data['author'] = Profile.objects.get(user = user)
        validated_data['author'] = Profile.objects.get(user__id = self.context.get('request').user.id)
        return super().create(validated_data)

    