from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from models.serializers import PostSerializer
from models.models import Post


class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-post_date')
    serializer_class = PostSerializer

    @action(detail=False, methods=['get', 'post', ])
    def get_boasts(self, request):
        boasts = Post.objects.filter(post_type=True).order_by('-post_date')

        page = self.paginate_queryset(boasts)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(boasts, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get', 'post'])
    def get_roasts(self, request):
        roasts = Post.objects.filter(post_type=False).order_by('-post_date')

        page = self.paginate_queryset(roasts)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(roasts, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def get_mostpopular(self, request):
        most_popular = sorted(Post.objects.all(),
                              key=lambda votes: votes.total_votes)[::-1]

        page = self.paginate_queryset(most_popular)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(most_popular, many=True)
        return Response(serializer.data)

    @action(detail=True)
    def upvote(self, request, pk):
        post = self.get_object()
        post.upvotes += 1
        post.save()
        return Response({'status': 'upvoted'})

    @action(detail=True)
    def downvote(self, request, pk):
        post = self.get_object()
        post.downvotes += 1
        post.save()
        return Response({'status': 'downvoted'})
