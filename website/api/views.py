# from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
from blog.models import Post
# def get_routes(request):

#     routes=[
#         {'GET':'/api/posts'},
#         {'GET': '/api/posts/id'},
#         {'POST': '/api/posts/id/comments'},

#         {'POST':'/api/users/token'},
#         {'POST': '/api/users/token/refresh'},
#     ]

#     return JsonResponse(routes,safe=False)


@api_view(['GET'])
def get_routes(request):

        routes=[
            {'GET':'/api/posts'},
            {'GET': '/api/posts/id'},
            {'POST': '/api/posts/id/comments'},

            {'POST':'/api/users/token'},
            {'POST': '/api/users/token/refresh'},
        ]

        return Response(routes)


@api_view(['GET'])
def get_posts(request):
    posts=Post.objects.all()
    serializer=PostSerializer(posts,many=True)

    return Response(serializer.data)


@api_view(['GET'])
def get_post(request,slug):
    post = Post.objects.get(slug=slug)
    serializer = PostSerializer(post, many=False)

    return Response(serializer.data)
