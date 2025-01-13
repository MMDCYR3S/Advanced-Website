from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
from ...models import Post

# Post list function
@api_view()
def post_list(request):
    return Response("OK!")

# show post detail
@api_view()
def post_detail(request, id):
    """ Summary:
        Gets Information from posts and with serializer,
        convert it into json and then show it to the page.
    """
    try:
        post = Post.objects.get(pk=id)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    except Post.DoesNotExist:
        return Response("Post does not exists!")
    except Post.objects.filter(status=False):
        return Response("This post has not published yet!")