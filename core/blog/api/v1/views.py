from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import status

from .serializers import PostSerializer, CategorySerializer
from ...models import Post, Category

from rest_framework.views import APIView
from rest_framework import mixins 

from rest_framework.generics import (
    GenericAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)

from rest_framework import viewsets

from rest_framework.routers import DefaultRouter


# Post list function
"""@api_view(["GET","POST"])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_list(request):
    if request.method == "GET":
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)"""

'''class PostList(APIView):
    """ Summary:
        Getting a list of posts and creating new posts
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    
    def get(self, request):
        """ Summary:
            Retriveing a list of  posts
        """
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        """ Summary:
            Creating a post with provided data
        """
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
'''

# Post list with GenericView
class PostList(ListCreateAPIView):
    """ Getting a list of posts and creating new posts """
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

        
    def get(self, request, *args, **kwargs):
        """ Retrieving a list of posts """
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """ Create a post object """
        return self.create(request, *args, **kwargs)
    
# show post detail
'''@api_view(["DELETE","GET","PUT"])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_detail(request, id):
    """ Summary:
        Gets Information from posts and with serializer,
        convert it into json and then show it to the page.
    """
    post = get_object_or_404(Post, pk=id, status=True)
    # Simple way
    if request.method == "GET":
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = PostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
        post.delete()
        return Response({"Detail" : "Your post has been delete successfully."}, status=status.HTTP_204_NO_CONTENT)
        '''

# Post Detail with APIView
'''class PostDetail(APIView):
    """ Summary:
        Showing a detail of a post and edit plus removing it
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    
    def get(self, request, id):
        """ Summary:
            Retriveing the post data
        """
        post = get_object_or_404(Post, pk=id, status=True) 
        serializer = self.serializer_class(post)
        return Response(serializer.data)

    def put(self, request, id):
        """ Summary:
            Editing the post data
        """
        post = get_object_or_404(Post, pk=id, status=True) 
        serializer = self.serializer_class(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, id):
        """ Summary:
            Deleting the post object
        """
        post = get_object_or_404(Post, pk=id, status=True) 
        post.delete()
        return Response({"Detail" : "Your post has been delete successfully."}, status=status.HTTP_204_NO_CONTENT)

    # try:
    #     post = Post.objects.get(pk=id)
    #     serializer = PostSerializer(post)
    #     return Response(serializer.data)
    # except Post.DoesNotExist:
    #     return Response({"Detail":"Post does not exists!"}, status=status.HTTP_404_NOT_FOUND)
    '''

# Post detail with GenericView
class PostDetail(RetrieveUpdateDestroyAPIView):
    """ Showing a detail of a post and edit plus removing it with GenericView"""
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    # lookup_field = 'id'
    
    def get(self, request, *args, **kwargs):
        """ Retrieving a post object """
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        """ Editing a post object """
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        """ Deleting a post object """
        return self.destroy(request, *args, **kwargs)
    
    # def get(self, request, id):
    #     """ Retriveing the post data """
    #     post = get_object_or_404(Post, pk=id, status=True) 
    #     serializer = self.serializer_class(post)
    #     return Response(serializer.data)

# Posts with ViewSets in CBV - (ViewSet and ModelViewSet)
class PostModelViewSet(viewsets.ModelViewSet):
    """ Show, create, edit and delete any post with ViewSets """
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    
    @action(methods=['get'], detail=False)
    def get_ok(self, request):
        """ Creating extra items """
        return Response({'Detail' : 'OK'})
    
# Category with ModelViewSet
class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
        