from django.shortcuts import render, redirect
from Blog_article.models.user import User
from Blog_article.serializers import UserSerializer


def user_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return render(request, {'users': serializer.data})


def user_detail(request, user_id):
    user = User.objects.get(id=user_id)
    serializer = UserSerializer(user)
    return render(request, 'user_detail.html', {'user': serializer.data})


def user_create(request):
    if request.method == 'POST':
        # 获取表单数据
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # 创建用户对象
        user = User.objects.create(username=username, email=email, password=password)

        # 序列化并返回创建的用户对象
        serializer = UserSerializer(user)
        return redirect('user_detail', user_id=serializer.data['id'])
    else:
        # 显示创建用户表单
        return render(request, 'user_create.html')


def user_update(request, user_id):
    user = User.objects.get(id=user_id)

    if request.method == 'POST':
        # 获取表单数据
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # 更新用户对象
        user.username = username
        user.email = email
        user.password = password
        user.save()

        # 序列化并返回更新的用户对象
        serializer = UserSerializer(user)
        return redirect('user_detail', user_id=serializer.data['id'])
    else:
        # 显示更新用户表单
        serializer = UserSerializer(user)
        return render(request, 'user_update.html', {'user': serializer.data})


def user_delete(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_delete = True
    user.save()
    return redirect('user_list')