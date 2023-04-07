from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response

from Blog_article.models.comment import Comment
from Blog_article.serializers import CommentSerializer


@api_view(['GET'])
def comment_list(request):
    comments = Comment.objects.filter(is_delete=False).select_related('article', 'user')
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def comment_detail(request, comment_id):
    comment = get_object_or_404(Comment.objects.select_related('article', 'user'), id=comment_id, is_delete=False)
    serializer = CommentSerializer(comment)
    return Response(serializer.data)


@api_view(['POST'])
def comment_create(request):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['PUT'])
def comment_update(request, comment_id):
    comment = get_object_or_404(Comment.objects.select_related('article', 'user'), id=comment_id, is_delete=False)
    serializer = CommentSerializer(instance=comment, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment.objects.select_related('article', 'user'), id=comment_id, is_delete=False)
    comment.is_delete = True
    comment.save()
    return Response(status=204)
