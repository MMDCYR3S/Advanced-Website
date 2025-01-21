from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status
from .serializers import PostSerializer
from ...models import Post
from rest_framework.views import APIView

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

class PostList(APIView):
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

class PostDetail(APIView):
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