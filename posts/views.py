from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.exceptions import ValidationError
#following is added to show proper output when a user without login try to access the api
from rest_framework import permissions

#to allow delete the vote
from rest_framework import mixins
from rest_framework import status
from rest_framework.response import Response

from .models import Post, Vote
from .serializers import PostSerializer
from .serializers import VoteSerializer

# Create your views here.
#class PostList(generics.ListAPIView):
#following is added to allow create post using post request
class PostList(generics.ListCreateAPIView):
    
    queryset = Post.objects.all()
    serializer_class=PostSerializer
    
    #following is added to show proper output when a user without login try to access the api
    
    #permission_classes = [permissions.IsAuthenticated]
    #allow to read post but not to create if not logged in
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    #without following line even with create it will show error when we want to automatically put poster_id and poster
    
    def perform_create(self, serializer):
        #serializer is holding django model here
        serializer.save(poster=self.request.user)

#created to allow delete post through api
class PostRetrieveDestroy(generics.RetrieveDestroyAPIView):
    
    queryset = Post.objects.all()
    serializer_class=PostSerializer
    
    #following is added to show proper output when a user without login try to access the api
    
    #permission_classes = [permissions.IsAuthenticated]
    #allow to read post but not to create if not logged in
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    #following fn to allow delete by the owner of post only
    def delete(self, request, *args, **kwargs):
        user = self.request.user
        post=Post.objects.filter(pk=kwargs['pk'], poster=user)
        if post.exists():
            return self.destroy(request, *args, **kwargs)    
        else:
            raise ValidationError("You don't have permission to delete this post")


class VoteCreate(generics.CreateAPIView, mixins.DestroyModelMixin):
    
    serializer_class=VoteSerializer
    
    #following is added to show proper output when a user without login try to access the api
    
    #permission_classes = [permissions.IsAuthenticated]
    #allow to read post but not to create if not logged in
    permission_classes = [permissions.IsAuthenticated]
    
    #define query set on which vote is to be performed
    def get_queryset(self):
        user = self.request.user
        #pk is passed through url and is defined in urls.py
        post = Post.objects.get(pk=self.kwargs['pk'])
        return Vote.objects.filter(voter=user, post=post)
    
    def perform_create(self, serializer):
        #perform a check to see i fthe user has already voted for this post
        if self.get_queryset().exists():
            raise ValidationError('You have already voted for this post')
        #serializer is holding django model here
        user = self.request.user
        post = Post.objects.get(pk=self.kwargs['pk'])
        serializer.save(voter=user, post=post)    
    
    def delete(self, request, *args, **kargs):
        #check if the vote exists
        if self.get_queryset().exists():
            self.get_queryset().delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise ValidationError('You never voted for this post')

def help(request):
    return render(request, 'posts/help.html')

