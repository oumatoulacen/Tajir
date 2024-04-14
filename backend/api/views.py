from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status


from .models import Post, User
from .serializers import PostSerializer, UserSerializer

#  welcome home page
def index(request):
    return HttpResponse('Hello, World!')

# user views
# get [users]
class UserListCreateAPIView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


# get a user, update a user or delete a user
class UserDetailAPIView(APIView):
    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, user_id):
        user = User.objects.get(id=user_id)
        serializer = UserSerializer(user, data=request.data, partial=True)  # Enable partial updates

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, user_id):
        user = User.objects.get(id=user_id)
        user.delete()
        return Response(status=204)

# get user's posts or create
class UserPostListAPIView(APIView):
    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        posts = user.post_set.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

# posts views
# get posts or create a new post
class PostListCreateAPIView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

# get a post, update a post or delete a post
class PostDetailAPIView(APIView):
    def get(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id)
            serializer = PostSerializer(post)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response({ 'message': f'post with id {post_id} doesn\'t exist'}, status=404)

    def put(self, request, post_id):
        post = Post.objects.get(id=post_id)
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, post_id):
            try:
                post = Post.objects.get(id=post_id)
                post.delete()
                return Response(status=204)
            except ObjectDoesNotExist:
                return Response({ 'message': f'can\'t delete post with id {post_id}, the post doesn\'t exist'}, status=404)

# authentication views
# register a new user
class RegisterAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

# login a user
class LoginAPIView(APIView):
    def post(self, request):
        print(request.data.get('password'))
        email = request.data.get('email')
        password = request.data.get('password')
        user = User.objects.get(email=email)
        if user.password == password:
            return Response({'message': 'login successful'})
        return Response({'message': 'login failed'}, status=400)

# logout a user
class LogoutAPIView(APIView):
    def post(self, request):
        return Response({'message': 'logout successful'})