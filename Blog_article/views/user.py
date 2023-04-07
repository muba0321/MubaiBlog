from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from django.shortcuts import render, redirect
from rest_framework.utils import json

from Blog_article.models.user import User
from Blog_article.serializers import UserSerializer


def user_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return JsonResponse({'code': 200, 'users': serializer.data})


def user_detail(request, user_id):
    user = User.objects.get(id=user_id)
    serializer = UserSerializer(user)
    return JsonResponse({'code': 200, 'user': serializer.data})


def user_create(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # 解析JSON数据
            name = data.get('name')
            email = data.get('email')
            password = data.get('password')

            if not (name and email and password):
                return JsonResponse({"error": "All fields are required."}, status=400)

            hashed_password = make_password(password)  # 哈希密码

            user = User.objects.create(name=name, email=email, password=hashed_password)  # 使用哈希后的密码创建用户
            return JsonResponse({"message": "User created successfully.", "user_id": user.id})

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data."}, status=400)


def user_update(request, user_id):
    user = User.objects.get(id=user_id)

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user.username = username
        user.email = email
        user.password = password
        user.save()

        serializer = UserSerializer(user)
        return JsonResponse({'code': 200, 'user': serializer.data})
    else:
        return JsonResponse({'code': 400, 'message': 'Invalid request method'})


def user_delete(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_delete = True
    user.save()
    return JsonResponse({'code': 200, 'message': 'User deleted successfully'})
